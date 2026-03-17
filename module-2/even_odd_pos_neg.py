num = int(input())
inp = input()
even = odd =  pos = neg = 0
numbers = [int(x) for x in inp.split()]
for i in range(num):
    if numbers[i]%2!=0:
        odd+=1
    elif numbers[i]%2==0:
        even+=1
        
    if numbers[i]>0:
        pos+=1
    elif numbers[i]<0:
        neg+=1

print("Even:",even)
print("Odd:", odd)
print("Positive:", pos)
print("Negative:", neg)
