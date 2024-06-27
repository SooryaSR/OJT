#while loop
i = 2
while i < 8:
    print(i)
    i += 1
#-----------------------------#

#program to add natural numers upto 
#add = 1+2+3+....+n
n = 20
add = 0
i = 1 #counter value
while i <= n:
    add = add + i
    i = i+1 #counter updated
print("Thw sum is",add)

#-----------------------------------#   

#break statement

a=10
while a>0:
    a-=1
    if (a!=5):
        print(a)
    else:
        break
#--------------------#

for a in "python":
    if a == "h":
        break
    print(a)
print("loop ends")
#-----------------------------#

#continue statement

a=10
while a>0:
    a-=1
    if(a!=5):
        print(a)
    else:
        continue #skip 5 and loop is on iteration


#---------------------------------#

for a in "Python":
    if a == "h":
        continue
    print(a)
print("Loop ends")

#-------------------------------#

# #PASS
# v1={'p','a','s','s'}
# for v in v1:
#     pass

# Printing table of given number.
num=int(input("Enter a Number : ")) 
i=1 
while(i<=10): 
 print(num*i) 
 i=i+1 

#--------------------#

#Printing reverse of a number.
num = int(input("Enter a Number : ")) 
rev = 0 
while(num != 0): 
 rem = num % 10 
 rev = rev * 10 + rem 
 num = int(num / 10) 
print(rev) 
    
