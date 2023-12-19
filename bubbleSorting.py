
numlist = [2,3,1,9,0]

size = len(numlist) # 5

for i in range(size-1): # 3
    for j in range(size-1-i):  # 1
        if numlist[j] > numlist [j+1]:    # numlist[0] > numlist [1]
            numlist[j] , numlist [j+1] = numlist[j+1] , numlist [j]



[2,3,1,9,0] # j = 0 , i = 0

[2,1,3,9,0] # j = 1, i = 0

[2,1,3,9,0] # j = 2, i = 0

[2,1,3,0,9] # j = 3, i = 0



[1,2,3,0,9] # j = 0 , i = 1

[1,2,3,0,9] # j = 1, i = 1

[1,2,0,3,9] # j = 2, i = 1



[1,2,0,3,9] # j = 0, i = 2

[1,0,2,3,9] # j = 1, i = 2



[0,1,2,3,9] # j = 0, i = 3




