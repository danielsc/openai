source .env
az ml job create --subscription 15ae9cb6-95c1-483d-a0e3-b1a1a3b06324 --resource-group ray --workspace-name ray --file "/Users/danielsc/git/openai/batch_score_rag.yaml" --stream --set environment_variables.OPENAI_API_BASE=$OPENAI_API_BASE --set environment_variables.OPENAI_API_KEY=$OPENAI_API_KEY --set environment_variables.COG_SEARCH_ENDPOINT=$COG_SEARCH_ENDPOINT --set environment_variables.SERPAPI_API_KEY=$SERPAPI_API_KEY --set environment_variables.COG_SEARCH_KEY=$COG_SEARCH_KEY