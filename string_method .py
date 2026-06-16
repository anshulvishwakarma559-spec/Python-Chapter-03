#Common string methods
'''
   Method                      Description                                                                                                         Example
.upper()                 Converts all characters to uppercase          - - - - - - - - - - - - - - - - - - - - - - - - - -         "samosa".upper() -> "SAMOSA"                                                                 "samosa".upper() -> "SAMOSA"
.lower()                 Converts all characters to lowercase          - - - - - - - - - - - - - - - - - - - - - - - - - -         "SAMOSA".lower() -> "samosa"
.title()                 Capitalizes the first letter of each word     - - - - - - - - - - - - - - - - - - - - - - - - - -         "hello world".title() -> "Hello World"
.find()                  Returns index of first occurence              - - - - - - - - - - - - - - - - - - - - - - - - - -         "banana".find("na") -> 2
.replace(old,new)        Replaces all occurences                       - - - - - - - - - - - - - - - - - - - - - - - - - -         "Python is cool".replace("cool","fun") -> "Python is fun"
.count(sub)              Counts occurrences                            - - - - - - - - - - - - - - - - - - - - - - - - - -         "Khushi".count("h") -> 2
.endswith(suffix)        Checks if string ends with given substring    - - - - - - - - - - - - - - - - - - - - - - - - - -         "coder.".endswith(".") -> True
.rstrip()                Remove trailing character from the end of a string            - - - - - - - - - - - - - - - - - -         "Hi!!!!!".rstrip("!")  -> Hi 
.split()                 Default me split() space ke basis par string ko todta hai.    - - - - - - - - - - - - - - - - - -         "Hello Anshul kese ho".split(" ") -> ["Hello","Anshul","kese","ho"]
.capitalize()            Capitalize the first letter of sentence                       - - - - - - - - - - - - - - - - - -         "hello anshul kese ho".capitalize() -> Hello anshul kese ho 
.center(45)              String ko center me align karne ke liye use hota hai.         - - - - - - - - - - - - - - - - - -         "Hello".center(50) ->          Hello 
.index()                 Kisi character ya word ki position (index) batata hai.        - - - - - - - - - - - - - - - - - -         "Python".index("t") -> 2
.isalnum()               Agar string me sirf alphabets aur digits hain → True 
----------               Agar space, special character (@, #, _, etc.) hai → False     - - - - - - - - - - - - - - - - - -         "Python123".isalnum() -> True 
.isalpha()               Agar string me sirf letters hain → True                       - - - - - - - - - - - - - - - - - -          
----------               Agar number, space ya special character hai → False                   - - - - - - - - - - - - - -         "Python".isalpha() -> True 
.islower()               Check karta hai ki string ke saare alphabet lowercase hain ya nahi.   - - - - - - - - - - - - - -         "Python".islower() -> False
.isprintable()           Check karta hai ki string ke saare characters screen par print kiye ja sakte hain ya nahi.    - -         "Hello World".isprintable()  -> True
.isspace()               Check karta hai ki string me sirf whitespace characters hain ya nahi                          - -         "  ".isspace() -> True
.istitle()               Check karta hai ki string title case format me hai ya nahi (har word ka first letter capital ho).         "Hello World".istitle() -> True
----------                                                                                                                         "hello world".istitle() -> False
.isupper()               Check karta hai ki string ke saare alphabet uppercase hain ya nahi.   - - - - - - - - - - - - - -         "HELLO WORLD".isupper() -> True
----------                                                                                                                         "Hello world".isupper() -> False
.startswith(suffix)      Checks if string starts with given substring                  - - - - - - - - - - - - - - - - - -          "Hello world".startswith("H") -> True
-------------------                                                                                                                "Hello world".startswith("c") -> False

.swapcase()              Convert uppercase to lowercase and lowercase to uppercase             - - - - - - - - - - - - - -         "Hello world".swapcase() -> "hELLO WORLD"

'''
#For Example : 
name = input("Enter : \n")

#uppercase()
print("uppercase:\n",name.upper())

print("="*40)

#lowercase()
print("lowercase:\n",name.lower())

print("="*40)

#title()
print("Capitalize the first letter 'title()':\n",name.title())

print("="*40)

#find()
print("Find the string index 'find(a)':\n",name.find("a"))

print("="*40)

#replace()
print("Replace the character 'replace()' all occurrence:\n",name.replace("a","k"))

print("="*40)

#count()
print("Count the character 'count()':\n",name.count("h"))

print("="*40)

#endswith()
print("endswith():\n",name.endswith("r"))

print("="*40)

#rstrip()
str1 = "Hi!!!!!!!!"
print("Remove trailing character 'rstrip(!)':\n",str1.rstrip("!"))

print("="*40)

#split()
str2 = "hello Anshul Kese ho"
print("split():\n",str2.split(" "))

print("="*40)

#capitalize()
print("capitalize():\n",str2.capitalize())

print("="*40)

#center()
print("center():\n",str2.center(50))

#Strings are immutable.
#Once created, a string cannot be modified directly.

print("="*40)

#index()
text = "python"
print("index():\n",text.index("t"))

print("="*40)

#isalnum()
ab = "python123"
print("isalnum() True condition:\n",ab.isalnum()) 

bc = "Python 123"
print("isalnum() False condition :\n",bc.isalnum())

print("="*40)

#isalpha ()
x = "Welcome"
print("isalpha() True condition:\n",x.isalpha())

o = "Welcome1223"
print("isalpha() False condition:\n",o.isalpha())

print("="*40)

#islower ()
gd = "LOwer"
gh = "lower"
print("islower() False condition:\n",gd.islower())
print("islower() True condition:\n",gh.islower())

print("="*40)

#isprintable()
sd = "hello world"
print("isprintable() True condition:\n",sd.isprintable())

ds = "hello\n World"
print("isprintable() False condition:\n",ds.isprintable())

print("="*40)

#.isspace() 
f = "  "
print("isspace():\n",f.isspace())

print("="*40)

#istitle()
g = "Hello World"
print("istitle() True condition:\n",g.istitle())

h = "hello  World"
print("istitle() False condition:\n",h.istitle())

print("="*40)

#isupper()
w = "HELLO WORLD"
print("isupper() True condition:\n",w.isupper())

e = "Hello world"
print("isupper() False condition:\n",e.isupper())

print("="*40)

#startswith()
q = "Hello world"
print("startswith() True condition:\n",q.startswith("H"))

r = "Hello world"
print("startswith() False condition:\n",r.startswith("c"))

print("="*40)

#swapcase()
y = "Hello world"
print("swapcase():\n",y.swapcase())

