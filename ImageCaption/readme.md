# Image Captioning Project

Full work was implemented in Google Colab(so the setup)

## Overview

This project implements an image captioning model using PyTorch. The goal is to automatically generate descriptive captions for a given image. Architecture: Encoder = CNN with an Attention mechanism for image feature extraction; decoder = LSTM to generate the textual captions.

This notebook was originally designed and is best suited for execution in a Google Colab environment due to its reliance on Google Drive for data storage and potential GPU usage for model training.

## Dataset

1.  **Images (`images.zip`):**
    * **Content:** A zip file containing JPG images.
      **Download Link:** `https://drive.google.com/uc?export=download&id=1Sto9tyja2MdHHi0KrIpfVBUj_p6DKrBu`
    * **Expected Colab Path:** `/content/drive/MyDrive/ImageCaption/images.zip`
    
2.  **Captions (`results.csv`):**
    * **Content:** A CSV file containing image file names and their corresponding captions. The notebook expects the columns to be separated by a pipe (`|`) character.
    * **Expected Colab Path:** `/content/drive/MyDrive/ImageCaption/results.csv`
