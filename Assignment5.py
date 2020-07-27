#1) Sort the list in increasing order and zeroes should be at right hand side.

"""
list1=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
list1.sort()
list1.extend((0,0,0,0,0,))
del list1[0:5]
print(list1)
"""

List = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
List.sort()
c=List.count(0)
print(List[c:]+List[:c])


#2) Merge two lists & produce one sorted list .
list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]
list3=list1+list2
list4=[]
for num in range(5,81):
  if num in list3:
        list4.append(num)
# print(list4)
