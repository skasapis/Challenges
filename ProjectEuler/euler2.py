prev, cur = 0,1
sum = 0
while cur <=4000000:
    prev, cur = cur, prev+cur
    if cur % 2 == 0:
         sum += cur
print(sum)
