"""
Waterline calculation using the implementation of integral

Author : Akram Faisal

Simple method to calculate the area of waterline (WL) using simpson (1/3) formula
"""

def simps(array,h):

    array_result = []

    if h % 2 == 0:
        if len(array) >= 3:

            for i in range (0, len(array) - 1):
                if (i+1) % 2 != 0:
                    odd = 1 * array[i]
                    array_result.append(odd)
                even = 4 * array[i]
                array_result.append(even)
    
    result = 1/3 * h * sum(array_result)
    
    if h % 2 != 0:
        print("Step must be an even number")

    if len(array) < 3:
        print("Minimum y (ordinate) is 3")


    return result

a = simps([2,3,5], 2)
print(a)