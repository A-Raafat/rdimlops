# rdimlops

This repo has the UI of the task

To test the app, go to https://rdimlops.herokuapp.com/

Or you can Curl to upload and check the prediction 
```bash

curl -X 'POST'   'http://rdimlops.herokuapp.com/'  \
     -H 'accept: application/json'   \
     -H 'Content-Type: multipart/form-data' \
     -F 'file=@img.jpg;type=image/jpeg' | grep "<p>"

```
