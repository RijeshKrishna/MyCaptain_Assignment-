string=input("String : ")
c = {}   
for i in string:
    if i in c:
        count[i] += 1
    else:
        count[i] = 1
print("Count of Characters: ",c)
