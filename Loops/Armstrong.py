N = int(input('Enter a number: '))
sum = 0
temp = N
while temp > 0:
    r = temp % 10
    sum += r ** 3
    temp //= 10
if N == sum:
    print(N," is an amstrong number")
else:
    print(N," is not an amstrong number")