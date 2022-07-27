# 1 palindrome program
user_in=input('enter the string: \n')
print('the string entered is',user_in)
if(user_in[::-1]==user_in):
    print(user_in,'is a palindrome')
else:
    print(user_in,'is not a palindrome')    

# 2 FACTORIAL PROGRAM    
def factorial(n):
    if(n==1 or n==0):
       return 1
    else: 
        return (n * factorial(n-1))
num=int(input('Enter the number you want to find factorial:'))      
fact = factorial(num)
print('factorial of',num,'=',fact)    

# 3FIBONACCI SERIES
def fibonacci(n):
    if (n==1 or n==0):
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
num=int(input('enter number of terms of series:'))
i=0
print('Fibonacci Series:')
while(i<num):
    print(fibonacci(i))
    i+=1

# 4 Armstrong Number Program
num=int(input('enter a number:'))
order=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
if num==sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")        

# 5 Calculator Program
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print('CALCULATOR')
print('Select Operation:')
print('1. ADD\n2. SUBTRACT\n3. MULTIPLY\n4. DIVIDE\n5. EXIT\n')
while True:
    choice=input('Enter choice(1/2/3/4/5):')
    if choice in ('1','2','3','4'):
        num1=float(input('Enter first number:'))
        num2=float(input('Enter second number:'))

        if choice=='1':
            print(num1,'+',num2,'=',add(num1,num2))
        elif choice=='2':
            print(num1,'-',num2,'=',sub(num1,num2))
        elif choice=='3':
            print(num1,'X',num2,'=',mul(num1,num2))
        elif choice=='4':
            print(num1,'/',num2,'=',div(num1,num2))
    elif choice=='5':
            print('EXIT')
            break
    else:
        print('Invalid choice')

# 6 Patterns Program
for x in range(4):
    for x in range(4):
        print('x',end=' ')
    print(' ')

for x in range(5):
    for y in range(x):
        print('x',end=' ')
    print(' ')

for x in range(5):
    x+=1
    for y in range(x):
        print(x,end=' ')
        x+=1
    print(' ')

num=1
for x in range(5):
    for y in range(x+1):
        print(num,end=' ')
        num+=1
    print(' ')

# 7LEAP YEAR PROGRAM
year=int(input('enter the year:'))
if (year%400==0 and year%100==0):
    print(year,'is leap year')
elif(year%4==0 and year%100!=0):
    print(year,'is leap year')
else:
    print(year,'is not a leap year')

# 8PRIME NUMBER PROGRAM
num=int(input('enter the number:'))
if(num>1):
    for i in range(2,num):
        if (num%i)==0:
            print(num,'is not a prime number')
            break
    else:
        print(num,'is a prime number')
else:
    print(num,'is not a prime number')

# 9 PROGRAM TO FIND AREA
area of square
print('AREA OF SQUARE')
side=float(input('enter the length of side of square:'))
area=side**2
print('area of square is ',area,'sq. unit')

area of rectangle
print('AREA OF RECTANGLE')
length=float(input('enter the length of rectangle:'))
breadth=float(input('enter the breadth of rectangle:'))
area=length*breadth
print('area of rectangle is ',area,'sq. unit')

area of circle
pi=3.14
r=float(int(input('enter the radius of circle:')))
area=pi*r**2
print('area of circle is ',area,'sq. unit')

# 10 Program To Reverse A List 
l=[1,3,5,7,9]
print('list=',l)
l.reverse()
print('reverse list=',l)

# 11 Program to find  sum of all elements in list
l=[1,3,5,7,9]
print(l)
sum=0
for x in range(len(l)):
    sum+=l[x]
print('sum of elements of list:',sum)

# 12 Find average, max, min  of list elements
l=[1,5,3,7,44,23,8]
print('elements of list:')
for x in range(len(l)):
    print(l[x],end=',')
maximum=max(l)
print('\nmaximum:',maximum)
minimum=min(l)
print('minimum:',minimum)
sum=0
for x in range(len(l)):
    sum+=l[x]
avg=sum/len(l)
print('Average of elements:',avg)

# 13  grouping dictionary
def grouping_dictionary(l):
    result = {}
    for k, v in l:
         result.setdefault(k, []).append(v)
    return result
colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print("Original list:")
print(colors)
print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
print(grouping_dictionary(colors))

# 14 nested dictionary
def nested_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result
student_id = ["1", "2", "3"] 
student_name = ["khushdeep", "muskandeep ", "prabhdeep"] 
student_grade = [95,96,94]
print("Original strings:")
print(student_id)
print(student_name)
print(student_grade)
print("\nNested dictionary:")
ch='a'
print(nested_dictionary(student_id, student_name, student_grade))

# 15 Python program to check if a set is a subset of another set.
print("Check if a set is a subset of another set, using comparison operators and issubset():\n")
setx = set(["a", "b","c"])
sety = set(["a", "b"])
setz = set(["a"])
print("x: ",setx)
print("y: ",sety)
print("z: ",setz,"\n")
print("If x is subset of y")
print(setx <= sety)
print(setx.issubset(sety))
print("If y is subset of x")
print(sety <= setx)
print(sety.issubset(setx))
print("\nIf y is subset of z")
print(sety <= setz)
print(sety.issubset(setz))
print("If z is subset of y")
print(setz <= sety)
print(setz.issubset(sety))

# 16 program to create a symmetric difference and set difference
set1=set([1,2,5,7,9,1])
set2=set([1,5,9,5,3,6])
print('sets:')
print('set1:',set1)
print('set2:',set2)
d1=set1.symmetric_diffetrence(set2)
print('symmetric difference of set1-set2:')
print(d1)
d2=set2.symmetric_difference(set1)
print('symmetric difference of set2-set1:')
print(d2)
d3=set1.difference(set2)
print('difference of set1 -set2:')
print(d3)
d4=set2.difference(set1)
print('difference of set2-set1:')
print(d4)

# 17 program to remove an empty tuple(s) from a list of tuple
def remove(tuples):
    tuples=[t for t in tuples if t]
    return tuples
tuples=[(),('1'),('2','3'),(),('hello','khush')]
print(tuples)
print(remove(tuples))

