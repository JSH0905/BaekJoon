n = int(input())
cnt = n

for i in range(n):
    word = input()

    for k in range(len(word)-1):
        if word[k] == word[k+1]:
            pass
        elif word[k] in word[k+1:]: ## 핵심
            cnt -= 1
            break

print(cnt)
