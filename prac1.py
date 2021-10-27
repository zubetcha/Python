# 리스트에서 짝수인 숫자만 출력하기

num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

for num in num_list:
    if num % 2 == 0 :
        print(num)

# 리스트에서 짝수인 숫자의 갯수 출력하기

count = 0
for num in num_list:
    if num % 2 == 0 :
        count += 1
print(count)

# 리스트에 있는 모든 숫자 더하기

sum = 0
for num in num_list:
    sum += num

print(sum)

# 리스트 안에 있는 자연수 중 가장 큰 숫자 구하기

max = 0
for num in num_list:
    if max < num:
        max = num
print(max)