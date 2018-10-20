test = ['a','b','c']
test2 = ['aa','bb','cc']
test3 = {}
test3.fromkeys(test)
for i in range(len(test)):
    test3[test[i]] = test2[i]


print(list(test3.keys()))