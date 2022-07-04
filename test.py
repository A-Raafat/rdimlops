import cv2
import joblib

def preprocess(im):
	im = cv2.resize(im,(150,150))/255.0
	im = im.reshape(1,-1)
	return im
	
	
im_path = 'norm.jpg'

im = cv2.imread(im_path,0)

im = preprocess(im)

print(im.shape)
	
gbm_pickle = joblib.load('model.pkl')

print(gbm_pickle.predict(im))
