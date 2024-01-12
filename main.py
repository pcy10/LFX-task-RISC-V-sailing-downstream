# creating an empty list
lst = []
v = []
# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())
	lst.append(ele)


if n % 10 != 0 :
   print("Error: total number of input is not a muliple of 10")
else:
   for i in range(0, n):
       if (i%2) and (i%3):
           v.append(lst[i])
   print("Here is the modified list assuming 0 based positioning in list")
   for i in range( 0, len(v)):
       print( v[i])

    
   
   
   

