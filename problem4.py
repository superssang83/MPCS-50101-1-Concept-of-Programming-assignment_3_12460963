# Problem 4
# Sang Park

def process_file(filename): 
    """Read, sort and return a file""" 
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    
    stripped_lines = []
    
    for line in lines:
        stripped_line = line.strip()
        stripped_lines.append(stripped_line)

    sorted_items = sorted(stripped_lines)
    number_of_lines = len(sorted_items)
    
    # Return a tuple
    return filename, sorted_items, number_of_lines

filename, items, lines = process_file("common_words.txt")

print(f"Filename: {filename}")
print(f"Sorted Items: {items}")
print(f"Number of Lines: {lines}")
