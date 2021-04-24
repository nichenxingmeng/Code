s = input().strip()
temp1 = s[:3]
temp2 = float(s[3:s.index('|')])
temp3 = s[s.index('|'):]
print('{:<8}|{:>8.1f}{}'.format(temp1, temp2, temp3))
