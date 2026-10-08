def tokenize(text_file_path):
    """
    runtime complexity: O(n) where n is the number of characters in the file,
    because we iterate through each character once
    """
    tokens = []
    current_token = []

    with open(text_file_path, 'r', encoding='utf-8', errors='ignore') as f:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            for char in chunk:
                if char.isalnum():
                    current_token.append(char.lower())
                else:
                    if current_token:
                        tokens.append("".join(current_token))
                        current_token = []
        if current_token:
            tokens.append("".join(current_token))

    return tokens

def computeWordFrequencies(tokens):
    """
    runtime complexity: O(n) where n is the number of tokens,
    since dictionary insertions/lookups take O(1) average time
    """
    freq_map = {}
    for token in tokens:
        if token in freq_map:
            freq_map[token] += 1
        else:
            freq_map[token] = 1
    return freq_map

def print_frequencies(freq_map):
    """
    runtime complexity: O(nlogn) where n is the number of tokens
    """
    sorted_items = sorted(freq_map.items(), key=lambda item: (-item[1], item[0]))

    for token, freq in sorted_items:
        print(f"{token}\t{freq}")