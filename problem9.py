# Problem 9
# Sang Park

common = open("common_words.txt", 'r')
speech = open("speech.txt", 'r', encoding='utf-8')

word_from_common = []
word_from_speech = []

for common_word in common:
    word_from_common.append(common_word.strip())

for speech_word in speech:
    cleaned_line = ''
    for character in speech_word:
        if character.isalnum() or character.isspace():
            cleaned_line += character.lower()
    words_in_line = cleaned_line.split()
    word_from_speech.extend(words_in_line)

speech.close()
common.close()

word_count = {}
for word in word_from_speech:
    if word and word not in word_from_common:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

count_list = []
for word, count in word_count.items():
    count_list.append((word, count))

for i in range(len(count_list)):
    for j in range(i + 1, len(count_list)):
        if count_list[i][1] < count_list[j][1]:
            count_list[i], count_list[j] = count_list[j], count_list[i]

output_file = open("top_words.txt", 'w')
for index in range(20): 
    output_file.write(f"{count_list[index][0]} - {count_list[index][1]}\n")
output_file.close()


