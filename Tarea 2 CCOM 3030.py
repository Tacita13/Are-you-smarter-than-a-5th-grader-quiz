
# Isamar López Rodríguez
# 19/10/15

# Bienvenida
print("Are you smarter than a 5th grader?_The Quiz \n")

# contador de contestaciones correctas iniciado a 0
correctCounter=0

# Quiz
answer= input("1. The Salem witch trials of 1692 ocurred in what present-day U.S. State? ").lower()

if answer == "massachusetts":
    print(answer,"is correct!")
    correctCounter+=1
else:
    print(answer,"is incorrect!")
print()

answer= input("2. Budapest is the capital of what European country? ").lower()

if answer == "hungary":
    print(answer,"is correct!")
    correctCounter+=1
else:
    print(answer,"is incorrect!")
print()

answer= input("3. In the sentence 'Questlove is a very good drummer' what part of speech is the word \"very\"? ").lower()

if answer == "adverb":
    print(answer,"is correct!")
    correctCounter+=1
else:
    print(answer,"is incorrect!")
print()

answer= input("4. In our Solar System, which planet is farthest from the Sun? ").lower()

if answer == "neptune":
    print(answer,"is correct!")
    correctCounter+=1
else:
    print(answer,"is incorrect!")
print()

answer= input("5. Other than Mars, what is the only planet in our Solar system whose name is only one syllable long? ").lower()

if answer == "earth":
    print(answer,"is correct!")
    correctCounter+=1
else:
    print(answer,"is incorrect!")
print()

answer= input("6. In the Sun's core, hydrogen atoms fuse together to form what other element? ").lower()

if answer == "helium":
    print(answer,"is correct!")
    correctCounter+=1
else:
    print(answer,"is incorrect!")
print()

answer= float(input("7. If Jacob stands on Spencer's shoulders, they are two and a half yards high, how many feet is that? "))

if answer == 7.5:
    print(answer,"is correct!")
    correctCounter+=1
else:
    print(answer,"is incorrect!")
print()

answer= input("8. What element is presented by the letter \"K\" on the periodic table? ").lower()

if answer == "potassium":
    print(answer,"is correct!")
    correctCounter+=1
else:
    print(answer,"is incorrect!")
print()

answer= int(input("9. How many planets in our Solar system have a circumference larger than Earth? "))

if answer == 4:
    print(answer,"is correct!")
    correctCounter+=1
else:
    print(answer,"is incorrect!")
print()

answer= input("10. Which of these prehistoric animals could fly? \n - Triceratops \n - Pterodactyl \n - Velociraptor \n").lower()

if answer == "pterodactyl":
    print(answer,"is correct!")
    correctCounter+=1
else:
    print(answer,"is incorrect!")
print()


# resultado final
result = int((correctCounter/10)*100)

# Si ganó o perdió.
if result >= 60:
    print ("Result: ", result,"%")
    print ("You are indeed smarter than a 5th grader!")
else:
    print ("Result: ", result,"%")
    print("You are not smarter than a 5th grader")
