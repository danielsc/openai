source .env
python src/search/indexblobs.py --storageaccount build20238715997449 --container "azureml-blobstore-a23c27e8-7bff-4c18-bf5a-ffb8f5ed882d" --blobsprefix "UI/2023-04-06_191207_UTC/simple-4000-100/" --searchservice gptkb-73g2mkes5kahm --index amldocs -v --deleteindexfirst --searchkey $COG_SEARCH_KEY
