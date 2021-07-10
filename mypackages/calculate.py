# import all the required fucntions
import math

# Even or Odd
def is_even(num):
    ''' This function checks if the number is even or not and returns the boolean value'''
    if(num%2==0):
        return(True)
    else:
        return(False)

# Factorial
def factorial(num):
    ''' This fucntion calculates the factorial of the given number'''
    if(num >= 0):
        if (num == 0):
            return 1
        else:
            return (num * factorial(num - 1))
    else:
        return("Error: Number should be a positive number")

# Multiplication Table
def mul_table(num,start=1,end=10):
    '''This function prints the table of the numbe
        arguments:
        num: the number for which you want the table
        start: the start index of the table
        end: the end index of the table

        output: multiplication table'''

    for i in range(start,end+1):
        print("{} x {} = {}".format(num,i,num*i))
    return

# Factors
def factors(num):
    '''This function returns the list of factors of the given number
        input: int->number
        output: list of all factors'''
    import  math
    i = 1
    list = []
    while i <= math.sqrt(num):
        if(num%i == 0):
            if(int(num/i) == i):
                list.append(i)
            else:
                list.append(i)
                list.append(int(num/i))
        i +=1
    return sorted(list)

# Prime number functions

def find_prime(num,start=2):
    '''This function will find the prime numbers upto given number
        input: int->number
               start : start position
               end: ending position

        output: array of numbers'''
    list = []
    end = num
    for i in range(start,end+1):
        if(is_prime(i)):
            list.append(i)
    return list


def is_prime(num):
    '''This fucntion returns True if the number is prime else returns False
        input: int->num
        output: bool'''
    if(num == 2 or num == 3):
        return(True)
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i == 0):
            return(False)
    return(True)

def prime_factors(n):
    '''This function finds the factors of a  prime number
        input: prime nubmer
        output: array of factors of that given prime number'''

    list = []
    while n%2 == 0:
        list.append(2)
        n = int(n/2)
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i == 0):
            list.append(i)
            n = int(n/i)
    if n>2:                         #Check if the number remaining is a prime, if yes add to list
        list.append(n)
    return list

# LCM and HCF
def hcf(a,b):
    '''This function calculates the highest common factor from the two values
        input:
        int -> num1, int-> num2
        output: int -> highest commom factor of the two values'''
    # We will use recursion to find the value
    if(b==0):       # Base Condition
        return a
    return hcf(b,a%b)

def lcm(a,b):
    '''This fucntion calculates the lowest common multiple of the two numbers
        input:
        int -> num1, int-> num2
        output: int -> highest commom factor of the two values'''
    calc_hcf = hcf(a,b)             # Calculate the hcf
    return(int((a*b)/calc_hcf))     # LCM = (n1 x n2)/hcf

#String function
def words_count(arr):
    '''This function  returns the dictionary of words with its count
        input: String
        output: dictionary of keys = word, value = count of that word'''
    dict = {}
    list = []
    list.append(arr)
    for i in list:
        for j in i.split():
            dict[j] = dict.get(j,0) + 1
    return dict




