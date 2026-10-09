import sys
from PartA import tokenize

def main():
    # runtime complexity: O(n+m) where n and m are the sizes of text files
    if len(sys.argv) < 3: # if not enough args
        print("Usage: python PartB.py <file1> <file2>") # give correct way to enter
        sys.exit(1)

    file1_path = sys.argv[1]
    file2_path = sys.argv[2]

    # use sets to avoid duplication and for O(1) intersection
    tokens1 = set(tokenize(file1_path))
    tokens2 = set(tokenize(file2_path))

    common_tokens = tokens1.intersection(tokens2) # O(1) time since sets
    # print number of common words
    print(len(common_tokens))

if __name__ == "__main__":
    main()