# Cat, Dog, & Hare Image Classifier

## Overview

This project implements an image classification model using PyTorch to distinguish between images of cats, dogs, and hares

## Data Source

* **`PetImages` Dataset:** Download link: `https://drive.google.com/uc?export=download&id=1DZDKtef0Fo5khSGRSearf39PXweoamBv`
    * `Cat/`: Containing images of cats.
    * `Dog/`: Containing images of dogs.
    * `Hare/`: Containing images of hares.
 

## Model
    
* **Model Definition (`CatDogCNN`):**
    * **Convolutional Layer 1:** 3 input channels, 32 output channels, 3x3 kernel, padding 1, ReLU activation.
    * **Max Pooling Layer 1:** 2x2 kernel, stride 2.
    * **Convolutional Layer 2:** 32 input channels, 64 output channels, 3x3 kernel, padding 1, ReLU activation.
    * **Max Pooling Layer 2:** 2x2 kernel, stride 2.
    * **Convolutional Layer 3:** 64 input channels, 128 output channels, 3x3 kernel, padding 1, ReLU activation.
    * **Max Pooling Layer 3:** 2x2 kernel, stride 2.
    * **Flatten Layer.**
    * **Fully Connected Layer 1 (fc1):** 128 \* 28 \* 28 input features, 128 output features, ReLU activation.
    * **Dropout Layer:** Dropout probability 0.5.
    * **Fully Connected Layer 2 (fc2):** 128 input features, 3 output features (for Cat, Dog, Hare classes).
