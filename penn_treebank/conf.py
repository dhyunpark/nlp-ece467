#NLP Project 2: HMM POS Tagger Confusion Matrix generation by Donghyun Park & Junbum Kim
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd

def confuse(documents):
    tags = []
    file = open(documents, 'r')
    for document in file:
        if documents == "test.list":
            doc = open("test_set/" + document.strip(), 'r')
        else:
            doc = open("test_label/" + document.strip(), 'r')
        for line in doc:
            line = line.strip()
            tokens = line.split(" ")
            for token in tokens:
                tag = token.split("/")
                if len(tag) > 1:
                    posTag = tag[1]
                    tags.append(posTag)
    return tags

def main():
    '''
    print("Enter Predicted Labels File: ", end="")
    predicts = input()
    predictfiles = open("test.list", 'r')
    predictFile = open(predicts, 'r')

    print("Enter True Labels File: ", end="")
    truths = input()
    truthfiles = open("test.labels", 'r')
    truthFile = open(truths, 'r')
    '''
    output = open("outputFile", "w")
    

    predictTags = []
    trueTags = []

    predictTags = confuse("test.list")
    trueTags = confuse("test.labels")

    sum = 0.0
    diag = 0.0
    conf = confusion_matrix(trueTags, predictTags)
    
    i = 0
    for row in conf:
        j = 0
        output.write("\t")
        for col in row:
            sum += col
            if i == j:
                diag += col
            j += 1
            output.write(str(col)+ "\t")
        i+=1
        output.write("\n")

    output.write("accuracy = " + str(diag/sum) + "\n")
    output.write("count = " + str(sum) + "\n")
    
    #confPD = pd.DataFrame(conf)
    #confPD.to_excel("outputFile.xlsx", index=False)
    #output.write(np.array2string(confusion_matrix(trueTags, predictTags)))

if __name__ == "__main__":
    main()

'''
logical progression:
import two files, one true, one predict
parse each line
tokenize the line
take in the tags
do conf matrix
'''
