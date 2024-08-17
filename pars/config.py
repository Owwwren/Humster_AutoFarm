from selenium import webdriver
from Proxy.Generate import gen_proxy
from Proxy.Proxy_login_script import get_login_proxy
from multiprocessing import Pool
from fake_useragent import UserAgent

import os
import time

quantity_autoreg = 2 #Количество браузеров
count = 0
execution = []
while True:     #Запуск стартовой странице
    count = count + 1
    lst = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'
    execution.append(lst)
    if count == quantity_autoreg:
        break
print(execution)


#Создание опций драйвера
def get_chromdriver(use_proxy=False, login_proxy=False, debug_proxy=False,
                    captha=False, fake_useragent=False, off_webdriver=False, headless=False):
    chrome_options = webdriver.ChromeOptions()

    if use_proxy == True: #Использование пркси вкл/выкл
        if login_proxy == False:     #proxy без логина и пороля
            chrome_options.add_argument(f"--proxy-server={gen_proxy(debug=debug_proxy)}")
        elif login_proxy == True:     #proxy с логином и поролем
            get_login_proxy(debug=debug_proxy)
            plugin_file = 'Proxy/proxy_auth_plugin.zip'
            chrome_options.add_extension(plugin_file)
    if captha == True: #Использование инструмента КАПЧА в хроме вкл/выкл
        _path = os.path.abspath("Captcha")
        chrome_options.add_argument(f'--load-extension={_path}')
    if fake_useragent == True: #Использование фэйкового user agent вкл/выкл
        chrome_options.add_argument(f'--user-agent={UserAgent().random}')
    if off_webdriver == True: #Отключение отображения WEB Driver для сайтов
        chrome_options.add_argument(f'--disable-blink-features=AutomationControlled')
    if headless == True:
        print('print')
        chrome_options.add_argument('headless')

    driver = webdriver.Chrome(options=chrome_options)
    return driver

def get_data(url):
    ############настройки################
    target_page = 'https://addexref.work/r/ref/111158' #'https://pr-cy.ru/technologies/ddos-guard/'   # Ссылка на сайт | если нет то None (!!!Уйдет в ошибку!!!)
    debug = True   # False |  ВКЛ/ВЫКЛ режим debug(Отображение стадий выполнения в коде, если у функций есть этот режим)
    protection = None   # DDoS-GUARD, CloudFlare, если нет то None | Обход защиты от DDos атак 
    capcha = False   # False |  ВКЛ/ВЫКЛ обход капчи
    use_proxy = False     # True | ВКЛ/ВЫКЛ использование прокси
    login_proxy = False    # True | Нужнали авторизация по логину и паролю в прокси
    fake_useragent = False   # True | ВКЛ/ВЫКЛ юзерагент
    off_webdriver = True   # False | Отключить вэбдрайвер
    
    headless = False    # ХЗ что это
    ############Логика################
    try:
        if debug == True:
            print("#########################")
            print("###Режим Debug ключен!###")
            print("#########################")
            print("")
            print("")

        driver = get_chromdriver(use_proxy=use_proxy, login_proxy=login_proxy, debug_proxy=debug,
                                 captha=capcha, fake_useragent=fake_useragent, off_webdriver=off_webdriver, headless=headless)
        driver.get(url)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(100)

        #humster_script()
        
    except Exception as ex:
         print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    p = Pool(processes=5)
    p.map(get_data, execution)
    print("")
    print('БОТ завершил работу!')

