#!/usr/bin/python

# Read user name
a=input("Enter name: ")

# read user age
b=input("Enter age: ")

#get marks for subject 1
m1=input("Enter marks for subject 1 ")

#get marks for subject 1
m2=input("Enter marks for subject 1 ")

#get marks for subject 1
m3=input("Enter marks for subject 1 ")

# convert to int
m4 = int(m1)
m5 = int(m2)
m6 = int(m3)

# Find total
c = m4 + m5 + m6

#find average
d = c / 3

#print the total and average
print("Your total marks",c)
print("Your average marks",d)
