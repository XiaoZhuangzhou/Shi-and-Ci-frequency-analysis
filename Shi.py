# -*- coding:utf-8 -*-
import draw_a_bar
txt = open('Shi.txt','r',encoding= 'gbk').read()
wfile=open('result.txt','w')
dict={}
# for i in txt:
#   if i in ['\n','\u3000'] or i in "0123456789ABCDEFG（）,， *().。、":
#     continue
#   if i in dict:
#     dict[i]+=1
#   else:
#     dict[i]=1
# print(dict)
# res=sorted(dict.items(), key=lambda d:d[1],reverse=True)
# print(res)

for i in range(1,len(txt)):
  if txt[i] in ['\n','\u3000'] or txt[i] in "0123456789ABCDEFGqwertyuiopasdfghjklzxcvbnm=_（）,， *().。+":
    continue
  if txt[i+1] in ['\n','\u3000'] or txt[i+1] in "0123456789ABCDEFGqwertyuiopasdfghjklzxcvbnm=_（）,， *().。+":
    continue
  if txt[i] in "而何乎乃其且若所为焉以因于则者之如不无上下左右" or txt[i+1] in "而何乎乃其且若所为焉以因于则者之不无上下左右如":
    continue
  if txt[i]+txt[i+1] in dict:
    dict[txt[i]+txt[i+1]]+=1
  else:
    dict[txt[i]+txt[i+1]]=1
dict=sorted(dict.items(), key=lambda d:d[1],reverse=True)
shi_name=[]
shi_num=[]
print(len(dict))
for i in range(1,15):
  print(dict[i])
  shi_name.append(dict[i][0])
  shi_num.append(dict[i][1])
print(shi_num,shi_name)
draw_a_bar.draw_bar(shi_num,shi_name)