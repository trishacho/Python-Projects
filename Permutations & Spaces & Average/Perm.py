string1 = "potter"
string2 = "pretto"

if(len(string1) != len(string2)):
    print("No it is not.")
else:
    sortString1 = sorted(string1)
    sortString2 = sorted(string2)
    if(sortString1 == sortString2):
        print("Yes it is.")
    else:
        print("No it is not.")
