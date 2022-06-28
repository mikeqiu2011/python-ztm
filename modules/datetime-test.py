import datetime

print(datetime.time())  # 00:00:00
print(datetime.time(17, 35, 2))  # 17:35:02

now = datetime.date.today()
print(now)  # 2022-06-28

from time import time

start = time()
end = time()
print(f'program lapse {end - start} seconds')

from array import array

arr = array('i', [1, 2, 3])  # 'i' stands for signed-int takes only 2 bytes
print(arr)  # more performant than dynamic list
