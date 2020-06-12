from tqdm import tqdm
import random

#Creating dataset for Italian-English
#Load in all the english subs
english = open("OpenSubtitles.en-it.en", "r")
linesEnglish = english.readlines()


#Load in all the italian subs
italian = open("OpenSubtitles.en-it.it", "r")
linesItalian = italian.readlines()


#Get rid of some weird characters
linesEnglish = [ele.replace('-','') for ele in linesEnglish]
linesEnglish = [ele.replace('#','') for ele in linesEnglish]
linesEnglish = [ele.replace('~','') for ele in linesEnglish]
linesItalian = [ele.replace('-','') for ele in linesItalian]
linesItalian = [ele.replace('#','') for ele in linesItalian]
linesItalian = [ele.replace('~','') for ele in linesItalian]



#Start making the chunks. Here pick how many lines in chunk you want
start = 0
end = 200000
#Set the number of chunks you want
for chunk in range(200):

    chunkItalianSub = linesItalian[start:end]
    chunkEnglishSub = linesEnglish[start:end]

    ####shuffle the two datasets in the same order
    temp = list(zip(chunkEnglishSub, chunkItalianSub))
    random.seed(420)
    random.shuffle(temp)
    trialEnglishSub, trialItalianSub = zip(*temp)

    #For creating sentences of X and more subs. Future experimentation
    # chunksItalian = [cleanTrialItalianSub[x:x+6] for x in range(0, len(cleanTrialItalianSub), 6)]
    # chunksEnglish = [cleanTrialEnglishSub[x:x+6] for x in range(0, len(cleanTrialEnglishSub), 6)]


    chunkedEnglishFinal = ""
    chunkedItalianFinal = ""

    for i in range(len(trialItalianSub)):
        #Get the 4 sentences of Italian
        smallChunkItalian = trialItalianSub[i]
        smallChunkEnglish = trialEnglishSub[i]

        #tokenizedItalian = smallChunkItalian.split()
        #tokenizedEnglish = smallChunkEnglish.split()

        if len(tokenizedItalian) > 6 and len(tokenizedEnglish) > 6:
            #print("This is the italian sub:", smallChunkItalian, "with length", len(tokenizedItalian) ,"\n")
            #print("This is the english sub:", smallChunkEnglish, "with length", len(tokenizedEnglish) ,"\n")

            chunkedItalianFinal += smallChunkItalian
            chunkedEnglishFinal += smallChunkEnglish

            # For creating larger sentence chunks
            #Strip away the new lines
            # cleanQuadItalian = " "
            # cleanQuadEnglish = " "
            # for j in range(len(smallChunkItalian)):
            #     strippedLineItalian = smallChunkItalian[j].strip()
            #     strippedLineEnglish = smallChunkEnglish[j].strip()
            #     cleanQuadItalian = cleanQuadItalian + strippedLineItalian + " "
            #     cleanQuadEnglish = cleanQuadEnglish + strippedLineEnglish + " "
            
            # chunkedItalianFinal = chunkedItalianFinal + cleanQuadItalian + "\n"
            # chunkedEnglishFinal = chunkedEnglishFinal + cleanQuadEnglish + "\n"    

    with open('single_english_human_{0}.txt'.format(chunk), 'w') as f:
        f.write(chunkedEnglishFinal)

    with open('single_italian_original_{0}.txt'.format(chunk), 'w') as f:
        f.write(chunkedItalianFinal)

    start += 200000
    end += 200000



