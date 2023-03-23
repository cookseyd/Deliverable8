# 20 March 2023
# Assignment 8
# Dustin Cooksey
# This project randomly populates a list with integer numbers
# and returns the summation of all of the elements of the list


import numpy as np


def Main():
    
    user = user_entry()
    
    print(user)
    
    list1 = random_list(user)
    summation = sum_random(list1)
    print(list1)
    print("The sum is: ")
    print(summation)
    

def random_list(size):
    list1 = []
    for i in range(size):
        list1.append(np.random.randint(10,50))
    return list1
    

def sum_random(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum

def user_entry():
    user = int(input("Enter an integer between 5 and 15: "))
    
    while user < 5 or user > 15:
        print("Input must be between 1 and 15!" )
        user = int(input("Enter an integer between 5 and 15: "))
    return user  
Main()