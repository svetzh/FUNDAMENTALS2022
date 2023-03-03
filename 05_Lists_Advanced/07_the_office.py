happiness = [int(el) for el in input().split()]
factor = int(input())
mult_happy_fact_compr = [num * factor for num in happiness]
avg_happiness = sum(mult_happy_fact_compr) / len(mult_happy_fact_compr)
happy_employees = [el for el in mult_happy_fact_compr if el >= avg_happiness]
half_num = len(mult_happy_fact_compr) / 2
if len(happy_employees) >= half_num:
    print(f"Score: {len(happy_employees)}/{len(mult_happy_fact_compr)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(mult_happy_fact_compr)}. Employees are not happy!")