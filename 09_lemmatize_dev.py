#Lemmatize *inputfile* with development dataset using MorphoDita and save the results to the *outputfile*.
#Lemmatize model can be extracted from http://hdl.handle.net/11234/1-1836
import argparse
import collections
import json
import sys
import requests
import xml.etree.ElementTree as ET

import lemmatizer

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=str, help="Input file name")
parser.add_argument("output_file", type=str, help="Output file name")
args = parser.parse_args()

#load input json file
def load_file(file):
    with open(file, "r", encoding='utf-8') as read_file:
        data = json.load(read_file) 
    print('--DATA SUCCESSFULLY LOADED--')
    return data

# save data to json file
def save_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f,ensure_ascii=False)
    print('--DATA SUCCESSFULLY SAVED--')    

def main():
    data = load_file(args.input_file)

    # iterate topic by topic
    for i in range(0, len(data['data'])):        
        # iterate and translate paragraph by paragraph
        for j in range(0, len(data['data'][i]['paragraphs'])):
            # iterate question by question
            for k in range(0, len(data['data'][i]['paragraphs'][j]['qas'])):               
                # iterate answer by answer
                for l in range(0, len(data['data'][i]['paragraphs'][j]['qas'][k]['answers'])):                 
                    answer = data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text']  
                    if not answer =='':
                        lemmalist = lemmatizer.lemmatize(answer)
                        answer_lemmas_dict = []
                        last_lemma_end = -1
                        for lemma in lemmalist:
                            if not last_lemma_end == -1:
                                lemma_start = lemma["start_index"]
                                #print(answer[last_lemma_end:lemma_start])
                                answer_lemmas_dict.append(answer[last_lemma_end:lemma_start])
                            answer_lemmas_dict.append(lemma["lemma"].lower())
                            last_lemma_end = lemma["end_index"]
                        end = len(answer)
                        answer_lemmas_dict.append(answer[last_lemma_end:end])
                        data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text'] = ''.join(answer_lemmas_dict)

    print('--LEMMATIZATION FINISHED--', file=sys.stderr) 
    save_file(data, args.output_file)

if __name__ == "__main__":
    main()
    

 
                
