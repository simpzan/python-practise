import sys

def lookup(word):
    return f"the fake definition of {word}"

def main():
    argv = sys.argv
    # print(argv)
    if len(argv) < 2: return -1

    word = argv[1]
    definition = lookup(word)
    print(f"The definition of '{word}':\n{definition}")

main()