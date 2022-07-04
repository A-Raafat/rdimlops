# RDI MLOps Task

This branch has the API of the task

This repo contains the CI/CD of the task, CI is done by using Github actions, it will run the test function in `app/test_api.py` using pytest, which checks the home page and the predict function api

To test the API functionality manually, go to https://rdi-mlops-api.herokuapp.com/docs

or 

You can check the deployed API using the following Curl command

```bash

curl -X 'POST' \
  'https://rdi-mlops-api.herokuapp.com/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@image.jpg;type=image/jpeg'
  
```


Another method is to download the repository and build docker image using the command

```bash

sudo docker build -t name:tag .

```

then run the docker image using the command

```bash

sudo docker run --rm -p 80:80 -it name:tag

```

Now you have the docker image deployed and you can access it with the link https://localhost:80, you will see the welcome message

Then you can go to localhost/docs to test the API using the FastAPI UI

or by also using curl


# Endpoints

## HOME [GET]

This endpoint checks whether a server is up and running or not

#### Request URL

https://rdi-mlops-api.herokuapp.com/  (for cloud deployment)
https://localhost/ (for local deployment)

#### Request parameters

NA

#### Request Body

NA

#### Request Response

200 OK

#### Representation

```json
"Welcome to Covid classifier by Ahmed Raafat, Please visit localhost/docs for the fastapi UI"
```

#### Code example

```bash

curl -X 'GET' \
  'https://rdi-mlops-api.herokuapp.com/' \
  -H 'accept: application/json'
  
```


## Predict [POST]

This endpoint is for classifying the image as covid or normal

#### Request URL

https://rdi-mlops-api.herokuapp.com/docs#/default/predict_predict_post (deployed api on cloud)
https:localhost/predict (for local deployment)

#### Request parameters

NA

#### Request Body

NA

#### Request Response

200 OK

#### Representation

```json
{
  "result": {
    "Prediction": "Normal",
    "Score": "98.9%"
  }
}
```

#### Code example

```bash

curl -X 'POST' \
  'https://rdi-mlops-api.herokuapp.com/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@img.jpg;type=image/jpeg'
  
```
