import names

file_path = 'C:/Users/dinka/PycharmProjects/Learning/logs.py'

with open(file_path, 'w') as file_txt:

    while True:
        now = datetime.now()

        user_name = names.get_first_name()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        action_time = time.