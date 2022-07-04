# rdimlops

This repo has the API of the task

To test the API functionality, go to https://rdi-mlops-api.herokuapp.com/docs

You can either use the curl the deployed API using the following Curl command

```bash

curl -X 'POST' \
  'https://rdi-mlops-api.herokuapp.com/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@image.jpg;type=image/jpeg'
  
```
