# 1. Create a variable, paragraph, that has the following content:
# "Python is a great language!", said Fred. "I don't ever remember
# having this much fun before."


#Ans 1:

# paragraph='"Python is a great language!", said Fred. "I don\'t ever remember \n having this much fun before."'
# print(paragraph)


#OR

#Ans 2:

# paragraph ="""
# "Python is a great language!", said Fred. "I don't ever remember
# having this much fun before."
# """
# print(paragraph)


#------------------------------------------------------------------------------------------------------------------


# 2. Write an if statement to determine whether a variable holding a year is
# a leap year.


#Ans:

# x=int(input("Enter year:"))
#
# if x % 4 ==0:
#     if x%100 == 0:
#         if x%400==0:
#             print(x,"is leap year")
#         else:
#             print(x,"is not leap year")
#     else:
#         print(x,"is leap year")
# else:
#     print(x,"is not leap year")


#------------------------------------------------------------------------------------------------------------------


# 3. Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.


#Ans:

# text = """I live in United States. The food here, it tastes so good.
# The beautiful thing about US is it's night life.
# """
#
# s=(text.translate(text.maketrans({'\n':' ', '.':'', ',':''})).lower()).split(' ')
# y=set(s)
# a=list(y)
#
# empty_list=[]
# for i in a:
#     sorted_word=sorted(i)
#     new_list= "".join(sorted_word)
#     empty_list.append(new_list)
#
#
# empty_set=set()
# for i in empty_list:
#     if empty_list.count(i)>=2:
#         empty_set.add(i)
#
#
#
# print("The anagrams that are used in given paragraph :", empty_set)



#------------------------------------------------------------------------------------------------------------------


# #4. Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?


#Ans:

# my_friends = ['ram', 'shyam']
# friends_names = ['sita', 'gita']
#
# for i in friends_names:
#     my_friends.append(i)
#
# my_friends.sort()
# print(my_friends)
# print(f'First Item on the list: "{my_friends[0]}" and second item of the list: "{my_friends[1]}"')
#


#------------------------------------------------------------------------------------------------------------------


# 5. Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.


#Ans:

# my_tuple = ('ram', 'kumar', 40)
# people =[]
# people.append(my_tuple)
#
# more_tuples =(('shyam', 'thapa', 45), ('sita', 'devi', 30), ('gita', 'kumari', 37))
# for i in more_tuples:
#     people.append(i)
#
# people.sort(key = lambda x: x[2])
# print("Sorted list is:", people)


#------------------------------------------------------------------------------------------------------------------


# 6. Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.


#Ans:

# list_of_names = ['Ram', 'Shyam',  'Harry', 'Sita', 'Dora', 'Sari', 'Jed']
#
# def search(l, s):
#     count=0
#     for i in l:
#         if i!=s:
#             count =count +1
#         else:
#             print("found")
#             break
#
#     if count == len(list_of_names):
#         print("not found")
#
# search(list_of_names, "John")


#------------------------------------------------------------------------------------------------------------------


# 7. Create a list of tuples of first name, last name, and age for your friends
# and colleagues. If you don't know the age, put in None. Calculate the
# average age, skipping over any None values. Print out each name,
# followed by old or young if they are above or below the average age.


#Ans:

# friends_list = [('shyam', 'thapa', 45), ('sita', 'devi', 30), ('gita', 'kumari', 37), ('gayatri', 'kumari', None),
#                 ('geet', 'kumari', None), ('gopi', 'kumar', 20)]
#
#
# #Calculating Average
# newlist=[]
# for i in friends_list:
#     newlist.append(i[2])
#
# count=0
# sum = 0
# for i in newlist:
#     if i == None:
#         continue
#     else:
#         count = count +1
#         sum=sum+i
#
# average = sum/count
#
# #Finding old or young
# for i in friends_list:
#     if i[2] != None:
#         if i[2] < average:
#             print(f'{i[0]} {i[1]} is young')
#         else:
#             print(f'{i[0]} {i[1]} is old')
#     else:
#         pass



#------------------------------------------------------------------------------------------------------------------


# 8. Write a function, is_prime, that takes an integer and returns True if the
# number is prime and False if the number is not prime


#Ans:

# def is_prime(n):
#     if n>1:
#         count=0
#         for i in range(2,n):
#             if n%i!= 0:
#                 count=count+1
#         if count==n-2:
#             return True
#         else:
#             return False
#     else:
#         return False
#
# print(is_prime(int(input("Enter integer:"))))



