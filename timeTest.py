import time

a = time.localtime()
x = time.strftime("%d.%m.%Y, %H:%M:%S", a)
print(x) 
# 18.03.2021, 20:47:30

import django
print(django.get_version())