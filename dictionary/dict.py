import sys

def lookup(word):
    return f"the fake definition of {word}"

def main():
    argv = sys.argv
    # print(argv)
    word = argv[1] if len(argv) >= 2 else "thinker"
    definition = lookup(word)
    print(f"The definition of '{word}':\n{definition}")

main()