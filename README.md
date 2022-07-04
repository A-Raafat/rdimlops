# rdimlops

This repo has the UI of the task

The CI is done using Github action, which runs the tests inside `app/test_api.py` using pytest and the CD is done using heroku which waits for the CI then deploys the app on its free cloud service 

To test the UI app, go to https://rdimlops.herokuapp.com/

Or you can Curl to upload and check the prediction 
```bash

curl -X 'POST'   'http://rdimlops.herokuapp.com/'  \
     -H 'accept: application/json'   \
     -H 'Content-Type: multipart/form-data' \
     -F 'file=@img.jpg;type=image/jpeg' | grep "<p>"

```
