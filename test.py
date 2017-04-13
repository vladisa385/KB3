RU1 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
RU1=RU1.lower()
tabl = {'0.0553':0,'0.0366 ':1,'0.0345':2,'0.0400':3,'0.0340':4,'0.0360':5,'0.0326':6,'0.0241':7,' 0.0287':8,'0.0317':9,'0.0265:':10,'0.0251':11,'0.0244':12,'0.0291':13,'0.0322':14,'0.0249':16,}

import math
#print(RU1)
def Kasiski(text):
    srez = 0
    srezintext = 0
    ListLenght = []
    while ((ListLenght!=None) and (srez < len(text))):

        threegram = text[srez:srez + 3]
        #print(text[srez:srez + 3])
        z = 0
        startfind = 0
        temp = []
        while (startfind!=len(text)): ##ищем триграмы
            z = text.find(threegram,startfind , len(text))
            if z != -1:
                if len(temp)==0:
                    temp.append(threegram)
                temp.append(z)
                #print(temp )
               # print(threegram)
                startfind = z+1
            else :
                break
        if len(temp) > 2 and temp[0].isalpha():
            temp2=[]
            temp2.append(temp[0])
            ss = 0
            for u in temp[1:]:

               # if s!=-1:
                 #for a in  text[s:u]:

                 #  if RU1.find(a,0,len(RU1))==-1:
                   #    print(a)
                    #   ss+=1
                if ss!=0:
                 temp2.append(u-ss)
                ss=u

            n = temp2[1:]
            a = n[0]
            for i in range(len(n)): ## общий делитель
                b = n[i]
                while b:
                    a, b = b, a % b
            temp2.append(str(a))


            if int(a)>1 and int(a)<10 and len(temp2)>3:

             c=0
             for i in ListLenght: ##проверяем на повторы
                 if i[0]==temp2[0]:
                     c=1
             if c!=1:
              ListLenght.append(temp2)

        srez +=1
   # print(ListLenght)
    return ListLenght

def findlenkey(listfound):
    tempscore = 0
    for tempcount in xx:
        tempscore += int(tempcount[len(tempcount) - 1])
    return round(tempscore/len(xx))

def createcows(text,numbercows):
    listcows=[]
    temp=0
    while temp<numbercows:
        listcows.append([])
        temp +=1
    temp = 0
    for i in text:
        listcows[temp].append(i)
        if temp == numbercows-1:
            temp = 0
        else:
            temp+=1
    return listcows

def vzaimindex(textwithcows):
    f = open('outputfile.txt', 'w')
    listscore=[]
    listindex=[]
    listscorealp=[]
    listsdv=[]
    temp = 0
    while temp < len(textwithcows):
        tempdict = {a: 0 for a in RU1}
        listindex.append(tempdict)
        temp += 1
    temp = 0
    sum=0
    chars=0
    while temp < len(textwithcows):
        sum=0
        chars = len(textwithcows[temp])
        for i in textwithcows[temp]:
            listindex[temp][i]= listindex[temp][i]+1
        for t in RU1:
            sum = (listindex[temp][t])*(listindex[temp][t]-1)/(chars*(chars-1))+sum
        listscore.append(sum)
        listscorealp.append(chars)

        temp +=1

    constSc=listscore[0]
    temp=1

    while temp < len(textwithcows):
        listsdv.append([])
        sumtemp = listscore[temp]
        itog=0
        n=0

        while ((0.07-itog)<0 or (itog-0.053)<0) :
            itog = 0
            for t in RU1:

                itog =((listindex[temp][t])*(listindex[0][t]))/(listscorealp[0]*listscorealp[temp])+itog

            forhelp=0
            x=str(round(itog,4))
            print("Kirill-krasava")
            try:

               # print(tabl[str(x)])
               # print(str(temp)+ "&&"+str(itog))
                listsdv[temp-1].append(tabl[str(x)])

            except:
                pass
            h=0
            copy =  listindex[temp].copy()

            for t in RU1:
                 if(RU1.index(t))==0:
                     c=31
                 else:
                     c=RU1.index(t)-1

                 listindex[temp][t]=copy[RU1[c]]



            f.write(str(listindex[temp])+'\n')
            f.write(str(n)+"=="+str(itog))

            n+=1
            if n ==17:break

        temp += 1



   # print(listsdv)
    
    return listsdv

def findgap(sdvig):
    temp=[]
    i=1
    while i<33:
        temp.append([])
        temp[i-1].append(RU1[i])
        for j in sdvig:
             if (i - int(j[0]))>=0:
                 temp[i-1].append(RU1[i - j[0]])
             else:

                 temp[i-1].append(RU1[32 - -i-int(j[0])])
        i=i+1
    print(temp)


text=""
f = open('text2.txt')
for line in f:
 text +=line

xx=Kasiski(text)
countcows = findlenkey(xx)
textwithcows=createcows(text,countcows)
sdvig=vzaimindex(textwithcows)
print(sdvig)

#x=findgap(sdvig)

#print(sdvig)
#y=findgap(sdvig)







