import re

subj_dict = {}

with open('task_6.txt') as my_f:
    for line in my_f:
        subj_list = line.split()
        sum = 0
        for el in subj_list:
            num = re.sub('[^0-9]','', el)
            if num != '':
                sum += int(num)
            else:
                pass
        subj_dict[subj_list[0][0:-1]] = sum

print(subj_dict)
