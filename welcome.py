from datetime import datetime


def age_check():
    age_str = input('How old are you?: ')
    try:
        y = int(age_str)
    except:
        print("Provide your age in numbers")
        return age_check()
    else:
        return y


first_name = input("Provide your first name: ")
last_name = input("Provide your last name: ")
age = age_check()

year = datetime.now().year
year_of_birth = year - age

print(f"Hello {first_name} {last_name}",
      f"you were born in the year {year_of_birth}")
