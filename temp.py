# #
# # File: temp.py
# # Auth: Martin Burolla
# # Date: 10/27/2021
# # Desc: A temporary place to write python code.
# #

import random
from datetime import date



# def main():

#     people_list = [
#         {"firstname": "joe", "lastname": "smith", "age": 30},
#         {"firstname": "peter", "lastname": "jones", "age": 66},
#         {"firstname": "mary", "lastname": "jane", "age": 22},
#         {"firstname": "sue", "lastname": "anderson", "age": 11},
#     ]

#     my_dict = {
#         1: 'one',
#         2: 'two',
#         3: 'three '
#     }

#     #print(people_list)
#     people_list.sort(key=lambda p: p['age'])
#     #print(people_list)

#     l = list(map(lambda p: {'age': p['age']}, people_list))
#     print(l)

#     foo()


# def foo():
#     my_list = []
#     for _ in range(0, 10):
#         my_list.append(random.randint(1, 100))
#     print(my_list)
#     # total = sum(my_list)
#     # print(f'The sum is: {total}')


# if __name__ == "__main__":
#     main()

def ex1():
    sum = 0
    for i in range(0,10):
        num = random.randint(0,100)
        sum += num
    print("The sum is: ", sum)
    
def ex2():
    width = input("Enter width: ")
    height = input("Enter height: ")
    length = input("Enter length: ")
    
    box = float(width) * float(height) * float(length)
    
    print("The volume is: " , round(float(box),3))

def ex3():
    list = input("Enter list of numbers: ").split(",")
    if(list[0] == list[-1]):
        return True
    return False

def ex4():
    list = "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado.".split(' ')
    print(list.count("Python"))

def ex5():
    myList =[1,2,3]
    mySet = {3,4,5}
    myNewList = set(myList).union(mySet)
    print(myNewList)

def ex6():
    mylist = [11, 100, 101, 999, 1001]
    mylist = list(reversed(mylist))
    print(mylist)
    

def ex7():
    num = random.randint(0,100)
    if num <= 10:
        print(num,"You lose.")
    if num > 10 & num < 50:
        print(num, "Try again.")
    if num >= 50:
        print(num, "You win!")

def ex8():
    myList = [6,2,7,3,77,7,1]
    smallest = myList[0]
    for i in myList:
        if i<smallest:
            smallest = i
    print(smallest)
    
def ex9():
    str = input("Enter a string: ")
    if(str.isupper()):
       return True
    return False

def ex10():
    str = input("Enter a string: ")
    vowels = ["a","e","i","o","u"]
    v = 0
    c = 0
    str = str.lower()
    for s in str:
        if s in vowels:
            v = v+1
        else:
            c = c+1
    print("Vowels: ", v, "\n","Consonants: ", c)


def ex11():
    today = date.today()
    d = today.strftime("%m/%d/%y")
    with open('output.txt', 'w') as f:
        f.write(f"Today's date is: {d}.")


def ex12():
    num = int(input("Enter integer: "))
    print(-1*num)


def ex13():
    first = ""
    second = ""
    while(True):
        first = input("Enter first integer: ")
        second = input("Enter second integer: ")
        if(first == "exit" or second == "exit"):
            break
        print("Answer: ",int(first) + int(second))


def main():
    ex13()

if __name__ == "__main__":
    main()

