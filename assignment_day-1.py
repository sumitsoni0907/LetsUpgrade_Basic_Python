#Take input for a list and sort it in descending order.

li = [int(i) for i in input("Enter the values").split()]    # taken input from user to enter values  
li.sort()      # sorted list Ascending order
li.reverse()    # reverse the list that give descending order
print(li)   # print the list


#Input:
#Enter the values: 88 41 25 47 36 20 10 11 43 88 75 52 30 25 2 81 70 99 

#Output:
#[99, 88, 88, 81, 75, 70, 52, 47, 43, 41, 36, 30, 25, 25, 20, 11, 10, 2]
