N = int(input("Enter a number: "))
c = 0
i = 1
while(i <= N):
    if(N % i== 0):
        c += 1
    i += 1
if (c == 2):
    print("Prime number.")
else:
    print("Not a prime number.")