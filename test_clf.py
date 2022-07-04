import joblib
import lightgbm

def preprocess(im):
	im = cv2.resize(im,(150,150))/255.0
	im = im.reshape(1,-1)
	return im
	
im_path = 'test_images/norm.jpg'

im = cv2.imread(im_path,0)
im = preprocess(im)

def test_mdl_sanity():

    assert joblib.load('model.pkl')
                       
                   
def test_mdl_prediction():
    clf = joblib.load('model.pkl')
    assert clf.predict(im)
