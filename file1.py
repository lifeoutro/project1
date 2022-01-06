import os, sys, requests
try:
    print(os.getlogin())
    print(sys.builtin_module_names)
except:
    pass
k = False
r = requests.get('https://yandex.ru')
print(r.status_code)
