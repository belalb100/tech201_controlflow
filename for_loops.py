# Looping

# A for loop is where you define an iterator number and cycle through data (list or dictionary) 'foreach entry' entry in that data structure.

# Creating a for loop.

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]

dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}
#
# for num in list_data:

# #it knows what we are talking about as we have stated it. --- for each instance of data do this thing vvvvvvvvvvvv a.k.a print(num *2)
# # num is used here but use something is related to what you are talking about etc talking about pizza use pizza if talking about students do `for students in etc...`

#     print(num * 2)

# a nested for loop/ to access specific list in the data.

# for data in embedded_lists:
#     print(data) #access to data in 1st part of the list
#     for num in data:
# 2nd for loop is printing them out individually. But we can't do this until we get inside the first list.

#         print(num)

# loops for dictionaries
# # Version 1
# for item in dict_data.values(): # we assign item to a variable, basically.
#     print(item)

# Version 2 more understandable.
#
# for item in dict_data.values(): #loop through this once,
#     for embed_values in item.values():

# before you go on to next dictionary i want you to loop through the item within item and then print them out.
#
#     #it is just giving us the value we want

     # print(embed_values)

for items in dict_data.values():
    print(items["money"])

#-----Loops and if statements

list_1 =[1, 2, 3, 4, 5]

for num in list_1:
    if num == 3:
        print("I found 3") # it will go through all numbers so 1 then 2 then 3 then 4 then 5
    elif num > 3:
        print("Gone too far!")
    else:
        print("Too soon.")