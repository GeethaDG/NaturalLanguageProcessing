"""
!!!! Attention Please !!!!
Please input the keyword python followed by Script Name followed by the dictionary(Kindly refer the format given in the example below
Example for running the script: python GeethaDG-lecture3-nltk-synsets.py "{\"politics\": \"the activities associated with the governance of a country or area, especially the debate between parties having power\", \"justice\": \"It is the fairness in the way that people are treated\",\"food\": \"any nutritious substance that people or animals eat or drink or that plants absorb in order to maintain life and growth\",\"patience\": \"the capacity to accept or tolerate delay, problems, or suffering without becoming annoyed or anxious.\"}"
If you do not want to test from command line please comment the code from 63-79 and uncomment from 87-104
"""

import nltk
from nltk.corpus import wordnet as wordnet
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import sys
import json
en_stops = set(stopwords.words('english'))


#To Get POS wordnet of words
def pos_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


#Comparing two lists
def count(list1,list2):
    count=0
    for k in range(len(input_list)):
        for l in range(len(syns_list)):
            if input_list[k] == syns_list[l]:
                count = count + 1
    return count


def text_processing(sentence):
    # Tokenising
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    all_words_tokenised = tokenizer.tokenize(sentence)

    #POS Tagging of words
    tag_test = nltk.pos_tag(all_words_tokenised)

    # Stop word Removal
    all_words_stop_words_removed = []
    for word in tag_test:
        if word[0] not in en_stops:
            all_words_stop_words_removed.append((word[0].lower(),word[1]))

    # Lemmatisation
    lemmalist = []
    lemmatizer = WordNetLemmatizer()
    for w in all_words_stop_words_removed:
        if pos_tagger(w[1])!=None:
            lemmalist.append(lemmatizer.lemmatize(w[0],pos_tagger(w[1])))
    return lemmalist

######## Command Line Type Script Starts ################
if len(sys.argv)>1 :
    input = json.loads(sys.argv[1])
    for i in input:
        if len(input[i])!=0:
            print('My definition of "{}":'.format(i))
            print(input[i] + '\n')
            input_list = text_processing(input[i])
            syns = wordnet.synsets(i)
            for j in range(len(syns)):
                print('Definition of ' +  str(syns[j]) + ':')
                print(syns[j].definition())
                syns_list = text_processing(syns[j].definition())
                print('Number of words matching: {} \n'.format(count(input_list,syns_list)))
        else:
            print('No User definition provided for {}, hence skipping comparison'.format(i))
else:
    print('Please input a dictionary for comparison')

######## Command Line Type Script ends ################



######## No Command Line Type Starts ################
"""
input = {"politics": "the activities associated with the governance of a country or area, especially the debate between parties having power",
    "justice": "It is the fairness in the way that people are treated",
    "food": "any nutritious substance that people or animals eat or drink or that plants absorb in order to maintain life and growth",
    "patience": "the capacity to accept or tolerate delay, problems, or suffering without becoming annoyed or anxious."
}
for i in input:
    if len(input[i])!=0:
        print('My definition of "{}":'.format(i))
        print(input[i] + '\n')
        input_list = text_processing(input[i])
        syns = wordnet.synsets(i)
        for j in range(len(syns)):
            print('Definition of ' +  str(syns[j]) + ':')
            print(syns[j].definition())
            syns_list = text_processing(syns[j].definition())
            print('Number of words matching: {} \n'.format(count(input_list,syns_list)))
    else:
        print('No User definition provided for {}, hence skipping comparison'.format(i))
"""
######## No Command Line Type ends ################
