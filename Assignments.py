import random
import datetime
import hashlib

def main():
    #Random()
    #boxVolume()
   #print(firstAndLast())
    #wordCount()
   #biggerSet()
    #reverseMe()
    #winnerWinner()
    #shortieStraw()
    #print(upperOrLower())
    #vAndCs()
    #dateTime()
    #neg2Pos_pos2Neg()
    #addOnlyCalc()
    foreverCalc()
    #foreverCalcLogger()
    #hashBrown()
    #authAuth()



def Random():
    randyList = []
    sum = 0
    
    for i in range(10):
        num = random.randint(0, 100)
        randyList.append(num)
        sum += num

    print(f"The list be: {randyList}")
    print(f"The sum is: {sum}" )

def boxVolume():
    width = input("Enter width: ")
    height = input("Enter height: ")
    length = input("Enter length: ")

    volume = float(width) * float(height) * float(length)
    print(f"The value is: {volume}")


def firstAndLast():
    numList = []
    list = input("Enter list of numbers: ")
    numList = list.split(",")

    if numList[0] == numList[-1]:
        return True
    else:
        return False


def wordCount():
    txt = "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."
    stringList = txt.split(" ")
    sum = 0
    for x in stringList:
        if x == "Python":
            sum += 1
    print(sum)

def biggerSet():
    myList = [1,2,3]
    mySet = {3,4,5}

    for p in myList:
        mySet.add(p)

    print(mySet)

def reverseMe():
    numList = [11, 100, 101, 999, 1001]
    numList.sort(reverse=True)
    print(numList)


def winnerWinner():
    num = random.randint(1, 100)
    if num < 10:
        print(f"{num}: You lose.")
    elif num > 10 and num < 50:
        print(f"{num}: Try again.")
    else:
        print(f"{num}: You win!")

def shortieStraw():
    myList = [6,2,7,3,77,7,1]
    temp = myList[0]

    for x in myList:
        if x < temp:
            temp = x
    print(temp)

def upperOrLower():
    message = input("Enter a string: ")
    if message.isupper():
        return True
    else:
        return False


def vAndCs():
    word = input("Enter string pls: ")
    vowels = "aeiou"
    vowCow = 0
    constCownt = 0

    for x in word:
        if x in vowels:
           vowCow += 1
        else:
            constCownt += 1

    print(f"Vowel Count: {vowCow}")
    print(f"Consonant Count: {constCownt}")

def dateTime():
    x = str(datetime.datetime.now())
    output = open("output.txt", "w")
    output.write(f"The date is: {x}")
    output.close()


def neg2Pos_pos2Neg():
    num = float(input("Enter integer: "))

    if num.is_integer():
        x=int(num)
        print(x*-1)        
    else:
        print(f"ERROR: {num} is not an integer.")    

def addOnlyCalc():
    num1 = input("Enter first integer: ")
    if(num1 =="exit"):
        return
    num2 = input("Enter second integer: ")    
    x = int(num1)
    y = int(num2)
    z = x+y
    print(z)
    addOnlyCalc()


def foreverCalc():
    num1 = input("Enter first integer: ")
    if(num1 =="exit"):
        return
    num2 = input("Enter second integer: ") 
    operation = input("Enter operation (add, sub, mul, div): ")
    x = int(num1)
    y = int(num2)
    if operation == "add":
        z = x + y
        print(z)
    elif operation == "sub":
        z = x - y
        print(z)
    elif operation == "mul":
        z = x * y
        print(z)
    else:
        z = x / y
        print(z)
    foreverCalcLogger(x, y, operation, z)
    foreverCalc()
    j = str(num1) + operation + str(num2)
    return j


def foreverCalcLogger(x, y, op, z):
    #foreverCalc()
    d = str(datetime.datetime.now())
    output = open("output.txt", "a")
    output.write(f"{d}: {x} {op} {y} = {z}\n")
    output.close()

def hashBrown():
    data = {}
    username = "ally"

    print("Type exit at anytime to end")
    
    while username != "exit":
        username = input("Enter username: ")
        if username == "exit":
            break
        password = input("Enter pasword: ")
        password = hashlib.sha256(password.encode())
        data.update({username: password})
    for x, y in data.items():
        print(f"{x} : {y.hexdigest()}")

def authAuth():
    data = {}
    print("Type exit at anytime to end program...")
    
    while True:
        mode = input("Enter mode (add|login): ")
        if mode == "add":
            username = input("Enter username: ")
            password = input("Enter pasword: ")
            password = hashlib.sha256(password.encode())
            data.update({username: password})
        elif mode == "login":
            loginName = input("Enter username: ")
            loginPassword = input("Enter pasword: ")
            hashLoginPass = hashlib.sha256(loginPassword.encode())
            print(hashpass.hexdigest())
            print(data[loginName])
            if loginName in data:
                if (data[loginName].hexdigest()) == hashpass:
                    print("Password is Correct")
                else:
                    print("password incorrect")
            else:
                print("User does not exist foo.")
        else:
            break
    for x, y in data.items():
        print(f"{x} : {y.hexdigest()}")
            



if __name__ == '__main__':
    main()