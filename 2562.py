list = []

for i in range(9):
    list.append(int(input()))

maxNumber = max(list)
indexOfMaxNumber = list.index(maxNumber) + 1

print(maxNumber)
print(indexOfMaxNumber)