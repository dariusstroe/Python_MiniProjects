import random
import time

def BasicSearch(l,target):
    #scan entire list, look for equality to target
    #if yes, return index; else return -1

    for i in range(len(l)):
        if l[i]==target:
            return i
    return -1

def BinarySearch(l, target,low=None,high=None):
    #list needs to be SORTED; divide and conquer

    if low is None:
        low=0
    if high is None:
        high=len(l)-1
    middle=(low+high)//2

    if high<low:
        return -1

    if l[middle]== target:
        return middle
    elif target<l[middle]:
        return BinarySearch(l,target,low,middle-1)
    else:
        #target>l[middle]
        return BinarySearch(l,target,middle+1,high)

if __name__=="__main__":
    #list=[1,3,5,10,18,19,23,28,32,40,42,50,77]
    #target=32
    #print(BasicSearch(list,target))
    #print(BinarySearch(list,target))

    length=10000
    sortedList=set()
    while len(sortedList) < length:
        sortedList.add(random.randint(-3*length,5*length))
    sortedList=sorted(list(sortedList))

    start=time.time()
    for target in sortedList:
        BasicSearch(sortedList,target)
    end=time.time()
    print("Basic search time is: "+str((end-start)))

    start=time.time()
    for target in sortedList:
        BinarySearch(sortedList,target)
    end = time.time()
    print("Binary search time is: "+str((end-start)))