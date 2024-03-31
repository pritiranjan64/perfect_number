#----------------------------using for loop---------------------------
#check given numbers is perfect or not
n=int(input('enter the values of n:'))
sd=0
for i in range(1,n//2+1):
    if n%i==0:
        sd+=i
if sd==n:
    print('perfect number')
else:
    print('not a perfect number')  


#-------------------------using while loop----------------------------
#print given number is perfect or not by using while loop.
n=int(input())
sd=0
i=1
while i<(n//2+1):
    if n%i==0:
        sd+=i
    i+=1
if n==sd:
    print('perfect number')
else:
    print('not a perfect number')        


