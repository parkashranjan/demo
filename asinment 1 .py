# 1..........
#  str='bhawan'
# print("length of the function: ",len(str))
                       
                  

# 2............

# str='bhawan'
#  x=str.count('h',0)
# print("h:",x)


# 3..............
# str='bhawandeep'
# if len(str) < 2:
#     print("")
# else:
#     ns=str[:2]+str[-2:]
#     print(ns)   
 

#  4.................
# str='my life my rules'
# str=str.replace('m','$')
# print('new version of string::')
# print(str)

# 5.............
# str='abc'

# 6...........................
# def add_string(str1):
#   length = len(str1)

#   if length > 2:
#     if str1[-3:] == 'ing':
#       str1 += 'ly'
#     else:
#       str1 += 'ing'

#   return str1
# print(add_string('ab'))
# print(add_string('abc'))
# print(add_string('string'))

# 7..............
# def not_poor(str1):
#   snot = str1.find('not')
#   spoor = str1.find('poor')
  

#   if spoor > snot and snot>0 and spoor>0:
#     str1 = str1.replace(str1[snot:(spoor+4)], 'good')
#     return str1
#   else:
#     return str1
# print(not_poor('The lyrics is not that poor!'))
# print(not_poor('The lyrics is poor!'))


# 8.......................
# a=['you','are','beautiful']
# maxx=len(a[0])
# temp=a[0]
# for i in a:
#     if(len(i)>maxx):
#         maxx=len(i)
#         temp=i
# print('the longest word is',temp)
# print('length of word is',maxx)        

# 9..................
# str='lifeisfun'
# n=4

# modify_str=''
# for char in range(0,len(str)):
#     if(char !=n):
#         modify_str+=str[char]
# print("modify the string after remove ",n)   
# print(modify_str)     

# 10............
# string = input("Enter a string :-")
# new_str = string[-1] + string[1:-1] + string[0]
# print(new_str)

# 
# 11................
# str1='i am the best'
# str2 = ""
# for i in range(len(str1)):
#     if(i%2==0):
#         str2=str2+str1[i]
# print('previous string:',str1)
# print('new string',str2)   
# 
# 23...............
# a='i am the best'
# print(a)
# if(a[0]=='i'):
#     print('it has sepecific character')
# else:
#      print('not')   
# 

# 12..........
# str=len('life is very beautiful'.split())
# print('count the given words: ',str)

# 13.........

# str=input('enter any string: ')
# print(str.upper())
# print(str.lower())

# 14...............
# str=input('enter any input: ')
# str2=str.split(',')
# str2.sort()
# print(',').join(str)

# 15............
# def add_tags(tag, word):
# 	return "<%s>%s</%s>" % (tag, word, tag)
# print(add_tags('i', 'khushi'))
# print(add_tags('b', 'khushdeep'))

# 16.................
# test_str = 'bhawan play'
  
# # printing original string
# print("The original string is : " + str(test_str))
  
# # initializing mid string
# mid_str = "love to"
  
# # splitting string to list
# temp = test_str.split()
# mid_pos = len(temp) // 2
  
# # appending in mid
# res = temp[:mid_pos] + [mid_str] + temp[mid_pos:]
  
# # conversion back
# res = ' '.join(res)
  
# # printing result
# print("Formulated String : " + str(res))


#18Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string. 
# a='python'
# if(len(a)>3):
#    print(a[:3])
# else:   
#    print(a)

#19program to get the last part of a string before a specified character


#20Python function to reverses a string if it's length is a multiple of 4
# a='pythonclass'
# if(len(a)%4==0):
#     print(a[::-1])
# else:
#     print(a)    

#21Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters\
# a='bhawan'
# num=0
# for x in a[:4]:
#     if(x.upper()==x):
#         num+=1
# if(num>=2):
#     print(a.upper())        
# else:
#     print(a)    

#22Python program to remove a newline in Python
# a='python class\n'
# print(a)
# print(a.rstrip())
# print(a)

#23Python program to check whether a string starts with specified characters.
# a='bhawan'
# print(a.startswith('Pr'))