import math
#note: requires panda to process the rest of the line! 
import pandas as pd

def mysqrt(a):
    x = a/4
    while True:
        y = (x+a/x)/2
        if abs(y-x) < 0.0001:
            break
        else:
            x = y
    return(y)


numlist = [1,2,3,4,5,6,7,8,9,10]
mysqrtlist = []
mathsqrtlist = []
difflist = []


for i in numlist:
    mysqrtlist.append(mysqrt(i))

for i in numlist:
    mathsqrtlist.append(math.sqrt(i))

for i in numlist:
    difflist.append(abs(mysqrt(i)-math.sqrt(i)))

finaltable = {'a': numlist, 'mysqrt(a)': mysqrtlist, 'math.sqrt(a)': mathsqrtlist, 'diff': difflist}
ft = pd.DataFrame(finaltable,columns=['a','mysqrt(a)','math.sqrt(a)','diff'])
ft.index += 1
print(ft)