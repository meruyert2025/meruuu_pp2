#SETS
'''

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)




thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)



set1 = {"abc", 34, True, 40, "male"}
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)





thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)




thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)



thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)





thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)



thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)




thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)



set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)






set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)





set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)







set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)






set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)         # биригу
print(set3)







set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2              #биригу
print(set3)        






set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)        #биригу
print(set1)





set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)            #биригу

print(set3)







set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)







set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)







set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)







set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)





set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)





copy()	 	Returns a shallow copy	
difference()	-	Returns a new frozenset with the difference	
intersection()	&	Returns a new frozenset with the intersection	
isdisjoint()	 	Returns whether two frozensets have an intersection	
issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another	
issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	^	Returns a new frozenset with the symmetric differences	
union()	|	Returns a new frozenset containing the union








'''
