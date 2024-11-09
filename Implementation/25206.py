# 너의 평점은

import sys

grade_list = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F" ]
grade_point = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0 ]

sum_of_credit = 0
credit_multiply_grade = 0

for _ in range(20):
    subject, credit, grade = map(str, sys.stdin.readline().split())

    if grade != "P":
        sum_of_credit += float(credit)
        credit_multiply_grade += float(credit) * grade_point[grade_list.index(grade)]

print(format(credit_multiply_grade / sum_of_credit, ".6f"))

