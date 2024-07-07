import random
 
def randomize_capitalization(line):
    return ''.join(random.choice([char.upper(), char.lower()]) for char in line)
 
def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            randomized_line = randomize_capitalization(line.strip())
            outfile.write(randomized_line + '\n')
 
# Example usage
input_file = '/Users/Root/Pentest-Lists/wordlist.txt'  # Replace with your input file name
output_file = '/Users/Root/Pentest-Lists/wordlist-random.txt'  # Replace with your output file name
process_file(input_file, output_file)
