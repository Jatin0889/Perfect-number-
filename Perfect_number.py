# WAP to find the perfect number
#A perfect number is a positive integer that is equal to the sum of all its proper divisors, excluding itself.

# for example = 6. Proper divisors of 6: 1,2,3:1+2+3=6 So, 6 is a perfect number.

sum = 0 
n = int (input("enter your number:"))
for i in range(1,n-1,1):
    if( n % i == 0):
        sum = sum + i
if (sum == n):
    print("perfect")
else:
    print("not perfect")
