#wap which will take the number as a input , and if the no. is even it
# will create a even factorial(8-> 2*4*6..) and if the number is odd(7 -> 1*3*5...) it will create a odd factorial , using functions

n = int(input("Enter the number: "))

def even_factorial(n):
    result = 1
    for i in range(2, n+1, 2):  
        result *= i
    return result

def odd_factorial(n):
    result = 1
    for i in range(1, n+1, 2):  
        result *= i
    return result

if n % 2 == 0:
    print("Even factorial:", even_factorial(n))
else:
    print("Odd factorial:", odd_factorial(n))