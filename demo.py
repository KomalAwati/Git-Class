Python 3.10.0 (v3.10.0:b494f5935c, Oct  4 2021, 14:59:20) [Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.


print("hello world")
hello world


for _ in range(5):
    print("hello world")

    
hello world
hello world
hello world
hello world
hello world


for i in range(5):
print("hello")
SyntaxError: expected an indented block after 'for' statement on line 1



================== RESTART: /Users/sandeep/Desktop/testing.py ==================
hello world
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello there
hello there
1.3
apple
google
gmail
yahoo


names
['apple', 'google', 'gmail', 'yahoo']


profile
{'fname': 'sandeep', 'lname': 'suryaprasad', 'age': 26}

names.append(1.5)
names.append(10)
names.append(profile)
names
['apple', 'google', 'gmail', 'yahoo', 1.5, 10, {'fname': 'sandeep', 'lname': 'suryaprasad', 'age': 26}]




a = 10

b = 20

a + b
30


========================= RESTART: /Users/sandeep/Desktop/testing.py =========================
hello world
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello there
hello there
1.3
apple
google
gmail
yahoo
30
result
30

========================= RESTART: /Users/sandeep/Desktop/testing.py =========================
hello world
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello there
hello there
1.3
apple
google
gmail
yahoo
30

add(1, 2)
3

========================= RESTART: /Users/sandeep/Desktop/testing.py =========================
hello world
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello there
hello there
1.3
apple
google
gmail
yahoo
30
hello world
hi there

========================= RESTART: /Users/sandeep/Desktop/testing.py =========================
hello world
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello there
hello there
1.3
apple
google
gmail
yahoo
30
hello world
hi there
3


print("hello")
hello

print("hello", end="")
hello


for _ in range(5):
    print("hello")

    
hello
hello
hello
hello
hello

for _ in range(5):
    print("hello", end="")

    
hellohellohellohellohello

========================= RESTART: /Users/sandeep/Desktop/testing.py =========================
hello world
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello there
hello there
1.3
apple
google
gmail
yahoo
30
end
Traceback (most recent call last):
a  File "<pyshell#50>", line 1, in <module>
    end
NameError: name 'end' is not defined
d



add()
hello world
hi there
30
add(20)
hello world
hi there
40

add(1, 2)
hello world
hi there
3




========================= RESTART: /Users/sandeep/Desktop/testing.py =========================
hello world
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello world welcome to python!
hello there
hello there
1.3
apple
google
gmail
yahoo
30


add(1.3, 1.4)
hello world
hi there
2.7


word = "hello world"

print(word)
hello world

word = 'hello world'

print(word)
hello world

word = """this is a sentence
and this is a multiline string"""

print(word)
this is a sentence
and this is a multiline string

firstName = "sandeep"

first_name = "sandeep"


# welcome to Python's world






word = 'welcome to Python's world'
SyntaxError: unterminated string literal (detected at line 1)

word = 'welcome to Python\'s world'
print(word)
welcome to Python's world

word = "welcome to Python\'s world"

word = "welcome to Python"s world"
SyntaxError: unterminated string literal (detected at line 1)

word = "welcome to Python\"s world"
print(word)
welcome to Python"s world

word = "welcome to Python\"s world"'
SyntaxError: unterminated string literal (detected at line 1)
word = "welcome to Python\"s world"'
word = 'welcome to Python"s world'
print(word)
welcome to Python"s world


file_path = "c:\new_release\testing\release1.2\soemthing.exe"

print(file_path)
c:
ew_release	esting
elease1.2\soemthing.exe

file_path = "c:\\new_release\\testing\\release1.2\\soemthing.exe"


file_path = r"c:\new_release\testing\release1.2\soemthing.exe"
file_path = r"c:\new_release\testing\release1.2\soemthing.exe"

print(file_path)
c:\new_release\testing\release1.2\soemthing.exe



word
'welcome to Python"s world'

type(word)
<class 'str'>


word = str("hello world")

w

word = "hello world"
type(word)
<class 'str'>


a = [1, 2, 3, 4]


type(a)
<class 'list'>



word
'hello world'


dir(word)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

word.upper()
'HELLO WORLD'
word
'hello world'

u_world = word.upper()
print(u_world)
HELLO WORLD
print(word)
hello world


word = "      hello world        "

s = word.strip()
print(s)
hello world
print(word)
      hello world        
sentence = "hello world welcome to python"

parts = sentence.split()

print(parts)
['hello', 'world', 'welcome', 'to', 'python']

print(type(parts))
<class 'list'>
type(sentence)
<class 'str'>


sentence = "hello,world,welcome,to,python"

parts = sentence.split(",")
parts
['hello', 'world', 'welcome', 'to', 'python']

sentence = "hello|world|welcome|to|python"

sentence.split("|")
['hello', 'world', 'welcome', 'to', 'python']

sentence
'hello|world|welcome|to|python'

word
'      hello world        '

word = "hello world"


word.len()
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    word.len()
AttributeError: 'str' object has no attribute 'len'


len(word)
11