#------------------------------------------------------------------------------------------------------------------


# 9. Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found


#Ans:

#
# # l=[1,2,5,6,3,4]
# l=['d', 'k', 'f', 'z', 'a']
# l.sort()
#
# def binary_search(sorted_seq, item):
#     if item in sorted_seq:
#         indx = sorted_seq.index(item)
#         return indx
#     else:
#         return -1
#
# print(binary_search(l, 'a'))



#------------------------------------------------------------------------------------------------------------------


# 10. Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.


#Ans:


# def string(s1, seperator):
#     l1=[]
#     l2=[]
#     for i in s1:
#         if i.isupper():
#             x=i.lower()
#             l1.append("_")
#             l1.append(x)
#             l2.append(seperator)
#             l2.append(x)
#         else:
#             l1.append(i)
#             l2.append(i)
#     l1.pop(0)
#     l2.pop(0)
#
#     snakecase= ''.join(l1)
#     kebabcase = ''.join(l2)
#
#     print('snake case:', snakecase)
#     print('kebab case:', kebabcase)
#
# string('ThisIsCamelCased', '-')



#------------------------------------------------------------------------------------------------------------------


# 11. Create a variable, filename. Assuming that it has a three-letter
# extension, and using slice operations, find the extension. For
# README.txt, the extension should be txt. Write code using slice
# operations that will give the name without the extension. Does your
# code work on filenames of arbitrary length?


#Ans:

#METHOD 1 (Assuming three letter extension )

# filename="README.txt"
#
# def filename_func(s):
#
#     ext=s[-3:len(s)]
#     print('Extension is:', ext)
#
#     fn=s[0:-4]
#     print('Filename is:', fn)
#
#
# filename_func(filename)




#METHOD 2 (Assuming extension of any length)

# filename="README.txt"
#
# def filename_func(s):
#     indx=s.find(".")
#
#     #finding extension
#     e=slice((indx+1), len(s))
#     print('The extension of the filename is:', s[e])
#
#     #finding filename
#     f=slice(0,indx)
#     print('The filename is:', s[f])
#
#
# filename_func(filename)


#>>Code works on filename of any length



#------------------------------------------------------------------------------------------------------------------


# 12. Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.


# def is_palindrome(s):
#
#     s1=s[0:len(s)]
#     s2=s[::-1]
#
#     if s1 == s2:
#         print("The word is palindrome")
#     else:
#         print("The word is not palindrome")
#
#
#
# is_palindrome('madam')



#------------------------------------------------------------------------------------------------------------------



# 13. Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',
# 21)] it should write the following in the file:
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21


#Ans:


# import csv
#
# list_of_tuples = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',21)]
# filename='testfile.csv'
#
# def csv_file(fn, lt):
#
#      l=[['name','address','age']]
#
#      for i in lt:
#           a=list(i)
#           l.append(a)
#
#      with open(fn, 'w', newline='') as file:
#           writer=csv.writer(file)
#           writer.writerows(l)
#
# csv_file(filename, list_of_tuples)


#------------------------------------------------------------------------------------------------------------------


# 14. Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.
# For the data in the previous example it would return:
# [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
# 'John', 'address': '54 Love Ave', 'age': 21}]


#Ans:

# import csv
# filename='testfile.csv' #Its a file from previous example that is already created. So i am using this file to read
# def reads_csv_file(fn):
#      with open(fn, 'r') as file:
#           csv_file = csv.DictReader(file)
#           l=[]
#           for row in csv_file:
#                x=dict(row)
#                l.append(x)
#           return l
#
#
# print(reads_csv_file(filename))



#------------------------------------------------------------------------------------------------------------------


# 15. Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?


#Ans:

# class Customer:
#      category = 'Nepali'
#      def __init__(self,fullname,DOB,gender,permanent_address,temporary_address,citizenshipno,ppsize_photo,phone_number,
#                   signature,email,account_number,account_type, *args):
#
#           #attributes
#           self.fullname =fullname
#           self.DOB = DOB
#           self.gender = gender
#           self.permanent_address = permanent_address
#           self.temporary_address = temporary_address
#           self.citizenshipno = citizenshipno
#           self.ppsize_photo = ppsize_photo
#           self.phone_number = phone_number
#           self.signature = signature
#           self.email = email
#           self.account_number = account_number
#           self.account_type = account_type
#
#      #methods
#
#      def can_deposit_money(self):
#           money=1000
#           return money
#
#      def can_withdraw_money(self):
#           pass
#
#      def can_open_account(self):
#           pass
#
#      def cam_issue_check(self):
#           pass
#
#      def can_do_transactions(self):
#           pass
#
#
# a=Customer('Ram','','','','','','','','','','','')
# print(a.fullname)
# print(a.can_deposit_money())


