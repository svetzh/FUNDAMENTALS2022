countries = input().split(", ")
capitals = input().split(", ")

binded_to_dict = {a_country: a_capital for a_country, a_capital in zip(countries, capitals)}
result = [f"{a_country} -> {a_capital}" for a_country, a_capital in binded_to_dict.items()]
print('\n'.join(result))

# with DICT COMPREHENSION:
# capital_by_country = {countries[idx]: capitals[idx] for idx in range(len(countries))}
# for k, v in capital_by_country.items():
#     print(f"{k} -> {v}")
# # with normal LOOP(LONG FORM):
capital_by_country = {}
for idx in range(len(countries)):
    country = countries[idx]
    capital = capitals[idx]
    capital_by_country[country] = capital

for k, v in capital_by_country.items():
    print(f"{k} -> {v}")