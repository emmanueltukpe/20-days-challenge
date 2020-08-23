
text_file = open("my_file.txt", "r")
lines = text_file.readlines()
text_file.close()

other_text_file = open("my_other_file.txt", "r")
second_lines = other_text_file.readlines()
other_text_file.close()

lines = [x.strip() for x in lines]
second_lines = [x.strip() for x in second_lines]
new_word= []

for x,y in zip(lines, second_lines):
    thrid_lines = (f'{x} {y}"\n')
    new_word.append(thrid_lines)


third_text_file= open("output_text_file.txt","w+")
third_text_file.writelines(new_word)
third_text_file.close()
    
    

