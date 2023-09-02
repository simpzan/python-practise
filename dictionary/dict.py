import sys

def lookup(word):
    file = open('dict.txt')
    prefix = f'[{word} || '
    result = None
    for line in file:
        if line.startswith(prefix):
            result = line
            break
    file.close()
    if result is None: return ''
    return result[len(prefix):-2]

def dictmake():
    a=dict()
    file=open('dict.txt','r')
    for line in file:
        z=line.find('|')
        a[line[1:z-1]]=line[z+4:-2]
    file.close()
    return a

def writing(word):
    a=None                            
    file=open('history.txt','r+')
    for line in file:        
         if line[:-1]==word:
             a=1            
             break         
    if a is None:          
       file.write(word+'\n')
    file.close()
   
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