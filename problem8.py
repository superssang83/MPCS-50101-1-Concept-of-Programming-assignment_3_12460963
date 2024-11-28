# Problem 8
# Sang Park

letters = """GTACGACGGAGTGTTATAAGATGGGAAATCGGATACCAGATGAAATTGTGGATCAGGTGCAAAAGTCGGC
AGATATCGTTGAAGTCATAGGTGATTATGTTCAATTAAAGAAGCAAGGCCGAAACTACTTTGGACTCTGT
CCTTTTCATGGAGAAAGCACACCTTCGTTTTCCGTATCGCCCGACAAACAGATTTTTCATTGCTTTGGCT
GCGGAGCGGGCGGCAATGTTTTCTCTTTTTTAAGGCAGATGGAAGGCTATTCTTTTGCCGAGTCGGTTTC
TCACCTTGCTGACAAATACCAAATTGATTTTCCAGATGATATAACAGTCCATTCCGGAGCCCGGCCAGAG
TCTTCTGGAGAACAAAAAATGGCTGAGGCACATGAGCTCCTGAAGAAATTTTACCATCATTTGTTAATAA
ATACAAAAGAAGGTCAAGAGGCACTGGATTATCTGCTTTCTAGGGGCTTTACGAAAGAGCTGATTAATGA
ATTTCAGATTGGCTATGCTCTTGATTCTTGGGACTTTATCACGAAATTCCTTGTAAAGAGGGGATTTAGT
GAGGCGCAAATGGAAAAAGCGGGTCTCCTGATCAGACGCGAAGACGGAAGCGGATATTTCGACCGCTTCA
GAAACCGTGTCATGTTTCCGATCCATGATCATCACGGGGCTGTTGTTGCTTTCTCAGGCAGGGCTCTTGG"""

count_A = 0
count_T = 0
count_C = 0
count_G = 0
total = len(letters)

for count in letters:
    if count == "A":
        count_A += 1
    elif count == "T":
        count_T += 1
    elif count == "C":
        count_C += 1
    elif count == "G":
        count_G += 1
        
letters.replace(" ", "")

# Calculate percentages and round to nearest integer
percent_A = round((count_A / total) * 100)
percent_T = round((count_T / total) * 100)
percent_C = round((count_C / total) * 100)
percent_G = round((count_G / total) * 100)

# Print results in the specified format
print(f"A: {percent_A}%")
print(f"T: {percent_T}%")
print(f"C: {percent_C}%")
print(f"G: {percent_G}%")

