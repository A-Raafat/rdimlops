import joblib
import numpy as np
from fastapi import FastAPI
from fastapi import UploadFile, File, Request
import cv2
from io import BytesIO
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Predicting Covid Class")

#app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
def load_clf():
    # Load classifier from pickle file
    global clf
    try:
    	clf = joblib.load("app/model.pkl")
    except:
        clf = joblib.load("model.pkl")


@app.get("/")
def home(request: Request):
    return 'Welcome to Covid classifier by Ahmed Raafat, Please visit localhost/docs for the fastapi UI'

    
@app.post("/predict")
async def predict(file: UploadFile = File(...) ):
    
    #img = cv2.imread(file.filename)
    img_bytes=file.file.read()
    nparr = np.fromstring(img_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image,(150,150))/255.0
    image = image.reshape(1,-1)
    pred = clf.predict(image)[0]
    
    if pred < 0.5:
    	out="Normal"
    	ss= round(((1-pred)*100),2)
    else:
    	out="Covid"
    	ss = round(pred*100,2)
    result={"Prediction": out, "Score" : str(ss)+'%'}
    
    return {"result": result}
    
    
    
