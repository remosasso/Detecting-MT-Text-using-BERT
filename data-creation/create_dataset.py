import glob
import re
import random
from sklearn.model_selection import train_test_split


####Get first all the original english with 0's behind. Change path to fit the data
path = "/Users/borismarinov/Desktop/University/Masters/2B/Language Project/Project/en-it.txt/run5/english_original/"

all_files_english_original = glob.glob(path + "/*")

#Order the files by last chunk number
all_files_english_original.sort(key=lambda f: int(re.sub('\D', '', f)))

all_data_english_original = ""

#Load all files in
for filename in all_files_english_original:
    chunk = open(filename, "r")
    linesEnglish = chunk.readlines()
    print(filename)
    temp = ""
    for line in linesEnglish:
        line = line.strip()
        temp = temp + line + "\t" + "0" + "\n"
    all_data_english_original += temp


with open('english_original_data.txt', 'w') as f:
        f.write(all_data_english_original)



#Do the same now for the english translated files with 1s behind
path = "/Users/borismarinov/Desktop/University/Masters/2B/Language Project/Project/en-it.txt/run5/english_translated/"

all_files_english_translated = glob.glob(path + "/*")

all_files_english_translated.sort(key=lambda f: int(re.sub('\D', '', f)))

all_data_english_translated = ""

#Load all files in
for filename in all_files_english_translated:
    chunk = open(filename, "r")
    linesEnglishTranslated = chunk.readlines()
    print(filename)
    temp = ""
    for line in linesEnglishTranslated:
        line = line.strip()
        temp = temp + line + "\t" + "1" + "\n"
    all_data_english_translated += temp


with open('english_translated_data.txt', 'w') as f:
        f.write(all_data_english_translated)


####### MERGE THE TWO WITH ALTERNATING SENTENCES
englishOriginal = open("english_original_data.txt", "r")
linesOriginal = englishOriginal.readlines()

#Load in all the italian subs
englishTranslated = open("english_translated_data.txt", "r")
linesTranslated = englishTranslated.readlines()



####shuffle the two datasets in the same order
temp = list(zip(linesOriginal, linesTranslated))
random.seed(420)
random.shuffle(temp)
linesOriginal, linesTranslated = zip(*temp)


#Get rid of -
#Get rid of the weird space encoding
linesTranslated = [ele.replace('\xa0',' ') for ele in linesTranslated] 


#Create the final data with the alternating order of the sentences
finalData = ""

for index in range(len(linesOriginal)):
    print(index)
    lineOriginal = linesOriginal[index]
    finalData = finalData + lineOriginal
    lineTranslated = linesTranslated[index]
    finalData = finalData + lineTranslated

with open('final_data.txt', 'w') as f:
        f.write(finalData)

#Open again so you can split into the train/test
finalData = open("final_data.txt", "r")
linesFinal = finalData.readlines()

#Ugly, change so its always 80% but for now whatever
train = linesFinal[0:int(len(linesFinal)*0.8)]

trainString = "".join(train)
with open('train.tsv', 'w') as f:
        f.write(trainString)


test = linesFinal[int(len(linesFinal)*0.8):-1]
testString = "".join(test)
with open('test.tsv', 'w') as f:
        f.write(testString)