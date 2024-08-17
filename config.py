from tkinter import *
from key_satings import account_key

def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   

#ПЕРЕМЕННЫЕ
auto_up_button_conf = 0
auto_key_button_conf = 1
auto_morz_button_conf = 1
auto_kombo_button_conf = 1
proxy_button_conf = 1

#Доп. функции
def on_off(conf):
    if conf == 'auto_up':
        global auto_up_button_conf
        x = auto_up_button_conf
        if auto_up_button_conf == 1:
            print(auto_up_button_conf)
            auto_up_button_conf = 0
        else:
            print(auto_up_button_conf)
            auto_up_button_conf = 1
        print(x)
        auto_up_button.config(image=photo_list[x])
    if conf == 'auto_key':
        global auto_key_button_conf
        x = auto_key_button_conf
        if auto_key_button_conf == 1:
            print(auto_key_button_conf)
            auto_key_button_conf = 0
        else:
            print(auto_key_button_conf)
            auto_key_button_conf = 1
        print(x)
        auto_key_button.config(image=photo_list[x])
    if conf == 'auto_morz':
        global auto_morz_button_conf
        x = auto_morz_button_conf
        if auto_morz_button_conf == 1:
            print(auto_morz_button_conf)
            auto_morz_button_conf = 0
        else:
            print(auto_morz_button_conf)
            auto_morz_button_conf = 1
        print(x)
        auto_morz_button.config(image=photo_list[x])
    if conf == 'auto_kombo':
        global auto_kombo_button_conf
        x = auto_kombo_button_conf
        if auto_kombo_button_conf == 1:
            print(auto_kombo_button_conf)
            auto_kombo_button_conf = 0
        else:
            print(auto_kombo_button_conf)
            auto_kombo_button_conf = 1
        print(x)
        auto_kombo_button.config(image=photo_list[x])
    if conf == 'proxy':
        global proxy_button_conf
        x = proxy_button_conf
        if proxy_button_conf == 1:
            print(proxy_button_conf)
            proxy_button_conf = 0
        else:
            print(proxy_button_conf)
            proxy_button_conf = 1
        print(x)
        proxy_button.config(image=photo_list[x])

#Настройки окна
window = Tk()
window.config(bg=from_rgb((26, 26, 26)))
# фон
img = PhotoImage(file = 'fon.png')
logo = Label(window, image = img, bg = 'black')
logo.pack()

#       Шапка
window.title('HK AutoBot') 
window.iconbitmap('icon.ico')

#       Размер окна
window.geometry('600x600')
window.resizable(width=False, height=False)


#Внутрянка
btn1 = Button(window,
             text = 'Аккаунт 1',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((158, 158, 158)),
             activeforeground = 'white',
             bg = from_rgb((26, 26, 26)),
             activebackground = 'black',
             command = lambda: account_key(1),
             border = "0")
btn1.place(x = 38, y = 90)
btn2 = Button(window,
             text = 'Аккаунт 2',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((158, 158, 158)),
             activeforeground = 'white',
             bg = from_rgb((26, 26, 26)),
             activebackground = 'black',
             border = "0")
btn2.place(x = 38, y = 150)
btn3 = Button(window,
             text = 'Аккаунт 3',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((158, 158, 158)),
             activeforeground = 'white',
             bg = from_rgb((26, 26, 26)),
             activebackground = 'black',
             border = "0")
btn3.place(x = 38, y = 210)
btn4 = Button(window,
             text = 'Аккаунт 4',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((158, 158, 158)),
             activeforeground = 'white',
             bg = from_rgb((26, 26, 26)),
             activebackground = 'black',
             border = "0")
btn4.place(x = 38, y = 270)
btn5 = Button(window,
             text = 'Аккаунт 5',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((158, 158, 158)),
             activeforeground = 'white',
             bg = from_rgb((26, 26, 26)),
             activebackground = 'black',
             border = "0")
btn5.place(x = 38, y = 330)
btn6 = Button(window,
             text = 'Аккаунт 6',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((158, 158, 158)),
             activeforeground = 'white',
             bg = from_rgb((26, 26, 26)),
             activebackground = 'black',
             border = "0")
btn6.place(x = 38, y = 390)
btn7 = Button(window,
             text = 'Аккаунт 7',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((158, 158, 158)),
             activeforeground = 'white',
             bg = from_rgb((26, 26, 26)),
             activebackground = 'black',
             border = "0")
btn7.place(x = 38, y = 450)






btn21 = Button(window,
             text = 'Аккаунт 8',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((158, 158, 158)),
             activeforeground = 'white',
             bg = from_rgb((26, 26, 26)),
             activebackground = 'black',
             border = "0")
btn21.place(x = 183, y = 90)
btn22 = Button(window,
             text = 'Аккаунт 9',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((158, 158, 158)),
             activeforeground = 'white',
             bg = from_rgb((26, 26, 26)),
             activebackground = 'black',
             border = "0")
btn22.place(x = 183, y = 150)
btn23 = Button(window,
             text = 'Аккаунт 10',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((158, 158, 158)),
             activeforeground = 'white',
             bg = from_rgb((26, 26, 26)),
             activebackground = 'black',
             border = "0")
