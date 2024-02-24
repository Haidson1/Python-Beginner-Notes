
multidimension = [
    [1,2,3], # Row 0
    [4,5,6], # Row 1
    [7,8,9]  # Row 2
]
print(multidimension[1][1]) #Will output "5" (Second list, 1st index)


# --------- Going through the whole multidimensional array ---------
for array in multidimension:   # [] = Array
    for index in array:        # 1,2,3 = index
        print(index)
