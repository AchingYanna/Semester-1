#PRACTICAL 3: TO FIND ALL PRIME NUMBERS TILL 'N' (without functins)

n = int(input("Enter the total nnumber: "))

prime = [True] * (n + 1)

for p in range(2, n + 1):
    if prime[p]:
        print(p, end=" ")
        for i in range(p * p, n + 1, p):
            prime[i] = False
