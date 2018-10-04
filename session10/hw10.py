#Excercise 1
test = ['1','2','3','4']
te = ['two', 'words']
t = ['t']

test.append(te)
print(test)
test = ['1','2','3','4']
test.extend(te)
print(test)
test = ['1','2','3','4']
print(test + te)

test.insert(2,te)
print(test)
test = ['1','2','3','4']
test.insert(2,t)
print(test)
test = ['1','2','3','4']
test.insert(2, 't')
print(test)
