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
    clf = joblib.load("app/model.pkl")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
async def home_predict(request: Request, file: UploadFile = File(...) ):
    
    #img = cv2.imread(file.filename)
    img_bytes=file.file.read()
    nparr = np.fromstring(img_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image,(150,150))/255.0
    image = image.reshape(1,-1)
    pred = clf.predict(image)[0]
    
    if pred < 0.5:
    	out="Congratulations you are Normal !"
    else:
    	out="Unfortunately you are infected by Covid"
    	
    result={"Prediction": out}
    return templates.TemplateResponse("index.html", {"request": request, 'result': result})
    
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
    else:
    	out="Covid"
    
    return {"Prediction": out}
