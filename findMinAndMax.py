d = [1, 3, 16, 25, 67, 8, 20]

def findMinAndMax(L) :
    if L == [] :
        return (None, None)
    else :
        a = L[0]
        b = L[0]
        for num in L :
            if num < a :
                a = num
        for num in L :
            if num > b :
                b = num
        return (a, b)

print (findMinAndMax(d))
