l = []
for i in open('data_aurora', 'r').readlines(): l.append(int(i))
year, m, d = 2020, 1, 0
for hr in l:
    if hr == 0: d += 1
    if d == 30: m += 1; d = 1
    if m == 12: year += 1; m = 1
    with open('datas', 'a') as w:
        w.write(str(year)); w.write('-'); w.write(str(m)); w.write('-'); w.write(str(d)); w.write('\n')
print(year, m, d)
