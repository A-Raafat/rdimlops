# rdimlops

This branch to explain the walkthrough of the training / test pipeline


## Requirements
- lightgbm
- openv-python-headless
- sklearn

## Functions used

- **prep_data(list)**

  1. This function takes a list of image paths, reads the image as grayscale, scales by 1/255.0 and resizes it to (150,150) then flattens it to 1x22500. 
  2. Creates the label depending on the folder containing the image ( which is the class )
  3. returns 2 lists, first list is the input images flattened ( No. images, 22500 ) and the second list is the labels ( No. images, 1)


# Train / Test Pipeline

## Training steps

- Create Lightgbm datasets [ train / test ]
- Create the lightgbm classifier parameters
- Create the lightgbm classifier model object and pass the parameters and datasets
- Fit on the dataset using model.train
- Saving (dump) the model as pickle format using joblib

## Testing steps
- Read the image
- Do the same preprocessing (scaling and resizing and flattening)
- Load the dumped model using joblib
- Call model.predict

## Evaluation 
- The test (around 400 images) set gave us the following results

- Learning curve

![alt text](https://github.com/A-Raafat/rdimlops/blob/Train_Test/traininerror.png)

- Confusion matrix

![alt text](https://github.com/A-Raafat/rdimlops/blob/Train_Test/cm2.png)

- Precision recall and F1 score

|Metric| Score |
|:----:|:-----:|
|Precision|0.9833484026522001|
|Recall|0.984708815806872|
|F1_score|0.9840230128975973|
|Accuracy|0.9855371900826446|
