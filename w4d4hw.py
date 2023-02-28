# You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square
# If it is a square, return its area. If it is a rectangle, return its perimeter.

# Example(Input1, Input2 --> Output):

# 6, 10 --> 32
# 3, 3 --> 9
# Note: for the purposes of this kata you will assume that it is a square if its length and width are equal, otherwise it is a rectangle.
def area_or_perimeter(l , w):
    if(l != w):
        return (l+w)*2
    return l*w
# currently I think it's O(1) because only two inputs are allowed, meaning more shouldn't be considered. If more than two inputs were allowed I think it would be O(n)?

# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

# Examples
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
# Notes
# The number can be negative already, in which case no change is required.
# Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
def make_negative( number ):
    if number == 0:
        return number
    elif number <= 0:
        return number
    else:
        return number - (number * 2)
# O(n)
    
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
def remove_char(s):
    s = s[:-1]
    s = s[1: ]
    return s
# I think its O(1) because it doesn't matter what or how many characters are put in the sting, the process and the amount of time it takes doesn't change