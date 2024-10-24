### 셀프 넘버

### 풀이 방법 : set() 사용.
### set()의 특징 : 1. 순서가 없음 / 2. 중복을 허용하지 않음

natural_num = set(range(1,10000))
generated_num = set()

for num in natural_num:

    for i in str(num):
        num += int(i)
    generated_num.add(num)

self_numbers = natural_num - generated_num
for self_num in sorted(self_numbers):
    print(self_num)
