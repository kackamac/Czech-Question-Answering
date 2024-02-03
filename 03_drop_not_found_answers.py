# select only answers where the match between answer and text after lemmatization and regardless of the word order is the same store result to outputfile 
import argparse
import json
import sys

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=str, help="Input file name")
parser.add_argument("output_file", type=str, help="Output file name")
parser.add_argument("--negate", default=False, action="store_true", help="Negate the test for dropping")
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
       
    # delete answers and questions with match < threshold
    for i in range(0, len(data['data'])):
        for j in range(0, len(data['data'][i]['paragraphs'])):
            for k in range(0,len(data['data'][i]['paragraphs'][j]['qas'])):
                l = 0 
                lenght_answers = len(data['data'][i]['paragraphs'][j]['qas'][k]['answers'])
                while l < lenght_answers:
                    drop = data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['answer_start'] < 0
                    if args.negate:
                        drop = not drop
                    if drop:
                        del data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]  #remove data
                        lenght_answers-=1
                    else:
                        l+=1
        
        
    for i in range(0, len(data['data'])):
         for j in range(0, len(data['data'][i]['paragraphs'])):
             k = 0
             length = len(data['data'][i]['paragraphs'][j]['qas'])
             while k<length:
                 if len(data['data'][i]['paragraphs'][j]['qas'][k]['answers'])==0 and data['data'][i]['paragraphs'][j]['qas'][k]['is_impossible'] == args.negate:
                     del data['data'][i]['paragraphs'][j]['qas'][k]
                     length -= 1
                 else:
                     k+=1
               
    # delete paragraphs that don't have any qas tasks
    for i in range(0, len(data['data'])):
        j = 0
        length= len(data['data'][i]['paragraphs'])
        while j<length: 
           if len(data['data'][i]['paragraphs'][j]['qas'])==0:
               del data['data'][i]['paragraphs'][j]
               length -=1
           else:
               j+=1

    # delete titles that don't have any paragraphs 
    length = len(data['data'])
    i = 0                                
    while i<length:        
        if len(data['data'][i])==0:           
            del data['data'][i]
            length -=1
        else:
            i+=1 
            
    print('--DATA SELECTED--')
        
    save_file(data, args.output_file)
    
if __name__ == "__main__":
    main()
    
