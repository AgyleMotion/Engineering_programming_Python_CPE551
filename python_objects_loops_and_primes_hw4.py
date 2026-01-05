import copy

def objects(a):
    # The variable a represents a list.
    # You are given a = [1,2,[3,4,5]]
    # The variable b also represents a list.
    # The list b is a copy of list a.
    # Both list a and list b should have the same id address.
    
    # Write the Python statement which will result in list b being a
    # copy of list a, with list a and list b having the same id address.
    # ENTER ANSWER BELOW.
    b = a 
    

    # Assign a shallow copy of the list a to the variable c.
    # (Variable c is a list and is a shallow copy of list a).
    # ENTER ANSWER BELOW.
    c = copy.copy(a)


    # Assign a deep copy of the list a to the variable d.
    # ENTER ANSWER BELOW.
    d = copy.deepcopy(a)
    
    # Assign the id of list a to the variable id_a
    # ENTER ANSWER BELOW.
    id_a = id(a)

    return b, c, d, id_a


# -----------------------------------------------------------------------------------------------------------------
"""
Write a function prime_number(number). 
This function will return a list of all the prime numbers
from 2 up to but not including the variable number.
Please refer to the sample outputs given below.

Example1:
        prime_number(10)
        Output:[2,3,5,7]
Example2:
        prime_number(100)
        Output:[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
Example3:
        prime_number(7)
        Output:[2,3,5]
"""

#PLEASE COMPLETE THE FOLLOWING PROGRAM.

def prime_number(number):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):  
            if n % i == 0:
                return False
        return True

    return [x for x in range(2, number) if is_prime(x)]

# -----------------------------------------------------------------------------------------------------------------
"""
Write a function while_loop(number). The variable
number is a string.

*If the character in the string is a number, the function
returns the sum of all integer numbers between 1 and
number inclusive. Please refer to the sample output
below:
Example1:
        while_loop("3")
        Output: 6
        Explanation: 3 + 2 + 1 = 6

*If the character in the string is not a number, (or not an integer
number) the function returns the string "Error". Please refer to the
sample output below:
Example2:
        while_loop("Hello")
        Output: "Error"
        Explanation: Chracters in the string are not numbers.
        Hint: You may want to consider using a try statement with an except statement.

*If the character in the sting is a number less than one, the function
returns the number zero as a default. Please refer to the sample
output below:
Example3:
        while_loop("-1")
        Output: 0
        Explanation: The number in the string is less than one. The defaul of zero is returned.
        
"""
#PLEASE COMPLETE THE FOLLOWING PROGRAM.

def while_loop(number):
    try:
        num = int(number)
        if num < 1:
            return 0
        total = 0
        i = 1
        while i <= num:
            total += i
            i += 1
        return total
    except ValueError:
        return "Error"
