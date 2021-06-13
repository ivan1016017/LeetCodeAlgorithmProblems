


def processLogs(logs, threshold):
    temp_user = []
    above_threshold = []
    dict_user = dict()
    for item in logs:

        if item.split()[0] == item.split()[1]:

            if item.split()[0] not in list(dict_user.keys()):
                dict_user[item.split()[0]] = 1
            else:
                dict_user[item.split()[0]] +=1

        if item.split()[0] != item.split()[1]:
            print(item.split()[0], item.split()[1])
            if item.split()[0] not in list(dict_user.keys()):
                dict_user[item.split()[0]] = 1
            else:
                dict_user[item.split()[0]] +=1
            if item.split()[1] not in list(dict_user.keys()):
                dict_user[item.split()[1]] = 1
            else:
                dict_user[item.split()[1]] +=1

    for names in list(dict_user.keys()):
        if dict_user[names] >= threshold:
            above_threshold.append(names)

    return above_threshold





print(processLogs(["88 99 200", "88 99 300", "12 12 15", "99 32 100"], 2))



