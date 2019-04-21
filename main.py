from quick_sort import quick_sort_hoare, quick_sort_lomuto
from merge_sort import merge_sort

a = [5,4,3,2,1,2,3,4,5]
b = a.copy()
c = a.copy()
quick_sort_lomuto(a)
print(a)
quick_sort_hoare(b)
print(b)
merge_sort(c)
print(c)

a = [1,2,3,4,5,6,7,8,9]
print(a[5:6])
