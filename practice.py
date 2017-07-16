# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 11:38:10 2017

@author: ammara
"""

#http://www.practicepython.org/

# Following problems are taken from link above


############################################################################################
#Excercise #1
#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
#############################################################################################

#solution 1: as statemnet 
k=input ("Please Enter you name: ")
p=int(input("Please Enter you date of birth: "))
print(k, ",you will be 100 years old in ", p+100)



#solution 2: as function
def func_age():
    k=input("please enter your name ")
    p=int(input("please enter your year of birth "))
    print(k, ",you will be 100 years old in ", p+100)

func_age()


#Add on to the previous program by asking the user for another number 
#and printing out that many copies of the previous message. 


#solution 3: Better solution
from datetime import date
import math
k=input ("Please Enter you name: ")
p=int(input("How old are you: "))
year=date.today().year
date_born=year-age # it will give the date i was born
year_100=date_born+100
s=(k+ ', you will be 100 years old in ' + str(year_100) + '\n')
num=int(input("Please Enter how many times you want to print results: "))
print(s*num)







#notes:
#date.today()  #willl give complete date today
#date.today().year # will inly give year
# when using + to separate int from string in print statment, then no need to use commas
# to separate them. just use + sign
###############################################################################





###############################################################################
#Exercise 2 
#Ask the user for a number. Depending on whether the number is even or odd,
#print out an appropriate message to the user.


num=int(input("Please enter a number:"))
if (num%2!=0):
    print(num, "is an odd number")
else:
    print(num, "is an even number")


#extras

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) 
#and one number to divide by (check). If check divides evenly into num, 
#tell that to the user. If not, print a different appropriate message.


num=int(input("Please enter a number:"))
check=int(input("Please enter a number to divide by:"))

if (num%2!=0):
    print(num, "is an odd number")
elif(num%4==0):
    print(num, "is a multiple of 4")
else:
    print(num, "is an even number")
if (num%check!=0):
    print(num, "does not divided evenly by" , check)
else:
    print(num, " divided evenly by" , check)

#notes
# integer and string should be separated by comma, they can not be separated by +
#zero is an even number 

#elif should be indented the same way, if is indented 


#################################################################################
#Exercise 3 
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.
#Instead of printing the elements one by one,
#make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Ask the user for a number and return a list that contains only 
#elements from the original list a that are smaller than that number given by the user.


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
t=int(input("please input a number:"))


#following program will give you list of numbers in which numbers are smaller than 
# the given number
# you can modify it if you only need numbers less than 5


list_5=[]       
for x in a:
    if (x<5):
        if (x<t):
            list_5.append(x)
print(list_5)

    
       

#notes:
# after if make sure to put bracket
#dontss put argumnet in bracket when using for 
#append function applies to list 
#pay attention to indexing of print 
###################################################################################
#Exercise 4 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#Take two lists and write a program that returns a list that contains only the elements that are
#common between the lists (without duplicates). Make sure your program works on two lists of different sizes.


uniq=[]
for x in a:
    for y in b:
        if x==y:
            uniq.append(x)
print(set(uniq)) # print line has to be out of the loop, so that list is not repeated.


 
   
# test this function on randomly generated two lists and try to write this program in one line
import random
print(list(set([element for element in random.sample(range(1,500),100)  if element in random.sample(range(1,500),100)])))   
     
#####################################################################################     

#Exercise 5

#Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)


        
        
pal=str(input("Please enter a palindrome: "))
if (pal[::]==pal[::-1]):
    print("you entered a palindrome")
else:
    print("The word, you eneterd is not palindrome")
    
################################################################################################################################



















