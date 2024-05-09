myList = ["1",2,3,"4",5,6,"7",8,9]
# print(myList)
# print(type(myList))
# print(myList[1])
# [a,b,*c]=myList
# print(a,b,c[-1][0])
# x=c[-1]
# print(x)
# x.append("987")
# print(x)
# x.append(156)
# print(myList)
# print(myList[:5])
# myList[2:4]=["Hamza","Manzoor","Alice"]
print(myList)
# myList.insert(1,"Hamza")
# a=['a','b','c','d','e','f','g','h','i']
# myList.extend(a)
# myList.remove(2)
# myList.remove(myList[-1])
# del myList[-1]
# myList.pop()
# myList.clear()
# print(myList)
# for x in myList:
#     print(str(x)+'10')
# sum=0
# for x in range(1,100+1):
    # a=sum(x)
# print('sum',sum(range(1,100+1)))
# print(sum(1+5))
# a=1
# for x in range(1,10+1):
#     a*=int(x)
# print('a',a)
def findPrime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True
print(findPrime(4))
sum=0
for x in range(2,102):
    if(findPrime(x)==True):
        sum+=1/x

print("sum",sum)
# 1/3+1/5+1/7+1/11+1/13+1/17...+1/101
    
