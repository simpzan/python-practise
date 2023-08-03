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

def lookup(word):
    s='0'
    z=open('dict.txt')
    for a in z:
        a=a.strip()
        if a.startswith('[' + word + ' |'):
            s=a
            break
    if s=='0':
        return "aabb"
    else:
         q=2
         for w in s:
             if w=="|":
                 break
             else: q+=1
         return s[q:-1]

def main():
    argv = sys.argv
    # print(argv)
    word = argv[1] if len(argv) >= 2 else "thinker"
    definition = lookup2(word)
    definition = definition.replace('\\n', '\n')
    print(f"The definition of '{word}':\n{definition}")

main()