from configPars import init_driver, User_input
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



def tg_connect(source_driver=None, debug=False):
    driver = init_driver(source_driver=source_driver, debug=debug)
    time.sleep(5)
    try:
        try:
            phone_number_field = driver.find_element(By.ID, 'sign-in-phone-number')
            phone_number_field.clear()
            phone_number_field.send_keys('7')
            phone_number_field.send_keys(User_input('number'))
            phone_number_field.send_keys(Keys.ENTER)
        except:
            phone_number_field = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]')
            phone_number_field.clear()
            phone_number_field.send_keys('7')
            phone_number_field.send_keys(User_input('number'))
            phone_number_field.send_keys(Keys.ENTER)
    except Exception as ex:
        if debug == True:
            print(ex)
            print('Элемент для ввода номера не найден')
    finally:  
        try:
            time.sleep(5)
            try:
                phone_number_field = driver.find_element(By.ID, 'sign-in-code')
                phone_number_field.clear()
                phone_number_field.send_keys(User_input('cod'))
            except:
                try:
                    phone_number_field = driver.find_element(By.CLASS_NAME, 'form-control')
                    phone_number_field.clear()
                    phone_number_field.send_keys(User_input('cod'))
                except:
                    try:
                        phone_number_field = driver.find_element(By.CLASS_NAME, 'input-field-input is-empty')  
                        phone_number_field.clear()
                        phone_number_field.send_keys(User_input('cod'))   
                    except:
                        try:
                            phone_number_field = driver.find_element(By.CLASS_NAME, 'input-field-border')  
                            phone_number_field.clear()
                            phone_number_field.send_keys(User_input('cod'))   
                        except:
                            try:
                                phone_number_field = driver.find_element(By.XPATH, '#//*[@id="sign-in-code"]')  
                                phone_number_field.clear()
                                phone_number_field.send_keys(User_input('cod'))  
                            except:
                                phone_number_field = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[4]/div/div[3]/div/input')  
                                phone_number_field.clear()
                                phone_number_field.send_keys(User_input('cod'))    
        except Exception as ex:
            if debug == True:
                print(ex)
                print('Элемент для ввода кода не найден')
        finally:
            try:
                time.sleep(5)
                try:
                    phone_number_field = driver.find_element(By.NAME, 'notsearch_password')
                    phone_number_field.clear()
                    phone_number_field.send_keys(User_input('password'))
                    phone_number_field.send_keys(Keys.ENTER)
                except:
                    try:
                        phone_number_field = driver.find_element(By.CLASS_NAME, 'input-field-input is-empty')
                        phone_number_field.clear()
                        phone_number_field.send_keys(User_input('password'))
                        phone_number_field.send_keys(Keys.ENTER)
                    except:
                        try:
                            phone_number_field = driver.find_element(By.CLASS_NAME, 'stealthy')         #form-control  sign-in-password  //*[@id="sign-in-password"]
                            phone_number_field.clear()
                            phone_number_field.send_keys(User_input('password'))
                            phone_number_field.send_keys(Keys.ENTER)
                        except:
                            try:
                                phone_number_field = driver.find_element(By.CLASS_NAME, 'input-field input-field-password')
                                phone_number_field.clear()
                                phone_number_field.send_keys(User_input('password'))
                                phone_number_field.send_keys(Keys.ENTER)
                            except:
                                try:
                                    phone_number_field = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[5]/div/div[2]/div/input[2]')
                                    phone_number_field.clear()
                                    phone_number_field.send_keys(User_input('password'))
                                    phone_number_field.send_keys(Keys.ENTER)
                                except:
                                    try:
                                        phone_number_field = driver.find_element(By.CLASS_NAME, 'form-control')
                                        phone_number_field.clear()
                                        phone_number_field.send_keys(User_input('password'))
                                        phone_number_field.send_keys(Keys.ENTER)
                                    except:
                                        try:
                                            phone_number_field = driver.find_element(By.ID, 'sign-in-password')
                                            phone_number_field.clear()
                                            phone_number_field.send_keys(User_input('password'))
                                            phone_number_field.send_keys(Keys.ENTER)
                                        except:
                                            phone_number_field = driver.find_element(By.XPATH, '//*[@id="sign-in-password"]')
                                            phone_number_field.clear()
                                            phone_number_field.send_keys(User_input('password'))
                                            phone_number_field.send_keys(Keys.ENTER)
            except Exception as ex:
                if debug == True:
                    print(ex)
                    print('Элемент для ввода пароля не найден')
            
        