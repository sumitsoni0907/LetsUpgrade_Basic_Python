# remove all the occurrences of element from a list.

li = [int(i) for i in input("enter values:").split()]     # take input for list from users.
find = int(input("enter number:"))        # ask the user to enter number to deleting all occurrence number.

for i in li:                        # taking loop for finding of all occurrence in list
  if(i == find):                
    li.remove(i)     # occurrence found then remove from list.
    
print(li)     # print the list

"""
input:

enter values:2 5 8 2 57 51 2 87 2 96 58 2 4 3 5 2 10 2 47 2
enter number:2

Output:

[5, 8, 57, 51, 87, 96, 58, 4, 3, 5, 10, 47]

"""
