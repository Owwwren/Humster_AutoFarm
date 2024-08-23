from tkinter import *
import time

######################ДОПИКИ###########################
# Создание RGB
def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb 
# Проверка написания русского номера
Usinput = None
def check_number(var = None, window = None, state=None):
    global Usinput
    text = var.get()
    if state == 'number': # Коррекция ввода пользователя в формат 9ХХХХХХХХХ
        if text[0] == '8':
            Usinput = text[1:]
        if text[0] == '7':
            Usinput = text[1:]
        if text[0] == '+':
            if text[1] == '7':
                Usinput = text[2:]
            if text[1] == '8':
                Usinput = text[2:]
            if text[1] == '9':
                Usinput = text[1:]
        if text[0] == '9':
            Usinput = text
        if len(str(Usinput)) != 10:  # Проверка на длину номера
            #error = Label(window, text='Не верный формат!',
            #            font = ("Comic Sans MS", 20, 'bold'),
            #            bg = from_rgb((26, 26, 26)),
            #            fg = from_rgb((255, 0, 0)))
            #error.place(x = 6)
            #time.sleep(5)                                      не работает :( 
            #error.destroy()
            print('Не верный формат!')
        else:
            window.destroy()
    if state != 'number':
        Usinput = text
        window.destroy()
#######################################################


# Инициализация драйвера
def init_driver(source_driver=None, debug=False):
    driver = source_driver
    if debug == True:
        if driver is None:
            print('Ошибка передачи Driver!')
            return False
        else:
            print('Driver Успешно передан!')
    return driver



# Всплывающее окно для ввода номера
def User_input(state=None):
    global Usinput
    #                                          Настройки окна
    window = Tk()
    window.config(bg=from_rgb((26, 26, 26)))
    #                                              Шапка
    window.title('')
    #                                           Размер окна
    window.geometry('300x150')
    window.resizable(width=False, height=False)
    #                                            Текст ввода
    if state == None:
        print('User_input(STATE). Не указан STATE!')
    if state == 'number':   # Текст для ввода номера
        text = Label(window, text='Введите номер телефона!',
                     font = ("Comic Sans MS", 12, 'bold'),
                     bg = from_rgb((26, 26, 26)),
                     fg = from_rgb((158, 158, 158)))
        text.place(x = 35, y = 5)
    if state == 'cod':   # Текст для ввода кода
        text = Label(window, text='Введите код из сообщения!',
                     font = ("Comic Sans MS", 12, 'bold'),
                     bg = from_rgb((26, 26, 26)),
                     fg = from_rgb((158, 158, 158)))
        text.place(x = 30, y = 5)
    if state == 'password':   # Текст для ввода пароля
        text = Label(window, text='Введите пароль от 2FA!',
                     font = ("Comic Sans MS", 12, 'bold'),
                     bg = from_rgb((26, 26, 26)),
                     fg = from_rgb((158, 158, 158)))
        text.place(x = 40, y = 5)
    #       Строка ввода
    enter = Entry(window, width = 30, bg = 'white')
    enter.place(x = 45, y = 50)
    #                                          Кнопка
    btn = Button(window,
             text = 'Подтвердить',
             font = ("Comic Sans MS", 12, 'bold'),
             fg = from_rgb((255, 255, 255)),
             activeforeground = 'white',
             bg = from_rgb((128, 128, 128)),
             activebackground = 'black',
             command = lambda: check_number(var=enter, window=window, state=state),
             border = "0")
    btn.place(x = 85, y = 90)
    window.mainloop()
    return Usinput
