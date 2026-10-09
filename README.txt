PartA.py:
- tokenizes a single text file, computes word frequencies using a dictionary, and prints in descending order of frequnecy (and alphabetically for ties)
- tokenizer uses chunk-based iteration to handle large files without overwhelming RAM
- run using "python PartA.py <text_file_path>"

PartB.py:
- tokenizes two text files, transforms into sets to get rid of duplicates, and uses set intersection to find overlap in constant time (O(1)). uses PartA tokenizer
- run using "python PartB.py <text_file_1_path> <text_file_2_path>"