def sumOfLastRow(s, d, r):
    total = str(s)
    dstring = str(d)
    numOfValues = 0
    arrOfValues = []
    arrOfValues.append(s)
    
    #get number of values in each pyramid
    for x in range(r):
        numOfValues = numOfValues + (r-x)
    
    #add octal numbers together and add sum to an array
    for x in range(1, numOfValues):
        total = oct(int(total, 8) + int(dstring, 8))
        arrOfValues.append(int(total[2:]))
    
    finalSum = 0
    length = len(arrOfValues)
    for x in range(r):
        element = arrOfValues[length - x - 1]
        
        #get individual digits
        separated = [int(y) for y in str(element)]
        
        #add individual digits to finalSum
        for i in separated:
            finalSum = finalSum + i
    
    return finalSum        
   
