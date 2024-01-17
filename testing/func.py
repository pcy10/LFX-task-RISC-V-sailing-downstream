def siz(n):
    if n%10 == 0 :
        return 1
    else:
        return 0
    
    
def printt(lst, n):
    v = []
    for i in range(1, n+1):
        if (i%2) and (i%3):
            v.append(lst[i-1])
     
    print("Here is the modified list assuming 1 based positioning in list")
    for i in range( 0, len(v)):
        print( v[i])
        
    ln = len(v) 
    return ln 
    
        
  
    

# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of input in array: "))

# iterating till the range
for i in range(0, n):
	ele = int(input())
	lst.append(ele)


ot = siz(n)
if ot == 0 :
    print("Error: total number of input is not a muliple of 10")

else:
    printt(lst, n)
   
       
           
   
   
       

    
   
   
   

