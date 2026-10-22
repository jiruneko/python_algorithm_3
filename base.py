data = [1,2,3,4,5,6,7,8,9,0]

for i in data:
    print(i)

data2 = [i for i in range(10) if i % 2 == 0]
print(data2)

data3 = [i if i % 2 == 0 else 0 for i in range(10)]
print(data3)

def calc(a):
    a -= 1
    return a

x = 3
print(calc(x))
print(x)