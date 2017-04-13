RU1 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
sdvig=[[1],[14],[15],[16]]
temp = []
i = 1
while i < 32:
    temp.append([])
    temp[i-1].append(RU1[i])
    for j in sdvig:
        if (i - int(j[0])) >= 0:
            temp[i-1].append(RU1[i - j[0]])
        else:

            temp[i-1].append(RU1[32 - -i - int(j[0])])
    i = i + 1
print(temp)