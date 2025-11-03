print("Hello, World!")


if 5 > 2 :
    print("Five is greater than two!")
#استفاده از تو رفتگی برای نشان دادن یک بلوک کد


if 5 > 2 :
    print("Five is greater than two!")
if 5 > 2 :
          print("Five is greater than two!")
"""تعداد فاصله در تورفتگی وابسته به برنامه نویس است اما باید حداقل یک فاصله وجود داشته باشد"""



x = 5
y = "john"
print(x)
print(y)

x = 4 #x is of type int
x = "sally" #x is now of type str
print(x)


x = str(3) # x will be '3'
y = int(3) # x will be 3
z = float (3)  # x will be 3.0
print(x)
print(y)
print(z)


x = 5
y = "john"
print(type(x))
print(type(y))


x = "john"
# is the same as
x = 'john'

a = 4
A = "sally"
# A will not overwrite a 
print(a)
print(A)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# مقدار دادن به چند متغیر در یک
#اطمینان از طابق تعداد متغیرها با تعداد مقادیر


x = y = z = "Orange"
print(x)
print(y)
print(z)
#اختصاص یک مقدار در یک خط یه چند متغیر


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits 
print(x)
print(y)
print(z)
# unpacking : استخراج مقادیر در متغیرها


x = "Python is awesome"
print(x)
#تابع print() برای خروجی دادن متغیرها استفاده میشود

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#در این تابع print (), چندین متغیر را که با کاما از هم جدا شده اند خروجی میدهد

x = "Python"
y = "is"
z = "awesome"
print(x + y + z)
# میتوان از عملگر + برای خروجی دادن چندین متغیر استفاده کنید

x = 5
y = 10
print(x + y)
# برای اعداد این + کاراکتر به عنوان یک عملگر ریاضی عمل میکند

x = 5 
y = "john"

#در تابع print() در صورت جمع یک رشته و یک عدد با + , پایتون خطا میدهد

x = 5
y = "john"
print(x, y)
#بهترین راه برای خروجی  رفتن از چندین متغیر در تابع print() جدا کردن آنها با کاما است


#ایجاد یک متغیر خارج از یک تابع و استفاده از ان در داخل تابع
x = "awesome"

def myfunc():
     print("Python is" + x)
myfunc()


#ایجاد یک متغیر درون یک تابع با همان نام متغیر سراسری
x = "awesome"

def myfunc():
     x = "fantastic"
     print("Python is" + x)

myfunc()

print("Python is" + x)



""" برای تغییر مقدار یک متغیر سراسری درون یک تابع
 با استفاده از کلمه کلیدی global به متغیر اشاره کنید"""


x = "awesome"

def myfunc():
     global x
     x = "fantastic"
myfunc()
print("Python is" + x)


x = 5
print(type(x))
 # استفاده از تابع type() برای دریافت نوع داده هر شی



#مثال هایی از تنظیم نوع داده ها
x = "Hello, World"
#display x :
print(x)
#display the data type of x :
print(type(x))

x = 20
#display x:
print(x)
#display the data type of x:
print(type(x))


x = ["apple", "banana", "cherry"]
#display x :
print(x)
#display the data type of x:
print(type(x))


x = frozenset({"apple", "banana", "cherry"})
#display x :
print(x)
#display the date type of x:
print(type(x))


#مثال هایی از تنظیم نوع داده خاص
x = str("Hello World")
#display x:
print(x)
#display the date type of x:
print(type(x))

x = int(20)
#display x :
print(x)
#display the date type of x :
print(type(x))

x = list(("apple", "banana", "cherry"))
#display x :
print(x)
#display the date type of x :
print(type(x))


x = bool(5)
#display x :
print(x)
#display the date type of x :
print(type(x))


#اعداد پایتون

x = 1    # int
y = 2.8  #float
z = 1j   #complex

# تابع type() برای بررسی نوع هر شی

x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))

#int
x = 1 
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

#float
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

#complex
x = 3 + 5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))


#casing: you can convert from one type to another with int(), float() and cmplex() methods:

#convert from int to float:
x = float(1)
#convert frm float to int:
y = int(2.8)
#convert from int to complex:
z = complex(1)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

#Python Casting 

x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)

# رشته های پایتون/ احاطه شده با نقل قول تکی یا دوتایی

print("Hello")
print('Hello')

