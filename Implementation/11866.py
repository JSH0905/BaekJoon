### 요세푸스0

people = []
result = []
current_loc = 0

N , K = map(int, input().split())

for i in range(1, N + 1):
    people.append(i)

for k in range(N):

    current_loc += K -1

    if current_loc >= len(people):
        current_loc = current_loc % len(people)

    result.append(str(people.pop(current_loc)))

print("<", ", ".join(result)[:], ">", sep = '')
