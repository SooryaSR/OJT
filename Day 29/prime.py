##program to check 
#weather the given number is 
#prime number or not 


num = int(input("Enter a Number : ")) 
i=2; 
while(i<num): 
 if(num%i==0):
  print("%d is not a prime number.."%num)
  break
 i=i+1
else:
 print("%d is a prime number.."%num)
   