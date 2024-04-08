n =int(input())
x = list()
y = list()
for c in range(n):
    x.append(int(input()))

x.sort()

for c in range(len(x)):
    if x[c] not in y:
        y.append(x[c])

for c in range (len(y)):
    print("{} aparece {} vez(es)".format(y[c],x.count(y[c])))


