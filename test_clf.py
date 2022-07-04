import joblib
import lightgbm
import cv2

def preprocess(im):
	im = cv2.resize(im,(150,150))/255.0
	im = im.reshape(1,-1)
	return im
	
im_path = 'test_images/cov.jpg'

im = cv2.imread(im_path,0)
im = preprocess(im)

def test_mdl_sanity():

    assert joblib.load('model.pkl')
                       
                   
def test_mdl_prediction():
    clf = joblib.load('model.pkl')
    assert clf.predict(im)
