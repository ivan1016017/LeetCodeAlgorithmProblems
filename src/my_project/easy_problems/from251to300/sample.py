def fix_me(my_list):

    if len(my_list) % 2:  # imperative code
        new_list = []
        try:            
            for item in my_list:
                for element in item:
                    new_list.append(element)
        except:
            new_list = my_list
    else:  # functional code

        new_list = [num for element in my_list for num in element]

    new_list.sort(reverse=False, key=lambda x: -x)

    return new_list
    


print(fix_me([ [ 3, 4 ], [ 2, 6 ] ]))

print(fix_me([ [ 3, 4 ], [ 12, 32, 89 ], [ 0 ] ]))

print(fix_me([ [ 3, 4 ], [ 12, 32, 89 ], [ 0 ], [ -1 ] ]))

print(fix_me([100, 89, 56, 12, 4, 3, 0]))
