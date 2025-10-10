#1
'''
def kv(n):
    for i in range(0,n+1):
        yield i**2
n=int(input())
for j in kv(n):
    print(j)
'''
#2
'''
def zupsan(n):
    for i in range(0,n+1,2):
        yield i
n=int(input())
a=[str(j) for j in zupsan(n)]
print(",".join(a))
'''
#3
'''
def bl(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input())
for j in bl(n):
    print(j,end=" ")
'''
#4
'''
def kv(a,b):
    for i in range(a,b+1):
        yield i*i
a,b=map(int,input().split())
for j in kv(a,b):
    print(j,end=" ")
'''
#5
'''
def sandar(n):
    for i in range(0,n+1):
        yield n-i
n=int(input())
for j in sandar(n):
    print(j)
'''
#6
'''
from datetime import datetime, timedelta
today = datetime.now()
five_days_ago = today - timedelta(days=5)
print(f"Бес күн бұрын: {five_days_ago.strftime('%Y-%m-%d')}")
'''
#7
'''
from datetime import datetime,timedelta
b=datetime.now()
c=b-timedelta(5)
print(c)
'''
#8
'''
from datetime import datetime,timedelta
today=datetime.now()
tomorrow=today+timedelta(1)
yesterday=today-timedelta(1)
print(today)
print(tomorrow)
print(yesterday)
'''
#9
'''
from datetime import datetime
now=datetime.now()
m=now.replace(microsecond=0)
print(m)
print(now)
'''
#10
'''
from datetime import datetime,timedelta
now=datetime.now()
yesterday=now-timedelta(1)
dif=(yesterday-now).total_seconds()
print(dif)
'''
#11
'''
import math

d = 15
r = math.radians(d)
print(r)
'''
#12
'''
def t(h, a, b):
    return (a + b) * h / 2

h = 5
a = 5
b= 6
ar= t(h, a, b)
print(ar)
'''
#13
'''
import math
def polygon_area(sides, length):
    return (sides * length**2) / (4 * math.tan(math.pi / sides))

sides = 4
length = 25
area = polygon_area(sides, length)
print(f"Көпбұрыштың ауданы: {area}")
'''
#14
'''
def parallelogram_area(base, height):
    return base * height

base = 5
height = 6
area = parallelogram_area(base, height)
print(f"Параллелограмның ауданы: {area}")
'''
#15
'''
import json

filename = "/Users/meruert/Desktop/python/meruuu_pp2/lab4/1.json"
with open(filename) as f:
    data = json.load(f)
print("Интерфейс Статусы")
print("=" * 80)
print(f"{'DN':<50} {'Сипаттама':<20} {'Жылдамдық':<10} {'MTU'}")
print("-" * 80)
for item in data:
    print(f"{item['DN']:<50} {item['Description']:<20} {item['Speed']:<10} {item['MTU']}")
    
'''