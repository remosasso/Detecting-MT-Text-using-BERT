# Detecting-Machine-Translated-Text-using-BERT
A BERT-based approach to the binary classification task of human vs. machine translated subtitles.

In order to train a BERT model the following steps need to be taken:
- 1. Download a BERT model that you want to use from https://github.com/google-research/bert and extract it into the /bert-code/model/ folder. Currently there is a BERT-tiny model present in that directory: remove it or create a new model directory to use another model.

- 2. Download one of the datasets from the following drive: https://drive.google.com/drive/folders/1FOczjt165RcDc74vIpOq9QiwbgJSkAyQ, then the train and test files into the /bert-code/data/ folder.

- 3. (OPTIONAL) If you would like to generate a dataset yourself follow these steps:
  - 1.  Obtain human parallel translated (subtitle) data. 
  - 2. Take the source language and divide it into chunks using the create_chunks.py script in /data-creation/. (This speeds up translating a lot using e.g. Google Translate and avoids any size limitation problems).
  - 3. Translate the source chunks with some machine translator.
  - 4. Use create_dataset.py to merge the translated chunks as well as to merge it with the human translated data in   
merge chunks and add corresponding labels.
  - 5. Now a dataset is obtained which should be split into a training and testing set as desired and the eventual files should be .tsv files.
  
 - 4. 
