'''
1. Character Count:
given a string count each letter in the string and then print the result.

Example 1:
character_count('banana')

Input: 'banana'
Output (in the console): 
the character b occurs 1 times
the character a occurs 3 times
the character n occurs 2 times
'''

def character_count(string):
  count_dict = {}
  # iterate characters
  for char in string:
    # when a character is in the table, increment its value
    if char in count_dict:
      count_dict[char] += 1
    # otherwise add character to table with a value of 1
    else:
      count_dict[char] = 1
  # iterate once to print characters
  for char in count_dict:
    print(f'the character {char} occurs {count_dict[char]} times')

# def character_count(string):
#   # iterates through the string
#   for i in string:
#     if string.count(i) == 1:
#       print(f"the character {i} occurrs {string.count(i)} times")
#     else:
#       print(f"the character {i} occurrs {string.count(i)} times")
      
character_count("banana")
character_count("hello world")