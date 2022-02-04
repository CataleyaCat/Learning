import time
import names
# import random
#
# # 1.Написать скрипт который в создаст список целых чисел.
#
# list_int = list(range(1, 30))
# print(list_int)

# 2. Написать скрипт который в создаст список целых чётных чисел.

# 1 вариант
# list_even = [i for i in range(2,30,2)]
# print(list_even)

# 2 вариант
# list_even = []
# for i in range(1, 30):
#     int = random.randint(0, 100)
#     if int % 2 == 0 :
#         list_even.append(int)

# print(list_even)

# 3.Написать скрипт который в создаст список целых чётных чисел.
# 1 вариант
# list_odd = [i for i in range(1,30,2)]
# print(list_even)

# 2 вариант
# list_odd_ran = []
# for i in range(1, 30):
#     int = random.randint(0, 100)
#     if int % 2 != 0 :
#         list_odd_ran.append(int)
#
# print(list_odd_ran)

# 4.Написать скрипт который из списка целых чисел выведет чётные числа.
# list_even_1 = []
# for i in list_int:
#     int = random.randint(0, 100)
#     if int % 2 == 0 :
#         list_even_1.append(int)
#
# print(list_even_1)

# 5.Написать скрипт который из списка целых чисел выведет нечётные числа.
# list_odd_1 = []
# for i in list_int:
#     if i % 2 != 0 :
#         list_odd_1.append(i)
#
# print(list_odd_1)

# 6.Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.
# list_div_5 = []
# for i in list_int:
#     if i % 5 == 0 and i % 2 ==0:
#         list_div_5.append(i)
#
# print(list_div_5)

# 7. Написать скрипт который из списка целых чисел выведет количество  чётных чисел которые делятся на 5 без остатка.
# list_div_5 = []
# for i in list_int:
#     if i % 5 == 0 and i % 2 ==0:
#         list_div_5.append(i)
#
# print(list_int, len(list_div_5), list_div_5)

# 8.  Написать скрипт который в создаст список целых рандомных чисел.
# list_int_random = []
#
# for i in range(1, 30):
#     int = random.randint(0, 100)
#     list_int_random.append(int)
#
# print(list_int_random)

# 9. Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.



from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/dinka/PycharmProjects/Learning/chromedriver.exe')
driver.get('http://itcareer.pythonanywhere.com/')

name_field = driver.find_element_by_id('name')
name_field.send_keys('Diana')
time.sleep(1)

surname_field = driver.find_element_by_id('surname')
surname_field.send_keys('Kot')
time.sleep(1)

email_field = driver.find_element_by_id('email')
email_field.send_keys('dinkakot1997@gmail.com')
time.sleep(1)

password_field = driver.find_element_by_id('password')
password_field.send_keys('123')
time.sleep(1)

submit_button = driver.find_element_by_tag_name('button')
submit_button.click()
time.sleep(1)

message_path = '/html/body/div[2]/div/div/div/strong'

time.sleep(3)
driver.close();




