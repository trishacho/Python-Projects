import numpy as np

rows_cols = "7 5"
split = rows_cols.find(" ")
rows = int(rows_cols[: split])
columns = int(rows_cols[(split+1) :])

array1 = "1 7 4 9 2 0 17 8 7 2 5 7 1 9 0 3 6 32 37 1 4 7 8 2 4 9 1 2 4 7 2 9 5 3 2"
array2 = "2 7 4 9 2 1 12 8 0 2 5 7 2 9 0 3 4 32 22 1 4 3 8 2 5 8 2 3 4 7 2 2 5 8 2"
array3 = "9 5 3 1 7 38 2 0 57 1 23 5 9 1 2 3 6 9 20 3 0 5 3 2 9 56 73 2 8 7 1 2 3 9 4"

array1 = [int(x) for x in array1.split(' ')]
array2 = [int(x) for x in array2.split(' ')]
array3 = [int(x) for x in array3.split(' ')]
    
a1 = np.reshape(array1, (rows, columns))
a2 = np.reshape(array2, (rows, columns))
a3 = np.reshape(array3, (rows, columns))

print(a1)
print(a2)
print(a3)
    
i = 0
j = 0
total = 0
while(i < rows and j < columns):
    first = a1[i][j]
    second = a2[i][j]
    third = a3[i][j]
    print("position rn:", i, j)
    minVal = min(first, second, third)
    print("minimum value:", minVal)
    total = total + minVal
    print("total rn:", total)
    if(i+1 < rows and j+1 < columns):
        val1 = a1[i][j+1]
        val2 = a1[i+1][j]
        val3 = a2[i][j+1]
        val4 = a2[i+1][j]
        val5 = a3[i][j+1]
        val6 = a3[i+1][j]
        print("all values:", val1, val2, val3, val4, val5, val6)
        maxVal = max(val1, val2, val3, val4, val5, val6)
        print("max value:", maxVal)    
        if(maxVal == val1):
            if(val1 == val2 or val1 == val3 or val1 == val4 or val1 == val5 or val1 == val6):
                i += 1
                j += 1
            else:
                j += 1
        elif(maxVal == val2):
            if(val2 == val1 or val2 == val3 or val2 == val4 or val2 == val5 or val2 == val6):
                i += 1
                j += 1
            else:
                i += 1
        elif(maxVal == val3):
            if(val3 == val1 or val3 == val2 or val3 == val4 or val3 == val5 or val3 == val6):
                i += 1
                j += 1
            else:
                j += 1
        elif(maxVal == val4):
            if(val4 == val1 or val4 == val2 or val4 == val3 or val4 == val5 or val4 == val6):
                i += 1
                j += 1
            else:
                i += 1
        elif(maxVal == val5):
            if(val5 == val1 or val5 == val2 or val5 == val3 or val5 == val4 or val5 == val6):
                i += 1
                j += 1
            else:
                j += 1
        elif(maxVal == val6):
            if(val6 == val1 or val6 == val2 or val6 == val3 or val6 == val4 or val6 == val5):
                i += 1
                j += 1
            else:
                i += 1
    else:
        break
print(total)
