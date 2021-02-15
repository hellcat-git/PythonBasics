from statistics import mean
import json

with open("text_7.txt", 'r', encoding='utf-8') as f:

    org_arr = {}
    while True:
        arr = f.readline().strip().split()
        if not arr:
            break
        rev = int(arr[2]) - int(arr[3])
        org_arr.update({arr[0]: rev})
    profit = mean(map(int, [k for k in org_arr.values() if k > 0]))
    res = [dict(org_arr), {'average_profit': profit}]

    with open("text_7.json", "w") as write_f:
        json.dump(res, write_f, indent=4)
