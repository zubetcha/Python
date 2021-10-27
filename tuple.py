# tuple = 수정이 불가능한 리스트

a = ('사과', '감', '배')

print(a)

# set = 중복되는 값을 제거한 후 출력

a = [1, 2, 3, 4, 5, 4, 2, 6, 1, 8]

a_set = set(a)
print(a_set )

a = ['사과', '감', '배', '수박', '딸기']
b = ['배', '사과', '포도', '참외', '수박']

a_set = set(a)
b_set = set(b)

print(a_set | b_set)

student_a = ['물리2','국어','수학1','음악','화학1','화학2','체육']
student_b = ['물리1','수학1','미술','화학2','체육']

a_set = set(student_a)
b_set = set(student_b)

print(a_set - (a_set & b_set))