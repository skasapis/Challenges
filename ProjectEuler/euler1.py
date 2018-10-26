sum = 0 #initialization
for i in range(0,1000): #would be 1:1000 (notice python starts count from 0)
    if (i%3==0) or (i%5==0): #% is the matlab mod function
        sum = sum + i #sum+=i is a different way to write sum = sum+1
    #notice there in no "end" in python
#notice there in no "end" in python
print(sum) #print outcome
