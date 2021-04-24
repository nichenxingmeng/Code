Time={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six',\
      '7':'seven','8':'eight','9':'nine','10':'ten','11':'eleven','12':'twelve',\
      '13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen',\
      '18':'eighteen','19':'nineteen','20':'twenty','30':'thirty','40':'forty','50':'fifty'}

time = list(map(str, input().split()))
for i in range(len(time)):
    if int(time[i]) > 20 and int(time[i]) < 60:
        a = str(int(time[i])%10)
        if a == 0:
            a = ''
        time.append(Time[str(int(time[i])//10*10)])
        time.append(Time[a])
    else:
        time.append(Time[time[i]])
if time[-1] == 'zero':
    time[-1] = "o'clock"
for i in range(2, len(time)):
    print(time[i],end=' ')
