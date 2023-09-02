import sys

def lookup2(word):
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

def writing(word):
    x=0
    file2=open('history.txt','a+')
    for line in file2:
        print(f"line {line}")
        if x==0:#len(line)-1==len(word): #and line[len(line)-1]==word:
            x=1
            break
    if x==0:
         file2.write(word+'\n')
    file2.close

def main():
    argv = sys.argv
    # print(argv)
    word = argv[1] if len(argv) >= 2 else "thinker"
    definition = lookup2(word)
    definition = definition.replace('\\n', '\n')
    print(f"The definition of '{word}':\n{definition}")
    writing(word)

main()