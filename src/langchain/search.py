from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import os

endpoint = "https://gptkb-73g2mkes5kahm.search.windows.net/"
index_name = "amldocs"
searchkey = os.environ["COG_SEARCH_KEY"]

client = SearchClient(endpoint=endpoint, index_name=index_name, credential=AzureKeyCredential(searchkey))

for i in client.search("virtual machines", top=1):
    print(i['sourcefile'])
    print(i['content'])
