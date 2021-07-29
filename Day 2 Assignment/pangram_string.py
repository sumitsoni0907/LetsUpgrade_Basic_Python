
# Check whether a string is a pangram or not.

import string          # import string module

str = input("enter sentence:")     # Asking the user to enter sentence.
alphabet = set(string.ascii_lowercase)        # taking all the alphabet from a,b,c,...,z

if((set(alphabet) - set(str)) == set()):          # checking sentence containg all the alphabet
  print("\""+ str + "\"" + " is a pangram string.")     # if yes then print pangram string
else:
  print("\""+ str + "\"" + " is not pangram string.")   # otherwise print not pangram string


"""
Input:

enter sentence:the quick brown fox jumps over the lazy dog

Output:

"the quick brown fox jumps over the lazy dog" is a pangram string

"""
