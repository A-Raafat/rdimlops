# rdimlops

This branch to explain the walkthrough of the training / test pipeline


## Requirements
- lightgbm
- openv-python-headless
- sklearn

## Functions used

- prep_data(list)

  1. This function takes a list of image paths, reads the image as grayscale, scales by 1/255.0 and resizes it to (150,150) then flattens it to 1x22500. 
  2. Creates the label depending on the folder containing the image ( which is the class )
  3. returns 2 lists, first list is the input images flattened ( No. images, 22500 ) and the second list is the labels ( No. images, 1)
