'''
#!Eg:3
#? take values of length and breadth of a
#? from user and check if it is square or not

#length=int(input())
#breadth=int(input())
#if length==breadth:
#  print("it is a square")
#eals
#  print("its not square")

#! Eg4
# python program to check whether the
# give integer is a multiple of both 5and 7

n=int(input("enter the number:"))
if n%5==0 and n%7==0:
    print("yes")

#!Eg:5
#write a program to accept the cost price of a bike and display the
#road tax to be paid
#accordingto the following criteria:

#    cost price(in rs)
#    >100000
#    <100000


price =int(input("enter the price:"))
amount=0
if price>=100000:
     discount=price*(6/100)
     value=price-discount
     tax=value*(15/100)
     total=value+tax
else:
    tax=price*(5/100)
    total=price+tax
    print("the on road cost of bike is: ",total)

 #if clif
 #fg:1
#    a=7
 #   b=9
  #  c=3
#if a>b and a>c:
#   print("A is grater")
# elif c>a and c>b:
   # print("c is greater")
# A school has following ruls for grading system:
# a.below 25-F
# b.25 to 45-E
# C.45 to 50-D
# d.50 to 60-c


'''
#! - looping
# looping can be implimented using
# for loop
# while loop
#---> for loop I
# ?for loop is used for iteartion, if we know the number of times the loop have to run
# ? it is used to iterate the iterables eg (string,list,tuple,etc...)

# todo--->syntax in c
# for(1=0;1<10;i++){
#    printf("hello"):
# }

#! for syntax in python
# for userdefined_variable in range(start, end, step): default setp value is 1
# statement
# statement
# statement
#? Eg:1
# To print the value from 1 to 10 using for loop
#for i in range(0,10):
#     print(i)
#     print("hello")
# eg:2
#for val in range(1,50, 5):
 #   print(val)
#? eg:3
# to decrement the valueor 


#for val in range(10,0, -1):
#    print(val)
#for val in range(10,4,-2):
#     print(val)
#? Eg:4
# ! print the output of 7th multiplication table from 21 to 43
#for val in range(1,10+1):
#    print(val*7)
#for i in range (2,10+2):
#    print(i*8)
#for val in range(1, 10+1):
#    print(7,'x',val,'=',val*7)
#? eg5
# break-->used to teerminate the loop

#for val in range(1,10):
#    if val==6:
#        break
#    print(val)

#eg 7
#for val in range(1,10):
#    if val==6:
#        print(val)
 #

# break3
#! continue
#eg1
#for val in range(1,10):
#    if val==6:
#       continue
#    print(val)
# ?
#print the even number between 20 to 40
#for val in range(20,40):
#    if val 
i=0
while i<11:
   print(i)
   i=i+1
  
  
