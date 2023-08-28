n=input()
b=set(n)
c=0
for i in b:
    if i in "qwertyuioplkjhgfdsazxcvbnm":
        c+=1
print(c)
