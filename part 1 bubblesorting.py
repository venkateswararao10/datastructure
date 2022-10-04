def bubblesorting():
       global l
       for i in range(len(l)):
        for j in range(len(l)-i-1): # time complexity=o(n^2)
            if l[j]>l[j+1]:
                l[j], l[j+1]=l[j+1],l[j]
size=int(input("enter size"))
l=list()
i=0
while(i<size):
    ele=int(input("enter no"))
    l.append(ele)
    i=i+1
bubblesorting()
print(l)
#time complexity=o(n^2)
#space complexity=o(n^2)
