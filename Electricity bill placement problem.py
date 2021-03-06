PROGRAM 1:
n=int(input())
d={}
for i in range(n):
    a=input().split(":")
    b=a[1].split("$")
    if(len(b)>1):
        for i in b:
            i=i.strip()
            c=i.split(" ")
            if(c[0] not in d.keys()):
                d[c[0]]=int(c[1])
            else:
                d[c[0]]+=int(c[1])
for i,j in d.items():
    if(d[i]>0 and d[i]<=999):
        print("{}:{:.2f}" .format(i,d[i]*0.40))
    elif(d[i]>1000 and d[i]<=2000):
        print("{}:{:.2f}" .format(i,d[i]*0.33))    
    elif(d[i]>2001 and d[i]<=5000):
        print("{}:{:.2f}" .format(i,d[i]*0.30))
    elif(d[i]>5000):
        print("{}:{:.2f}" .format(i,d[i]*0.20))




PROGRAM 2:
import collections, functools, operator
n=int(input())
list1=[]
for i in range(n):
    a=input().split("$")
    b=a[0].split(":")
    a.append(b[1])
    if(len(a[1:])!=1):
       for j in (a[1:]):
           j=j.strip()
           j=j.split(" ")
           d={j[0]:int(j[1])}
           list1.append(d)
shop = dict(functools.reduce(operator.add, 
         map(collections.Counter,list1)))
for i in range(1,len(shop)+1):
    e="shop{}".format(i)
    if(shop[e]>0 and shop[e]<=999):
        x=shop[e]*0.40
        print("{}:{:.2f}".format(e,x))
    elif(shop[e]>=1000 and shop[e]<=2000):
        x=shop[e]*0.33
        print("{}:{:.2f}".format(e,x))
    elif(shop[e]>=2001 and shop[e]<=5000):
        x=shop[e]*0.30
        print("{}:{:.2f}".format(e,x))
    elif(shop[e]>=5000):
        x=shop[e]*0.20
        print("{}:{:.2f}".format(e,x))         



PROGRAM 3:
import collections, functools, operator
n=int(input())
list1=[]
for i in range(n):
    a=input().split(":")
    b=a[1].split("$")
    if(len(b)!=1):
        for i in b:
            i=i.strip()
            c=i.split(" ")
            d={c[0]:int(c[1])}
            list1.append(d)
shop = dict(functools.reduce(operator.add, 
         map(collections.Counter,list1)))
for i in range(1,len(shop)+1):
    e="shop{}".format(i)
    if(shop[e]>0 and shop[e]<=999):
        x=shop[e]*0.40
        print("{}:{:.2f}" .format(e,x))
    elif(shop[e]>1000 and shop[e]<=2000):
        x=shop[e]*0.33
        print("{}:{:.2f}" .format(e,x))    
    elif(shop[e]>2001 and shop[e]<=5000):
        x=shop[e]*0.30
        print("{}:{:.2f}" .format(e,x))
    elif(shop[e]>5000):
        x=shop[e]*0.20
        print("{}:{:.2f}" .format(e,x))

'''
TEST CASE 1:
3
Jan 1, 2020: shop1 320$shop2 220$shop3 330$shop4 420$shop5 5
Jan 2, 2020: shop5 318$shop4 320$shop3 330$shop2 420$shop1 5
Jan 3, 2020:

OUTPUT:
shop1:130.00
shop2:256.00
shop3:264.00
shop4:296.00
shop5:129.20

TEST CASE 2:
6
Jan 01, 2020: shop1 320$shop2 220$shop3 330$shop4 420$shop5 57
Jan 02, 2020: shop5 81$shop4 380$shop3 327$shop2 240$shop1 318
Jan 03, 2020: shop1 316$shop3 334$shop4 400$shop5 75$shop2 211
Jan 04, 2020:
Jan 05, 2020: shop1 323$shop2 210$shop3 300$shop4 418$shop5 43
Jan 06, 2020: shop1 324$shop3 315$shop4 411$shop5 48

OUTPUT:
shop1:528.33
shop2:352.40
shop3:529.98
shop4:608.70
shop5:121.60

TEST CASE 3:
8
Jan 1, 2020: shop1 320$shop2 220$shop3 330$shop4 420$shop5 5
Jan 2, 2020: shop5 318$shop4 320$shop3 330$shop2 420$shop1 5
Jan 3, 2020: shop1 316$shop1 820$shop3 330$shop4 420$shop5 5
Jan 4, 2020: shop1 314$shop2 110$shop3 68$shop4 420$shop5 5
Jan 5, 2020: shop1 323$shop2 220$shop3 330$shop4 420$shop5 5
Jan 6, 2020: shop1 324$shop3 330$shop4 420$shop5 5
Jan 7, 2020: shop1 320$shop2 220$shop3 330$shop4 420$shop5 51
Jan 8, 2020:

OUTPUT:
shop1:822.60
shop2:392.70
shop3:614.40
shop4:852.00
shop5:157.60 
'''
