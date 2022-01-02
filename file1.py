import os, sys, requests
print(os.getlogin())
print(sys.builtin_module_names)
print(list(os.uname()))
k = False
r = requests.get('https://yandex.ru')
print(r.status_code)