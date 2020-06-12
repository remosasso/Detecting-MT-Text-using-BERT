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
  - 6. In order to visualize the data you created you can use the jupyter notebook "plotting_script.ipynb" in the main folder of this repo.
  
 - 4. Now having TensorFlow installed you can train the bert model by using the following command:       
 ``` python run_classifier.py --task_name=cola --do_train=true --data_dir=./data/ --vocab_file=./model/vocab.txt --bert_config_file=./model/bert_config.json --init_checkpoint=./model/model.ckpt --max_seq_length=256 --train_batch_size=8 --learning_rate=2e-5 --num_train_epochs=1.0 --output_dir=./output/ --do_lower_case=False --convert_data=True --save_checkpoints_steps=10000 --training_steps=1000000 --max_models_save=5000 --converted_data_folder=None```
      
      Note that the input data first needs to be converted to features, which can be controlled by the "convert_data" parameter. Once the data is converted once, you don't need to convert it again. "save_checkpoints_steps" denotes after how many steps a checkpoint will be saved, "training_steps" denotes the total number of steps you want to model to train (usually equal to the size of your dataset), "max_models_save" denotes after how many saved models it will start overwriting previous models to save storage space, and finally if you have already converted the data you can specify its location with "converted_data_folder". These parameters were added by us, all other parameters belong to the original BERT code and speak for themselves.

- 5. At this point the pre-trained BERT model you chose will start training after it converted the data. That is, the model is finetuned using an additional layer of 2 neurons as an output layer. You can now start predicting your test set using the following command:
 ``` python accuracy_and_predict.py --data_dir=./data/ --output_dir=./output/  ``` Where the data and output directories should be the same as before, but if not you can specify them otherwise with these parameters. This will run a prediction process of the model which will, again, first convert the testing data, then make all predictions based on your test set and eventually compute the accuracy score.
 
 - 6. That's it. We have done this procedure for four different datasets (as present in the google drive) and for four different BERT models from the BERT repo (tiny, small, medium and base).
 
 Final note: when training the BERT model you may notice that after a certain amount of training steps there is no, or barely any difference in performance anymore. At this point your model has converged and is unlikely to improve any further. A possible solution, which hasn't been tried by us, is to add a dropout layer before the the output layer. 


