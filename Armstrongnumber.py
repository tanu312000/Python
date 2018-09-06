n=int(input("Enter number"))
x=n
s=0
while(n>0):
    r=n%10
    s=s+r**3
    n=n//10
    print(s)

if(s==x):
    print("Number is Armstrong")

else:
    print("Number is not Armstrong")

