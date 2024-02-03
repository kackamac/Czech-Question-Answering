#Lemmatize *inputfile* with original texts and answers using MorphoDita and save the results to the *outputfile*.
#Lemmatize model can be extracted from http://hdl.handle.net/11234/1-1836
import argparseimport argparse
import collections
import json
import sys
import requests
import xml.etree.ElementTree as ET

import lemmatizer

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=str, help="Input file name")
parser.add_argument("input_english_file", type=str, help="Input English file name")
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
    data_english = load_file(args.input_english_file)
    
    # iterate topic by topic
    for i in range(0, len(data['data'])):        
        # iterate and translate paragraph by paragraph
        for j in range(0, len(data['data'][i]['paragraphs'])):
            text = data['data'][i]['paragraphs'][j]['context']
            text_lemmas = lemmatizer.lemmatize(text)
            text_english_length = len(data_english['data'][i]['paragraphs'][j]['context'])
            
            # iterate question by question
            for k in range(0, len(data['data'][i]['paragraphs'][j]['qas'])):
               
                # iterate answer by answer
                for l in range(0, len(data['data'][i]['paragraphs'][j]['qas'][k]['answers'])):                 
                    answer = data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text']  
                    answer_english_ratio = data_english['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['answer_start'] / text_english_length
                    answer_lemmas = lemmatizer.lemmatize(answer)

                    best_offset = None
                    for lemma_type in ["lemma", "form"]:
                        answer_lemmas_dict = collections.defaultdict(lambda: 0)
                        for lemma in answer_lemmas:
                            answer_lemmas_dict[lemma[lemma_type].lower()] += 1

                        for offset in range(max(len(text_lemmas) - len(answer_lemmas) + 1, 0)):
                            text_lemmas_dict = collections.defaultdict(lambda: 0)
                            for m in range(offset, offset + len(answer_lemmas)):
                                text_lemmas_dict[text_lemmas[m][lemma_type].lower()] += 1

                            if answer_lemmas_dict == text_lemmas_dict:
                                if best_offset is None or \
                                        abs(text_lemmas[offset]["start_index"] / len(text) - answer_english_ratio) < \
                                        abs(text_lemmas[best_offset]["start_index"] / len(text) - answer_english_ratio):
                                    best_offset = offset

                    if best_offset is not None:
                        data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text'] = \
                                data['data'][i]['paragraphs'][j]['context'][text_lemmas[best_offset]["start_index"]:text_lemmas[best_offset + len(answer_lemmas) - 1]["end_index"]]
                        data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['answer_start'] = text_lemmas[best_offset]["start_index"]
                    else:
                        data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['answer_start'] = -1
                    data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text_translated'] = answer
    print('--LEMMATIZATION FINISHED--') 
    save_file(data, args.output_file)

if __name__ == "__main__":
    main()
    
 
                
