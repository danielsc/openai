mlflow models predict -m data/5model/model -i data/6score/yelp_text_small.csv -t csv

mlflow models serve -m data/5model/model 

curl http://127.0.0.1:5000/invocations -H 'Content-Type: application/json' -d '{
    "columns": ["text"],
    "data": [["awesome!!! best place ever."], ["terrible, terrible food"]]
}'

Azureml:
{"input_data": {
    "columns": ["text"],
    "data": [["Awesome....\n\nYou have to go at least once in your life."],["This place shouldn't even be reviewed - because it is the kind of place I want to keep for myself... =)"]]
}}

MLFlow:
{
    "columns": ["text"],
    "data": [["awesome!!! best place ever."], ["terrible, terrible food"]]
}

Azureml:
{"input_data": {
    "columns": ["text"],
    "data": [["Awesome....\n\nYou have to go at least once in your life. \n\n###\n\n"],["This place shouldn't even be reviewed - because it is the kind of place I want to keep for myself... =)"]]
}}