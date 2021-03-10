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

filename = 'myfile'
list_of_tuples = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',
21)]
def csv_func(s, l):

    empty=[]
    for i in list_of_tuples:

        li=list(i)
        empty.append(li)

        # for j in li:
        #     print(j, end=',')
    #     empty.append(li)
    #
    # print(empty)
    # for i in empty:
    #     print(i)

    for i in empty:
        for j in i:
            x=print(j, end=',')
            




csv_func(filename,list_of_tuples)