# ------------------------------------------------------------------------------------------------------------------


# 16. Imagine you are creating a Super Mario game. You need to define a
# class to represent Mario. What would it look like? If you aren't familiar
# with SuperMario, use your own favorite video or board game to model
# a player


#Ans:

# class Mario:
#      def __init__(self):
#           self.name = "Mario"
#           self.costume="type1"
#
#
#      def can_jump(self):
#           pass
#
#      def can_walk(self):
#           pass
#
#      def can_run(self):
#           pass
#
#      def can_use_items(self):
#           pass
#
#      def can_throw_items(self):
#           pass
#
#      def can_earn_coins(self):
#           pass




# ------------------------------------------------------------------------------------------------------------------


# 17. Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.


#Ans:

# import sys
#
# # error handling for input that doesn't cleanly convert to numbers
# try:
#      x = float(input("Enter first number:"))
#      y = float(input("Enter second number:"))
#      o = input("Enter operator:")
# except Exception :
#      print("Enter valid number")
#      sys.exit(1)
#
#
# #Basic Calculator
# def calculator(n1,n2,op):
#      if n2==0 and op == '/':
#           return "Math error: Number can't be divided by 0"
#      else:
#           if op == "+":
#                return n1 + n2
#           elif op == "-":
#                return n1 - n2
#           elif op == "*":
#                return n1 * n2
#           elif op == "/":
#                return n1 / n2
#           else:
#                return "Invalid operator. Please select '+,-,* or /'"
#
#
# print(calculator(x,y,o))



# ------------------------------------------------------------------------------------------------------------------


# 18. Find a package in the Python standard library for dealing with JSON.
# Import the library module and inspect the attributes of the module.
# Use the help function to learn more about how to use the module.
# Serialize a dictionary mapping 'name' to your name and 'age' to your
# age, to a JSON string. Deserialize the JSON back into Python.


#Ans:

# import json
#
# data={ 'name':'ram', 'age': 40}
#
# #Serializing
# json_string = json.dumps(data, indent=2)
# print(json_string)
#
#
# #Deserializing
# python_string = json.loads(json_string)
# print(python_string)


# ------------------------------------------------------------------------------------------------------------------


# 19. Write a Python class to find validity of a string of parentheses, '(', ')',
# '{', '}', '[' and ']. These brackets must be close in the correct order, for
# example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid


#Ans:

# class Brackets:
#
#     def is_valid(self, s):
#         d = {'(': ')', '{': '}', '[': ']'}
#         l = []
#         for i in s:
#             if i in d:
#                 l.append(d[i])
#             elif not l or i != l.pop():
#                 return False
#         return not l
#
#     # print(is_valid('{{{'))
# a=Brackets()
# print(a.is_valid('()[]'))
# print(a.is_valid('({[)]'))




# ------------------------------------------------------------------------------------------------------------------

# 20. Write a Python class to find the three elements that sum to zero from
# a list of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]


#Ans:

# class Zero:
#     def sum_zero(self, l):
#         l=sorted(l)
#         result = []
#         i = 0
#
#
#         while i < len(l)-2:
#             j=i+1
#             k= len(l) -1
#             while j < k:
#                 if l[i] + l[j] + l[k] < 0:
#                     j= j+1
#                 elif l[i] + l[j] + l[k] >0:
#                     k=k-1
#                 else:
#                     result.append([l[i], l[j], l[k]])
#                     j = j+1
#                     k =k-1
#                     while j<k and l[j] == l[j-1]:
#                         j=j+1
#                     while j<k and l[k] == l[k+1]:
#                         k=k-1
#             i=i+1
#             while i<len(l)-2 and l[i]==l[i-1]:
#                 i=i+1
#         return result
#
# a=Zero()
# print(a.sum_zero([-25, -10, -7, -3, 2, 4, 8, 10]))



