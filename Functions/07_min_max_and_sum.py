customer_insert = input().split()
customer_input = list(map(int, customer_insert))

print(f"The minimum number is", min(customer_input))
print(f"The maximum number is", max(customer_input))
print(f"The sum number is:", sum(customer_input))
