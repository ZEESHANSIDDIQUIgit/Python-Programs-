import random
computer = random.choice([-1, 0, 1]) 

youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")
youDict={"s" : 1, "w":-1,"g":0}
reverseDict={ 1 : "Snake", -1:"water", 0:"Gun"}
you=youDict[youstr]

print(f"You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}")

if(computer == you):
    print("The match is Draw")

else:
    if(computer ==-1 and you==1):
        print("You Win!")

    elif(computer ==-1 and you==0):
        print("You Loose!")

    elif(computer ==1 and you==-1):
        print("You Loose!")

    elif(computer ==1 and you==0):
        print("You Win!")

    elif(computer ==0 and you==-1):
        print("You Win!")

    elif(computer ==-0 and you==1): 
        print("You Win!")

    else:
        print("Something went wrong !!!!")
