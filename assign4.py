#example 1

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod

    def eat1(self):

        pass

    @abstractmethod

    def eat2(self):

        pass

class Tiger(Animal):

    def eat1(self):

        print("Tiger implementation ...")

class lion(Tiger):

    def eat2(self):

        print("lion implementation ..")

t = lion()

t.eat1()

t.eat2()

 

# Example 2

from abc import ABC, abstractmethod

class AbstractClassExample(ABC):

    def _init_(self, value):

        self.value = value

        super()._init_()

    @abstractmethod

    def do_something(self):

        pass

class DoAdd(AbstractClassExample):

    def do_something(self):

        return self.value + 42

 

class DoMul(AbstractClassExample):

 

    def do_something(self):

        return self.value * 42

 

x = DoAdd(10)

y = DoMul(10)

print(x.do_something())

print(y.do_something())

 

# Example 3

 

def status(age):

    if age < 0:

        raise ValueError("Only positive integers are allowed")

    if age>22:

        print("eligible for mrg")

    else:

        print("not eligible for mrg try after some time")

try:

    num = int(input("Enter your age: "))

    status(num)

except ValueError:

    print("Only positive integers are allowed you ......")

finally:

    print("finally block....")

 

# Example 5:

 

class TooYoungException(Exception):

 def _init_(self,age):

        self.age=age

class TooOldException(Exception):

    def _init_(self,age):

        self.age=age

try:

    age=int(input("Enter Age:"))

    if age<18:

        raise TooYoungException("Plz wait some time ")

    elif age>65:

        raise TooOldException("Your age too old")

    else:

        print("we will find one girl soon")

except TooYoungException as e:

    print("Plz wait some time ")

except TooOldException as e:

    print("Your age too old ")

 

# Example 6:

try:

    print("outer try block")

    n = int(input("enter a number"))

    print(10/n)

    try:

        print("inner try")

        print("anu"+"preet")

    except TypeError:

        print("Hello")

    else:

        print("inner no exception")

except ArithmeticError:

    print(10/5)

else:

    print("outer no excepiton")

finally:

    print("finally block")

 

# Example 7

 

class Person(object):

    def _init_(self, first, last):

        self.firstname = first

        self.lastname = last

    def Name(self):

        return self.firstname + " " + self.lastname

class Employee(Person):

    def _init_(self, first, last, staffnum):

        super()._init_(first,last)

        # Person._init_(self,first, last)

        self.staffnumber = staffnum

    def GetEmployee(self):

        return self.Name() + ", " + self.staffnumber

x = Person("komal", "addanki")

y = Employee("komal", "addanki", "111")

print(x.Name())

print(y.GetEmployee())

 

# Example 8

class Person:

    def _init_(self, first, last):

        self.firstname = first

        self.lastname = last

    def _str_(self):

        return self.firstname + " " + self.lastname

class Employee(Person):

    def _init_(self, first, last, id):

        super()._init_(first, last)

        self.id = id

    def _str_(self):

        return super()._str_()+" "+self.id

x = Person("kamalpreet", "gurpreet")

y = Employee("kamalpreet", "gurpreet", "111")

print(x)

print👍

 

# Example 9

class Vehicle:

    def _del_(self):

        print("Vehicle object destroyed")

        print(10/0)

v = Vehicle()

del v

 

# Example 10

class Customer:

    def _init_(self,name,bal=0.0):

        self.name=name

        self.bal=bal

    def deposit(self,amount):

        self.bal=self.bal+amount

    def withdraw(self,amount):

        if amount>self.bal:

            raise RuntimeError("withdraw amount is more than balance")

        else:

            self.bal=self.bal-amount

    def remaining(self):

        return self.bal

 

c = Customer("Komal",10000)

damt = int(input("enter amount to deposit"))

c.deposit(damt)

amt = int(input("enter amount to withdraw"))

c.withdraw(amt)

print(c.remaining())