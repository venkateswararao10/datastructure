def dacpowerno(x,y):
    if y==1:
        return x
    else:
        mid=y//2
        b=dacpowerno(x, mid)
        c=b*b
        if y%2==0:
            return c
        else:
            return c*x
no=int(input("enter a no"))
po=int(input("enter a po"))
ans=dacpowerno(no,po)
print(ans)