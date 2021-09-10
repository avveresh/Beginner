# хранятся только уникальные значения
set1 = {1,2,3,4,5} # множество, изменяемый тип данных
set3 = {1,3,5,7,9,}
list1 = [1,1,2,2,3,3,3]
set2 = set(list1)
tuple2 = tuple(list1)
y = type (tuple2)
set4 = set1.intersection(set3)
set5 = set1.union(set3)
print (set2,tuple2,list1,y,set4,set5)