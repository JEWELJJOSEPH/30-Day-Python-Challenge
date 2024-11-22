s=[2,5,22,67,40,11,43,66,34,7]
even=[]
odd=[]
for i in s:
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
print("even no's :",even)
print("odd no's:",odd)

