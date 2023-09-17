import sys
import json

def dictmake():
    a=dict()
    file=open('dictionary/dict.txt','r')
    for line in file:
        z=line.find('|')
        a[line[1:z-1]]=line[z+4:-2]
    file.close()
    return a

def writing(word):
    with open('history.json','r') as file:
        data=json.load(file)
    if word not in data['history']:
        data['history']+=[word]
        with open('history.json','w') as file:
            json.dump(data,file,indent=4)
            

def main():
    argv = sys.argv
    # print(argv)
    a=dictmake()
    for i in range(len(argv)-1):
        word=argv[1+i]
        if word in a:
           definition=a[word]
           print(f"The definition of '{word}':\n{definition}\n")
           writing(word)
   

main()