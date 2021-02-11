import csv
import re

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

def get_data(file):
    with open(file, encoding='utf-8') as f_n:
        f_n_reader = f_n.read().split('\n')
        for row in f_n_reader:
            a = re.findall(r'Изготовитель системы:.+?(?=$)', row)
            b = re.findall(r'Название ОС:.+?(?=$)', row)
            c = re.findall(r'Код продукта:.+?(?=$)', row)
            d = re.findall(r'Тип системы:.+?(?=$)', row)

            if a:
                os_prod_list.append(re.split(r':\s+', row)[1])
            if b:
                os_name_list.append(re.split(r':\s+', row)[1])
            if c:
                os_code_list.append(re.split(r':\s+', row)[1])
            if d:
                os_type_list.append(re.split(r':\s+', row)[1])
            
        main_data.append([
            os_prod_list[-1:][0],
            os_name_list[-1:][0],
            os_code_list[-1:][0],
            os_type_list[-1:][0]
        ])

    return main_data

def write_to_csv(file, csv_file):
    with open(csv_file, 'w', encoding='utf-8') as new_file:
        csv_file = csv.writer(new_file)
        for line in get_data(file):
            csv_file.writerow(line)

write_to_csv('info_1.txt', 'main.csv')
write_to_csv('info_2.txt', 'main.csv')
write_to_csv('info_3.txt', 'main.csv')




# re.split('\s+', text)

# g = (re.split(r',', r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'))
# print(g[1])
# text = 'Изготовитель системы:             LENOVO'
# g = (re.split(r':\s+', text))
# print(g[1])