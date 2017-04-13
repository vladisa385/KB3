RU1 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

text=""
f = open('text3.txt')
for line in f:
 for i in line:
     if RU1.find(i)!=-1:
         text +=i
print(text.lower())
