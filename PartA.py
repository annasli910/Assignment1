import sys

def tokenize(text_file_path):
    # runtime complexity: O(n) where n is the number of characters in the file,
    # because we iterate through each character once
    tokens = []
    current_token = []

    with open(text_file_path, 'r', encoding='utf-8', errors='ignore') as f:
        # errors='ignore' handles non-English or weird characters w/o crashing
        while True:
            chunk = f.read(1024)
            # iterates by chunk
            if not chunk:
                break
            for char in chunk:
                if char.isalnum():
                    current_token.append(char.lower())
                else:
                    if current_token:
                        tokens.append("".join(current_token))
                        current_token = []
        if current_token: # catches trailing token at end of file
            tokens.append("".join(current_token))
    return tokens

def computeWordFrequencies(tokens):
    # runtime complexity: O(n) where n is the number of tokens
    # looking in dictionary is constant time O(1)
    freq_map = {}
    for token in tokens:
        if token in freq_map:
            freq_map[token] += 1
        else:
            freq_map[token] = 1
    return freq_map

def print_frequencies(freq_map):
    # runtime complexity: O(K log K) where K is the number of unique tokens
    # because sorting takes O(K log K) time and printing takes another O(K)
    sorted_items = sorted(freq_map.items(), key=lambda item: (-item[1], item[0]))

    for token, freq in sorted_items:
        print(f"{token}\t{freq}")

def main():
    # part a takes one file and tokenizes, computes word frequencies, sorts and prints
    if len(sys.argv) < 2:\
        # checks to see if user entered a text file -> if not, exit
        print("Usage: python PartA.py <text_file>")
        sys.exit(1)
        
    file_path = sys.argv[1] # stores the second argument which should be text_file
    tokens = tokenize(file_path) 
    freq_map = computeWordFrequencies(tokens)
    print_frequencies(freq_map)

if __name__ == "__main__":
    main()