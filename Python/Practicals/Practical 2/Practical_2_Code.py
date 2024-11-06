#PRACTICAL 2:To find IF n IS PRIME NUMBER

n = int (input("Enter a number: "))


flag = False

if n == 0 or n ==1:
         print(n, "Is not a prime number")


elif n >1:
         for i in range(2,n):
             if(n%1) == 0:
                 flag = True
                 break



         if flag:
             print(n, "is a prime number")

         else:
             print(n, "is not a pime number")
