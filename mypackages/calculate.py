def iseven(num):
    ''' This function checks if the number is even or not and returns the boolean value'''
    if(num%2==0):
        return(True)
    else:
        return(False)

def factorial(num):
    ''' This fucntion calculates the factorial of the given number'''
    if(num >= 0):
        if (num == 0):
            return 1
        else:
            return (num * factorial(num - 1))
    else:
        return("Error: Number should be a positive number")

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

def words_count(arr):
    '''This function  returns the dictionary of words with its count
        input: array of strings
        output: dictionary of keys = word, value = count of that word'''
    dict = {}
    for i in arr:
        for j in i.split():
            dict[j] = dict.get(j,0) + 1
    return dict



