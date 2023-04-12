import argparse
import re
from azure.identity import DefaultAzureCredential, AzureCliCredential
from azure.core.credentials import AzureKeyCredential
from azure.storage.blob import BlobServiceClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import *
from azure.search.documents import SearchClient

parser = argparse.ArgumentParser(description="Load documents into a Cognitive Search index.")
parser.add_argument("--category", help="Value for the category field in the search index for all sections indexed in this run")
parser.add_argument("--storageaccount", help="Azure Blob Storage account name")
parser.add_argument("--container", help="Azure Blob Storage container name")
parser.add_argument("--blobsprefix", help="Prefix for blobs to index (e.g. 'docs/')")
parser.add_argument("--storagekey", required=False, help="Optional. Use this Azure Blob Storage account key instead of the current user identity to login (use az login to set current user for Azure)")
parser.add_argument("--searchservice", help="Name of the Azure Cognitive Search service where content should be indexed (must exist already)")
parser.add_argument("--index", help="Name of the Azure Cognitive Search index where content should be indexed (will be created if it doesn't exist)")
parser.add_argument("--searchkey", required=False, help="Optional. Use this Azure Cognitive Search account key instead of the current user identity to login (use az login to set current user for Azure)")
parser.add_argument("--deleteindexfirst", action="store_true", help="Delete and re-create the search index.")
parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
args = parser.parse_args()

default_creds = AzureCliCredential() if args.searchkey == None or args.storagekey == None else None
search_creds = default_creds if args.searchkey == None else AzureKeyCredential(args.searchkey)
storage_creds = default_creds if args.storagekey == None else args.storagekey

# Create (or re-create) the search index
if args.verbose: print(f"Ensuring search index {args.index} exists")
index_client = SearchIndexClient(endpoint=f"https://{args.searchservice}.search.windows.net/",
                                    credential=search_creds)
index_list = index_client.list_index_names()
if args.deleteindexfirst and args.index in index_list:
    if args.verbose: print(f"Deleting search index {args.index}")
    index_client.delete_index(args.index)
if args.index not in index_list or args.deleteindexfirst:
    index = SearchIndex(
        name=args.index,
        fields=[
            SimpleField(name="id", type="Edm.String", key=True),
            SearchableField(name="content", type="Edm.String", analyzer_name="en.microsoft"),
            SimpleField(name="category", type="Edm.String", filterable=True, facetable=True),
            SimpleField(name="sourcefile", type="Edm.String", filterable=True, facetable=True)
        ],
        semantic_settings=SemanticSettings(
            configurations=[SemanticConfiguration(
                name='default',
                prioritized_fields=PrioritizedFields(
                    title_field=None, prioritized_content_fields=[SemanticField(field_name='content')]))])
    )
    if args.verbose: print(f"Creating {args.index} search index")
    index_client.create_index(index)
else:
    if args.verbose: print(f"Search index {args.index} already exists")

# Read blobs and push their content/metadata into the search index
search_client = SearchClient(endpoint=f"https://{args.searchservice}.search.windows.net/",
                                index_name=args.index,
                                credential=search_creds)
blob_service = BlobServiceClient(account_url=f"https://{args.storageaccount}.blob.core.windows.net", credential=storage_creds)
blob_container = blob_service.get_container_client(args.container)

if args.verbose: print(f"Indexing files in container '{args.container}' into search index '{args.index}'")
i = 0
batch = []
for blob_name in blob_container.list_blob_names(name_starts_with=args.blobsprefix):
    blob = blob_container.get_blob_client(blob_name)
    if args.verbose: print(f"Downloading {blob_name}")
    content = blob_text = blob.download_blob().readall().decode("utf-8")
    cleaned_id = re.sub("[^a-zA-Z0-9]", "-", blob_name)
    batch.append({"id": cleaned_id, "content": content, "category": args.category, "sourcefile": blob_name})
    i += 1
    if i % 100 == 0:
        results = search_client.upload_documents(documents=batch)
        succeeded = sum([1 for r in results if r.succeeded])
        if args.verbose: print(f"Indexed {len(results)} blobs, {succeeded} succeeded")
        batch = []

if len(batch) > 0:
    results = search_client.upload_documents(documents=batch)
    succeeded = sum([1 for r in results if r.succeeded])
    if args.verbose: print(f"Indexed {len(results)} sections, {succeeded} succeeded")
