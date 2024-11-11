
with open("input_dict.txt", 'r') as infile:
    original_dict = {}
    for line in infile:
        line.strip()
        key, value = line.split(':')
        original_dict[key.strip()] = value.strip()
        inverted_dict = {value : key for key, in original_dict.items()}
        with open('invered_dict.txt', 'w') as outfile:
            for key, value in inverted_dict.items():
                outfile:
 

inverted_dict = {value: key for key, value in dictionary.items()}

with open('inverted_dict.txt', 'w') as file:
    for key, value in inverted_dict.items():
        file.write(f'{key}: {value}\n')

print("Dictionary inverted and saved to 'inverted_dict.txt'")