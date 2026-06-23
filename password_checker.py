
user_input = input("Enter Your Password: ")
score = 0
has_lowercase = False
has_uppercase = False
number = False
special = False

if len(user_input) >= 8:
   score = score + 1

for char in user_input:
    if char.islower():
        has_lowercase = True


if has_lowercase :
     score = score + 1


for char in user_input:
    if char.isupper():
        has_uppercase = True

if has_uppercase:
     score = score + 1


for char in user_input:
    if char.isnumeric():
        number = True

if number is True:
    score = score + 1


for char in user_input:
    if not char.isalnum():
        special = True

if special is True:
    score = score + 1

if score<= 2:
    print("Your password is too weak!")
elif score<=4:
    print("you can do better")
elif score == 5 :
    print("you have got the perfect password")
print("Score:", score, "/5")