print("It's alright")
print("He is called 'johnny")
print('He is called "johnny"')

#اختصاص رشته به یک متغیر
a = "Hello"
print(a)

#رشته های چندخطی

a = """Lorem ipsum sit amet, consectetur adioicing elit, sed do eiusmod tempor incident ut labore et dolore magna aliqua""" 
print(a)

a = '''em ipsum sit amet, consectetur adioicing elit, sed do eiusmod tempor incident ut labore et dolore magna aliqua'''
print(a)

#برای دسترسی به عناصر رشته میتوان از براکت های مربعی استفاده کرد

a = "Hello, World!"
print([a])

#پیمایش با استفاده از حلقه هل

for x in "banana":
     print(x)


#طول رشته / تابع len()

a = "Hello, World!"
print(len(a))

#برای بررسی وجود یک عبارت یا کاراکتر خاص در یک رشته/ کلمه کلیدی in

txt = "The best things in life are free!"
print("free" in txt)


#slicing strings

b = "Hello, World!"
print(b[2:5])

#برش از ابتدا
b = "Hello, World!"
print(b[:5])

#برش تا انتها
b = "Hello, World!"
print(b[2:])

#نمایه سازی منفی
b = "Hello, World!"
print(b[-5:-2])


#مجموعه ای از متدهای از پیش تعریف شده

b = "Hello, World!"
print(a.upper())  # رشته را با حروف بزرگ برمیگرداند

b = "Hello, World!"
print(a.lower()) # رشته را به حروف کوچک برمیگرداند

a = "Hello, World!"
print(a.replace("H", "J")) #replace sring

a = " Hello, World! "
print(a.strip())  #remove whitespace 

a = "Hello, World!"
b = a.split(",")
print(b)  #split string

#عملگر + برای ترکیب یا الحاق دو رشته
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)
 


#fsttring : روشی‌برای‌نمایش‌دادن‌ترکیبی‌stringها‌و‌متغیر ها
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#قالب بندی رشته ها / placeholder
price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

name = "Alice"
age = 30
greeting = f"Hello, I'm {name} and I'm {age} years old."
print(greeting) 
#Output: Hello, I'm Alice and I'm 30 years old.

x = 10
y = 20
result = f"The sum of {x} and {y} is {x + y}."
print(result) 
#Output: The sum of 10 and 20 is 30.


#escape character : برای‌وارد‌کردن‌کاراکترهایی‌که‌در‌یک‌رشته‌غیرمجاز‌هستند
txt = 'It\'s alright.'
print(txt)

txt = "This will insert one \\ (backslash)."
print(txt)

txt = "Hello\nWorld!"
print(txt)

txt = "Hello\tWorld!"
print(txt)

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)

txt = "Hello\rWorld!"
print(txt)

#مقادیر بولی : True / False
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a:
     print("b is greater than a")
else:
     print("b is not greater than a")

#isinstance() :تابعی‌که‌می‌تواند‌برای‌تعیین‌اینکه‌آیا‌یک‌شیء‌از‌نوع‌داده‌ خاصی است یا نه استفاده شود
x = 200
print(isinstance(x, int))

#عملگرهای حسابی
x = 5
y = 3
print(x + y)

x = 12
y = 3
print(x / y)

x = 15
y = 2
print(x // y)

x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2

x = 5
y = 3
print(x - y)

x = 5
y = 3
print(x * y)

#عملگر های انتساب

x = 5
print(x)

x = 5
x += 3
print(x)

#عملگرهای مقایسه ای

x = 5
y = 3
print(x == y)

x = 5
y = 3
print(x != y)

x = 5
y = 3
print(x >= y)

#عملگر های منطقی

x = 5
print(x > 3 and x < 10)

x = 5
print(x > 3 or x < 4)

x = 5
print(not(x > 3 and x < 10))

#عملگرهای هویت
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y,even if they have the same content 
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
#returns True because x is not the same object as y, even if they have the same content
print(x != y) 

#عملگر های عضویت

x = ["apple", "banana"]
print("banana" in x)

x = ["apple", "banana"]
print("pineapple" not in x)


#عملگرهای بیتی

print(6 & 3)  #and

print(6 | 3) #or

#اولویت عملگرها

print((6 + 3) - (6 + 3))
"""Parenthesis have the highest precedence, and need to be
evaluated first.
The calculation above reads 9 - 9 = 0
"""