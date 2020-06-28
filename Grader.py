#Grader
#A regular polygon has n number of sides. Each side has length s.
#The area of a regular polygon is:  0.25∗n∗s2/tan(π/n)
#The perimeter of a polygon is: length of the boundary of the polygon
#Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

'''
n = Number of sides, must be greater than 2
s = Lenght of the sides, must be greater than 0
'''

def polysum(n,s):
#importing library math
    import math
#calculate area
    a = (0.25 * n * s * s)/math.tan(math.pi/n)
#calculate perimeter
    p = s*n
#sum area and square of the perimeter
    r = a + (p*p)
#returning result rounded to 4 decimals
    return round(r,4)