# show difference between answers in two files
import argparse
import json
import sys

parser = argparse.ArgumentParser()
parser.add_argument("input_file_a", type=str, help="Input file name a")
parser.add_argument("input_file_b", type=str, help="Input file name b")
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

    data = load_file(args.input_file_a)
    data_b = load_file(args.input_file_b)
       
    shown = set()
    for i in range(0, len(data['data'])):
        for j in range(0, len(data['data'][i]['paragraphs'])):
            for k in range(0,len(data['data'][i]['paragraphs'][j]['qas'])):
                for l in range(len(data['data'][i]['paragraphs'][j]['qas'][k]['answers'])):
                    drop_a = data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['answer_start'] < 0
                    drop_b = data_b['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['answer_start'] < 0
                    if drop_a != drop_b:
                        print("Found difference. Drop in {} is {}, drop in {} is {}".format(args.input_file_a, drop_a, args.input_file_b, drop_b))
                        if (i, j) not in shown:
                            print("Context:", data['data'][i]['paragraphs'][j]['context'])
                            shown.add((i, j))
                        print("Question", data['data'][i]['paragraphs'][j]['qas'][k]['question'])
                        print("Answer a", data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text'])
                        print("Answer b", data_b['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text'])
                        print()
    
if __name__ == "__main__":
    main()
    
