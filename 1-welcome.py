str="This is the first code that we are gonna write"
stringlength=len(str)
slicedString=str[stringlength::-1]
words_split=slicedString.split(" ")
print (words_split)
words_split=words_split[-1::-1]
answer=' '.join(words_split)
print(answer)