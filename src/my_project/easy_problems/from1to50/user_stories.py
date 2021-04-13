import random
random.seed(10)

first_dict_members = {'Christtian': list(), 'Ivan': list(), 'Manuel': list()}
first_temp_list = list()
first_choices = [1, 2, 3, 4, 5, 6, 7, 8]
i = 1
while i <= 8:
    a = random.choice(first_choices)
    if a not in first_temp_list:
        first_temp_list.append(a)
        if i == 1 or i == 2:
            first_dict_members["Christtian"].append(a)
        elif i in [3,4,5]:
            first_dict_members["Ivan"].append(a)
        elif i in [6, 7, 8]:
            first_dict_members["Manuel"].append(a)
        i += 1

second_dict_members = {'Christtian': list(), 'Ivan': list(), 'Manuel': list()}
second_temp_list= list()
second_choices = [9, 10, 11, 12, 13, 14, 15, 16]
i = 1
while i <= 8:
    a = random.choice(second_choices)
    if a not in second_temp_list:
        second_temp_list.append(a)
        if i == 1 or i == 2:
            second_dict_members["Christtian"].append(a)
        elif i in [3,4,5]:
            second_dict_members["Ivan"].append(a)
        elif i in [6, 7, 8]:
            second_dict_members["Manuel"].append(a)
        i += 1

print(first_dict_members)
print(second_dict_members)