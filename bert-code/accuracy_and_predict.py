import pandas as pd
from sklearn.metrics import accuracy_score
import tensorflow as tf
import os
import csv

flags = tf.flags
FLAGS = flags.FLAGS

flags.DEFINE_string(
    "output_dir", './output/',
    "The output directory where the model checkpoints will be written.")
flags.DEFINE_string(
    "data_dir", "./data/",
    "The input data dir. Should contain the .tsv files (or other data files) "
    "for the task.")


os.system('python run_classifier.py --task_name=cola --do_predict=true --data_dir=./data/ --vocab_file=./model/vocab.txt --bert_config_file=./model/bert_config.json --init_checkpoint=./output/model.ckpt --max_seq_length=256 --output_dir=./output/ --convert_data=True')

df_result = pd.read_csv(FLAGS.output_dir + 'test_results.tsv', sep='\t', header=None, engine='python',quoting=csv.QUOTE_NONE)
test = pd.read_csv(FLAGS.data_dir + 'test.tsv', sep='\t', usecols=[1], header=0, engine='python',quoting=csv.QUOTE_NONE)



labels = test.astype('int32')
labels = labels.values.tolist()

print("Found "+str(len(labels))+" labels")
print("Found "+str(len(df_result))+" predictions")

assert len(labels) == len(df_result)


print("Converting predictions to class labels...")
binary_results = []
for line in df_result.iterrows():
    human = line[1][0]
    machine = line[1][1]
    result = 0 if human > machine else 1
    binary_results.append(result)

print("Computing accuracy...")
accuracy = accuracy_score(binary_results, labels)
print("Accuracy: " + str(accuracy))

