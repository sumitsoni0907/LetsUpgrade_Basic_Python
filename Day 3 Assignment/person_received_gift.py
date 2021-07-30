"""
Consider a person is represented by Pi, where i is the index of the following list.
A list shows the person to whom person Pi has given the gift.
 
Consider the below example:
gift_presented_to = [2, 1, 5, 3, 4]
 
This list is giving us the following details:
Person P1 has given gift to person P2
Person P2 has given gift to person P1
Person P3 has given gift to person P5
Person P4 has given gift to person P3
Person P5 has given gift to person P4
 
So for the given list, the list of persons from whom they have received the gift would be 
gift_received_from = [2, 1, 4, 5, 3]
 
i.e.
Person P1 has received gift from person P2
Person P2 has received gift from person P1
Person P3 has received gift from person P4
Person P4 has received gift from person P5
Person P5 has received gift from person P3
 
Your task:
 
Take input for the gift_presented_to[] list and print its respective gift_received_from[] list.
"""

gift_presented_to =[int(i) for i in input("gift_presented_to: ").split()]   # take input list from users
gift_received_by = []    # creating a received gift list

for i in gift_presented_to:       #  travarse every elemnts of list    
   gift_received_by.insert(i - 1, gift_presented_to.index(i) + 1)   # generate gift received by whom list

print("gift_ received_from:",gift_received_by)     # print list


#Input - 1:
#gift_presented_to: 2 1 5 3 4

#Output - 1:
#gift_ received_from: [2, 1, 4, 5, 3]

# Input -2:
#gift_presented_to: 3 4 1 5 2

#Output - 2:
#gift_ received_from: [3, 5, 1, 2, 4]
