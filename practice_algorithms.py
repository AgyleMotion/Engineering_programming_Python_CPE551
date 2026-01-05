"""
QUESTION 1:
========================================================================================================
Given a list of numbers, write a function to find the maximum number in the list.
Do Not Use the built-in Python function max.
Note: For the purpose of this problem, we define that an empty list will return None.

NOTE: DO NOT USE THE PYTHON FUNCTION max. WRITE your program using a loop. 

Example 1:
========================================
Input: [10, 5, 20, 15, 25]
Output: 25

Example 2:
========================================
Input:[10,10,10]
Output: 10

Example 3:
========================================
Input: []
Output: None
"""

def find_maximum(numbers):
    if numbers == []:
        return None
    max = numbers [0] 
    for i in numbers:
        if i > max:
            max = i      
    return max



"""
QUESTION 2: 
========================================================================================================
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Write a function named generateParenthesis that takes an integer as an input and returns a list of strings 
as an output. Note that you can define a function inside a function if necessary.

Example 1:
========================================
Input: 0
Output: ['']

Example 2:
========================================
Input: 1
Output: ['()']

Example 3:
========================================
Input: 2
Output: ['(())', '()()']

Example 4:
========================================
Input: 3
Output: ['((()))', '(()())', '(())()', '()(())', '()()()'])
"""

def generateParenthesis(n):
    
    def helper(current, i, j):
        if len(current) == 2 * n:
            L.append(current)       
        if i < n:
            helper(current + '(', i + 1, j)
        if j < i:
            helper(current + ')', i, j + 1)
    L = []
    if n == 0:
        return ['']
    else:
        helper('', 0, 0)
    return L


"""
QUESTION 3: 
========================================================================================================
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome. Write a function
named isPalindrome that takes a string as an input and returns a bool as an output.

Hint: refer to the following example on how to reverse a string.

>>> S = "abc"
>>> S[::-1]
'cba'


Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true

Explanation:
After removing non-alphanumeric charactors and ignoring cases, the input is:  amanaplanacanalPanama
which reads the same as backward and forward, so it is true.

Example 2:
=========================================
Input: "race a car"
Output: false

Explanation:
After removing non-alphanumeric charactors and ignoring cases, the input is:  raceacar
which does not read the same as backward and forward, so it is false.
"""

def isPalindrome(x):
    string = ''
    p = (string.join([c for c in x if c.isalnum()])).lower()
    return p == p[::-1]

    
