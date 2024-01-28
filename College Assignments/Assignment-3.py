'''
F21C26
Prathamesh Kamble
Assignment-3 To calculate minimum,maximum,sum and average using list
'''

print("\nPerforming operations using list:")
list=[13,57,34,52,12,28,10,91,17]
print("List=",list)

print(list[5])

list.append(29)
print("After appending 29 list is=",list)

list.insert(5,35)
print("After inserting 35 list is=",list)

list.remove(34)
print("After removing 34 list is=",list)

print("\nSum of the elements present in the list is=",max(list))

print("\nMinimum number in the given list=",min(list))

print("\nMaximum number in the given list is=",max(list))

print("\nTotal numbers present in list=",len(list))

average=sum(list)/len(list)
print("\nAverage of the given list is=",average)