btn23.place(x = 183, y = 210)
btn24 = Button(window,
             text = 'Аккаунт 11',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((158, 158, 158)),
             activeforeground = 'white',
             bg = from_rgb((26, 26, 26)),
             activebackground = 'black',
             border = "0")
btn24.place(x = 183, y = 270)
btn25 = Button(window,
             text = 'Аккаунт 12',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((158, 158, 158)),
             activeforeground = 'white',
             bg = from_rgb((26, 26, 26)),
             activebackground = 'black',
             border = "0")
btn25.place(x = 183, y = 330)
btn26 = Button(window,
             text = 'Аккаунт 13',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((158, 158, 158)),
             activeforeground = 'white',
             bg = from_rgb((26, 26, 26)),
             activebackground = 'black',
             border = "0")
btn26.place(x = 183, y = 390)


btn_more = Button(window,
             text = 'ЕЩЁ',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((158, 158, 158)),
             activeforeground = 'white',
             bg = from_rgb((26, 26, 26)),
             activebackground = 'black',
             border = "0")
btn_more.place(x = 183, y = 450)
btn_start_all = Button(window,
             text = 'ЗАПУСТИТЬ ВСЕ',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((255, 255, 255)),
             activeforeground = 'white',
             bg = from_rgb((72, 0, 1)),
             activebackground = 'black')
btn_start_all.place(x = 77, y = 510)


auto_up = Label(window,
              text = 'АВТО ПРОКАЧКА',
              font = ("Comic Sans MS", 12, 'bold'),
              bg = from_rgb((0, 0, 0)),
              fg = from_rgb((158, 158, 158)))
auto_up.place(x=410, y=350)
auto_key = Label(window,
              text = 'АВТО КЛЮЧИ',
              font = ("Comic Sans MS", 12, 'bold'),
              bg = from_rgb((0, 0, 0)),
              fg = from_rgb((158, 158, 158)))
auto_key.place(x=410, y=400)
auto_morz = Label(window,
              text = 'АВТО МОРЗЯНКА',
              font = ("Comic Sans MS", 12, 'bold'),
              bg = from_rgb((0, 0, 0)),
              fg = from_rgb((158, 158, 158)))
auto_morz.place(x=410, y=450)
auto_kombo = Label(window,
              text = 'АВТО КОМБО',
              font = ("Comic Sans MS", 12, 'bold'),
              bg = from_rgb((0, 0, 0)),
              fg = from_rgb((158, 158, 158)))
auto_kombo.place(x=410, y=500)
proxy = Label(window,
              text = 'ПРОКСИ',
              font = ("Comic Sans MS", 12, 'bold'),
              bg = from_rgb((0, 0, 0)),
              fg = from_rgb((158, 158, 158)))
proxy.place(x=410, y=545)












photo_list = [
               PhotoImage(file = 'button_off.png'),
               PhotoImage(file = 'button_on.png'),
] 
if auto_up_button_conf == 1:
    img_auto_up_button = PhotoImage(file = 'button_on.png')
if auto_up_button_conf != 1:
    img_auto_up_button = PhotoImage(file = 'button_off.png')
auto_up_button = Button(window,
                        image = photo_list[auto_up_button_conf],
                        bg = 'black',
                        border = "0",
                        activebackground = 'black',
                        command = lambda: on_off('auto_up'))
auto_up_button.place(x=340, y=350)

if auto_key_button_conf == 1:
    img_auto_key_button = PhotoImage(file = 'button_on.png')
if auto_key_button_conf != 1:
    img_auto_key_button = PhotoImage(file = 'button_off.png')
auto_key_button = Button(window,
                        image = img_auto_key_button,
                        bg = 'black',
                        border = "0",
                        activebackground = 'black',
                        command = lambda: on_off('auto_key'))
auto_key_button.place(x=340, y=400)

if auto_morz_button_conf == 1:
    img_auto_morz_button = PhotoImage(file = 'button_on.png')
if auto_morz_button_conf != 1:
    img_auto_morz_button = PhotoImage(file = 'button_off.png')
auto_morz_button = Button(window,
                         image = img_auto_morz_button,
                         bg = 'black',
                         border = "0",
                         activebackground = 'black',
                         command = lambda: on_off('auto_morz'))
auto_morz_button.place(x=340, y=450)

if auto_kombo_button_conf == 1:
    img_auto_kombo_button = PhotoImage(file = 'button_on.png')
if auto_kombo_button_conf != 1:
    img_auto_kombo_button = PhotoImage(file = 'button_off.png')
auto_kombo_button = Button(window,
                          image = img_auto_kombo_button, 
                          bg = 'black',
                          border = "0",
                          activebackground = 'black',
                          command = lambda: on_off('auto_kombo'))
auto_kombo_button.place(x=340, y=500)

if proxy_button_conf == 1:
    img_proxy_button = PhotoImage(file = 'button_on.png')
if proxy_button_conf != 1:
    img_proxy_button = PhotoImage(file = 'button_off.png')
proxy_button = Button(window,
                     image = img_proxy_button,
                     bg = 'black',
                     border = "0",
                     activebackground = 'black',
                     command = lambda: on_off('proxy'))
proxy_button.place(x=340, y=545)



window.mainloop()