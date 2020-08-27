import random


boys = ["Liam", "Jackson", "Hugh", "Mason", "Luke", "Jermaine", "Derrick", "Richmond", "Craig", "Nick"]
girls = ["Tabitha", "Dorothy", "Matilda", "Pauline", "Christiana", "Dorcas", "Junia", "Pheobe", "Sophia", "Johanna"]
chosen_boy = random.choice(boys).lower()
chosen_girl = random.choice(girls).lower()
tinder_match = (chosen_boy + "loves" + chosen_girl)
print (tinder_match)
tinder_alogrithm = {}
love_code = ""

for letter in tinder_match:
    if letter not in tinder_alogrithm:
        tinder_alogrithm[letter] = 1
    else:
        tinder_alogrithm[letter] += 1
print (tinder_alogrithm)

for letter in tinder_match:
    if letter in tinder_alogrithm:
        num = str(tinder_alogrithm[letter])
        love_code += num
print (love_code)

def love_evaluator(num):
    length = len(num)
    if length is 1:
        return int(num[0])
    
    elif length is 2:
        return str(int(num[0]) + int(num[-1]))

    else:
        add = int(num[0]) + int(num[-1])
        new_num = num[1:-1]
        other = love_evaluator(new_num)
        return str(add) + str(other)

calculate = love_evaluator(love_code)

def love_calculator(num):
    length = len(num)

    if length is 2:
        return num
    
    else:
        num = love_evaluator(num)
        return love_calculator(num)

calculate = love_calculator(love_code) + "%"
print (f"The love percentage is {calculate}")

    

    
