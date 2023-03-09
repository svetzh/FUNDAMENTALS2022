results_points = {}
submissions = {}
command = input()
count = 0
while not command == "exam finished":
    banned_command = command.split("-")
    if banned_command[1] == "banned":
        del results_points[banned_command[0]]
        break

    line = command.split("-")
    user_name = line[0]
    lang_submission = line[1]
    points = int(line[2])

    if user_name not in results_points.keys():
        results_points[user_name] = points
        if results_points[user_name] < points:
            results_points[user_name] = points
    else:
        if results_points[user_name] < points:
            results_points[user_name] = points

    if lang_submission not in submissions:
        submissions[lang_submission] = 0
    submissions[lang_submission] += 1
    command = input()

print("Results:")
for i, e in results_points.items():
    print(f"{i} | {e}")

print("Submissions:")
for k, v in submissions.items():
    print(f"{k} - {v}")

####################################################
# # with sorting discending at the end:
# user_points = {}
# language_submission = {}
#
# data = input()
#
# while not data == "exam finished":
#     split_data = data.split("-")
#     if split_data[1] == "banned":
#         pass
#     else:
#         user, language, points = split_data
#         points = int(points)
#         if user in user_points:
#             if user_points[user] < points:
#                 user_points[user] = points
#         else:
#             user_points[user] = points
#
#         if language not in language_submission:
#             language_submission[language] = 0
#         language_submission[language] += 1
#
#     data = input()
#
# sorted_user_points = sorted(user_points.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))
# print("Results:")
# for user, points in sorted_user_points:
#     print(f"{user} | {points}")
#
# sorted_language_submissions = sorted(language_submission.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))
# print("Submissions:")
# for lang, sumbmiss in sorted_language_submissions:
#     print(f"{lang} - {sumbmiss}")





















