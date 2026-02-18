# FOR iSpot <- numItems ... 0
#   FOR iCheck <- 0 ... iSpot - 1
#       IF array[iSpot] < array [iCheck]
#           swap( array[iSpot], array[iCheck] )

data = [3, 11, 19, 3, 7, 99, 6, 3, 17]
length = len(data)

print(f"{'Row Name':<10}, {'i':>5}, {'j':>5}, {'Data':>20}")    # Header

for i in range(length-1, 0, -1):
    for j in range(i):
        if data[i]< data[j]:
            data[i],data[j] = data[j], data[i]
        print(f"{'Row 1':<10}  {i:>5}  {j:>5}  {data}")                    


print(data)