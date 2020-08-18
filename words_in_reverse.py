ten_word_string = "This is the first code that we are gonna write"
string_length = len(ten_word_string)
sliced_string = ten_word_string[string_length::-1]
print (sliced_string)
words_split = sliced_string.split(" ")
words_split = words_split[-1::-1]
answer = ' '.join(words_split)
print(answer)
