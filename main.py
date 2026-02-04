import random
'''
snake=1
water=-1
gun=0
'''
computer=random.choice([-1,1,0])
youstr=input("Enter your Choice (s/w/g):  ").lower()
youDict={"s":1 , "w":-1 , "g":0}
reverseDict={1: "Snake", -1: "Water", 0:"Gun"}
if youstr not in youDict:
    print("Invalid Choice, Please Try Again...")
    exit()
you=youDict[youstr]
print(f"You Chose {reverseDict[you]} /n Computer Chose {reverseDict[computer]}")
if computer==you:
    print("Draw, Try again...")
else:
    if(computer==-1 and you==1):
        print("You Win,  Congratulations !")
    elif(computer==-1 and you==0):
        print("You Lose,  Better Luck Next Time!!!")
    elif(computer==1 and you==-1):
        print("You Lose,  Better Luck Next Time!!!")
    elif(computer==1 and you==0):
        print("You Win,  Congratulations !")
    elif(computer==0 and you==-1):
        print("You Win,  Congratulations !")
    elif(computer==0 and you==1):
        print("You Lose, Better Luck Next Time!!!")
    else:
        print("Something Went Wrong")
