#PRACTICAL 4: TO FIND PRIME NUMBERS till n

n = int(input("Enter the range of nnumbers: "))

prime = [True] * (n + 1)

for p in range(2, n + 1):
    if prime[p]:
        print(p, end=" ")
        for i in range(p * p, n + 1, p):
            prime[i] = False
