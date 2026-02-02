
array = [3, 45, 12, 89, 2, 16]
print(array)

for iSpot in range(len(array)-1, 0, -1):
    for iCheck in range(0, iSpot):
        if array[iCheck] > array[iCheck+1]:
            array[iCheck], array[iCheck+1] = array[iCheck+1], array[iCheck]


print(array)