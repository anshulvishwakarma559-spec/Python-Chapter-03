#Strings in Python

#What is Strings? 
'''A string is a data type  in python that stores
 a sequence of character - letters, numbers, or 
 symbols - enclosed in single, double, or triple quotes.
'''
#Example: 
print("First\n")
str1 = 'Hello'
str2 = "Anshul Vishwakarma"
str3 = '''Welcome to Python'''
print(str1,"\n",str2,"\n",str3)

#Strings are immutable, meaning once created, their content cannot be change directly (jinki vlaue change nhi ki ja sakti use immutable kehte hai.)

#String concatenation : 

print("Second\n")
print(str1+" "+str2+" "+str3)   


#Length of String : 

print("Length\n")
print(str1)  
print(len(str1)) #5

#Indexing: -  Each character in a string has a position(index) starting from 0.
#str   = "K h u s h i M e h r a"
#Index = "0 1 2 3 4 5 6 7 8 9 10"
#Example:
print("Indexing\n") 
print(str1[0]) #H
print(str1[1]) #e
print(str1[2]) #l
print(str1[3]) #l
print(str1[4]) #o
#This throws error "print(str1[5])"

#Practice Question : Write a python program that takes a user's name as input and print:
 #The first character
 #The last character
 #The total length of the name
print("Practice\n")
Name = input("Enter your Name : ")#Anshul
print("Your name is : ",Name)
print("The first letter of your name is : ",Name[0])  #A
print("The last letter of your name is : ",Name[-1]) #l
print("Length of your name is : ",len(Name)) #6

#Using loop 

print("Lets use a for loop\n")
for char in Name:
    print(char)

#Slicing: - Slicing lets you access a part of a string. 
#Syntax:  string[start:end] 
#End index is not executed
#Example : 
print("Slicing\n")
Name1 =  input("Enter your Name : ")#Anshul Vishwakarma
print(len(Name1))
print(Name1[:])   #Blank chhodne pr puri string print hogi
print(Name1[0:5]) #starting ke 5 letters print honge
print(Name1[:6])  #Starting point blank chhodne pr use 0 se strat  karega
print(Name1[5:])  #last blank chhodne pr start jahase kiya unhe chhodkr saraa print karayega
print(Name1[0:21]) #strig me 21 letters h nhi fir bhi hamne 21 likha to koi error nhi aayega puri hi string print hogi 
print(Name1[15:20]) #jitnwe letter mil rahe bo print honge
print(Name1[19:22]) #19 se 22 letter h hi nhi to blank print hoga

#Negative Indexing
#   A   N   S   H   U   L   V   I   S   H   W   A   K   A   R   M   A 
#  -17 -16 -15 -14 -13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
#Example: 

print("Negative Slicing\n")
print(Name1[-17:-12]) #second letter se aayega
print(Name1[-18:-12])  # first letter se aayega 
print(Name1[0:-17])   #blank
print(Name1[-18:-1])  #last character ko chhodkr puri string print hogi 
print(Name1[-18:0])   #blank 

##Practice Question : write a python program that takes your favorite food name as input and print.

print("Practice2\n")
food = input("Enter your favorite food : ")
mid = len(food)//2
if len(food) >= 3:
    print(food[mid-1:mid+2])
else:
    print(food)


str10 = "HELLO ANSHUL"
str20 = "kese ho"
print(str10 and str20)  # and operator returns the second value when both strings are non-empty

#Quick Quiz: 
nm = "Harry"
print(nm[-4:-2])   #ar