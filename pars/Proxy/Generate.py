import random
import linecache

def gen_proxy(debug=False):
    line_count = sum(1 for line in open('Proxy/proxy.txt'))
    num = random.randint(1, line_count)
    proxy = linecache.getline(r"Proxy/proxy.txt", num)
    if debug == True:
        print(f'Всего прокси: {line_count}')
        print(f"Выбрано прокси: {proxy}")
    return proxy

