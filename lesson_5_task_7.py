import json

total_profit = 0
i = 0
stat = {}
my_f = open('task_7.txt')
for line in my_f:
    data = line.split()
    profit = int(data[2])-int(data[3])
    total_profit += profit
    i += 1
    stat[data[0]] = profit
my_f.close()
average = int(total_profit/i)
av_dict = {'average_profit': average}

with open('task_7.json', 'w') as write_f:
    json.dump(stat, write_f)
    json.dump(av_dict, write_f)