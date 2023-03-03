version_str = input().split(".")
version_int = int("".join(version_str)) + 1
new_version_list = list(str(version_int))
print(".".join(new_version_list))

#
# new_version_int = int("".join(new_version_list))
# new_version_str = str(new_version_int)
# t = iter(new_version_str)
# final_string = ".".join(a for a in t)
# print(final_string)