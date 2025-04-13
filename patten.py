
"""

 * * * * * * 
 * * * * * * 
 * * * * * * 
 * * * * * * 
 * * * * * * 
 * * * * * * 
"""
n=int(input("enter rows"))
for i in range(0,n):
    for j in range(0,n):
        print("* ",end="")
    print()


print("_________________________________________")



"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * *

""" 

# n=6
for i in range(0,n):
    for j in range(0,n):
        if i>=j:
            print("* ",end="")
    print()


print("_________________________________________")






"""
 * * * * * * 
   * * * * * 
     * * * *
       * * *
         * *
           *

"""
for i in range(0,n):
    for j in range(0,n):
        if i<=j:
            print("* ",end="")
        else:
            print("  ",end="")
    print()


print("_________________________________________")

"""
 * * * * * *
  * * * * *
   * * * *
    * * *
     * *
      *


"""
# n=6
for i in range(0,n):
    for j in range(0,n):
        if i<=j:
            print("* ",end="")
        else:
            print(" ",end="")
    print()
print("_________________________________________")

"""
* * * * *
*       *
*       *
*       *
* * * * *

"""

for i in range(0,n):
    for j in range(0,n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

print("_________________________________________")

"""
* * * * *
* *     *
*   *   *
*     * *
* * * * *

"""
for i in range(0,n):
    for j in range(0,n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j:
            print("* ",end="")
        else:
            print("  ",end="")
    print()


print("_________________________________________")


"""
* * * * *
* *   * *
*   *   *
* *   * *
* * * * *

"""
for i in range(0,n):
    for j in range(0,n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

print("_________________________________________") 

"""

*       *
* *   * *
*   *   *
* *   * *
*       *


"""

for i in range(0,n):
    for j in range(0,n):
        if  j==0 or j==n-1 or i==j or i+j==n-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()


print("_________________________________________") 


"""
*
* *
*   *
*     *
* * * * *
"""
for i in range(0,n):
    for j in range(0,n):
        if  j==0 or i==n-1 or i==j:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

print("_________________________________________") 


"""
 * * * * *
   *     *
     *   *
       * *
         *
"""
for i in range(0,n):
    for j in range(0,n):
        if  i==0 or j==n-1 or i==j:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

print("_________________________________________") 


"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

"""


for i in range(1,n):
    for j in range(1,n+1):
        print(j,end=" ")
    print()

print("_________________________________________") 



print("_________________________________________")

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""

for i in range(1,n+1):
    for j in range(1,i+1):
        if i>=j:
            print(j,end=" ")
    print()

print("_________________________________________")

"""
 1
 2 3
 4 5 6
 7 8 9 10
 11 12 13 14 15
"""


count=1
for i in range(1,n+1):
    for j in range(1,i+1):
        
            print(count,end=" ")
            count+=1
    print()


print("_______________________________")

for i in range(1,n+1):
    for j in range(1,i+1):
        if i==1 or i==j  :
            print(j,end=" ")
    print()

print("_________________________________")




num = -350
original = num 
sign = -1 if num < 0 else 1
num = abs(num)
rev = 0
while num != 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
rev = rev * sign

print(rev)