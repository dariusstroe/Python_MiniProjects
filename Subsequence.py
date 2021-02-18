array=[5,7,2,9,0,18]
sequence=[5,9]

def isSubsequence(array,sequence):
    sequenceIndex=0
    for value in array:
        if(sequence[sequenceIndex]==value):
            sequenceIndex+=1
        if(sequenceIndex==len(sequence)):
            break
    return sequenceIndex==len(sequence)

print(isSubsequence(array,sequence))