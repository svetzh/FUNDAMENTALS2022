raw_input = input()
company_data = {}
while raw_input != "End":
    command = raw_input.split(" -> ")
    company_name = command[0]
    employee_id = command[1]
    if company_name in company_data.keys():
        if employee_id not in company_data[company_name]:
            company_data[company_name].append(employee_id)
    else:
        # company_data[company_name] = [id]
        company_data[company_name] = []
        company_data[company_name].append(employee_id)

    raw_input = input()

# for company, ids in company_data.items():
#     print(f"{company}")
#     for i in range(len(ids)):
#         print(f"-- {ids[i]}")

for company in company_data:
    print(f"{company}")
    for employee in company_data[company]:
        print(f"-- {employee}")
#
#############################################################################

# command = input()
# company_info = {}
#
# def employee_id_search(id):
#     if id not in company_info[id].values():
#         return False
#
#
# while command != "End":
#     company_name, employee_id = command.split(" -> ")
#     company_info[company_name] = company_info.get(company_name, {})
#
#     if not employee_id_search(company_name):
#         company_info[company_name][employee_id] = employee_id
#     command = input()
#
# for name_uni in company_info:
#     print(name_uni)
#     for key, value in company_info[name_uni].items():
#         print(f"-- {value}")
#############################################################################
company_dict = {}

while True:
    command = input()
    if command.lower() == "end":
        break
    command = command.split(" -> ")
    company = command[0]
    employee_id = command[1]
    company_dict.setdefault(company, {})
    company_dict[company][employee_id] = employee_id

var = {print(company, "-- " + "\n-- ".join([x for x in company_dict[company]]), sep="\n") for company in company_dict}









