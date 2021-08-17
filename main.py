# coding=utf-8
""" В качестве решения я выбрала способ создания словарей из файла с нормализованными данными.
Для создания словарей я создавала по 2 файла, в первый записывались ненормализованные данные,
во второй результат ручной обработки. Также создала файл с исходными(ненормализованными)
данными и пустой файл для результата.
Для обработки входных данных используется библиотека FlashText, которая позволяет обработать
весь текст и параллельно заменить слова на соответсвующие им ключевые из словаря.
Результаты работы этой библиотеки были записаны в Excel.
В качестве бибилиотеки для записи результата в Excel я использовала Pandas."""
from flashtext import KeywordProcessor
import codecs
import pandas as pd
keyword_processor = KeywordProcessor()
#
# это все для извлечения бренда
#
# Списки для создания словаря брендов, извлекаются из файлов построчно
text1 = []
text2 = []
# Извлекаем строки из файлов и добавляем в списки
lines1 = (line.rstrip('\n') for line in open("text1.txt"))
for line in lines1:
    text1.append(line)

lines2 = (line.rstrip('\n') for line in open("text2.txt"))
for line in lines2:
    text2.append(line)
# Создаем списки списков (в виде [a,[b]]) для создания словаря
company_list = [[] for _ in range(len(text1))]
company_full = [[] for _ in range(len(text1))]

for i in range(len(text1)):
    company_full[i].append(text1[i])
for i in range(len(text1)):
    company_list[i].append(text2[i])
    company_list[i].append(company_full[i])
# Преобразуем в словарь и добавляем в словарь библиотеки FlashText
company_dict = dict(company_list)
keyword_processor.add_keywords_from_dict(company_dict)
# Создаем список для извлечения строк из заданного файла с ненормализованными данными
# для того, чтобы прогнать через библиотеку FlashText и записать "ключевые слова" в итоговый файл с названиями брендов
done_list = []
lines_done = (line.rstrip('\n') for line in codecs.open("done.txt", encoding = 'utf8'))
for line in lines_done:
    done_list.append(line)
# Записываем ключевые слова в файл построчно
with codecs.open("brands_new.txt", 'w') as file:
    for row in done_list:
        brand = keyword_processor.extract_keywords(row)
        file.write('%s\n' % brand)

#
# часть для граммов/литров/штук
#
# определяем новый словарь бибилиотеки FlashText для числовых величин
keyword_for_numbers = KeywordProcessor()
# Списки для создания словаря чисел, извлекаются из файлов построчно
num1 = []
num2 = []
# Извлекаем строки из файлов и добавляем в списки
lines1 = (line.rstrip('\n') for line in open("num1.txt"))
for line in lines1:
    num1.append(line)

lines2 = (line.rstrip('\n') for line in open("num2.txt"))
for line in lines2:
    num2.append(line)
# Создаем списки списков (в виде [a,[b]]) для создания словаря
num_list = [[] for _ in range(len(num1))]
num_full = [[] for _ in range(len(num1))]

for i in range(len(num1)):
    num_full[i].append(num1[i])
for i in range(len(num1)):
    num_list[i].append(num2[i])
    num_list[i].append(num_full[i])
# Преобразуем в словарь и добавляем в словарь библиотеки FlashText
num_dict = dict(num_list)
keyword_for_numbers.add_keywords_from_dict(num_dict)
# Создаем список для извлечения строк из заданного файла с ненормализованными данными
num_done_list = []

lines_done = (line.rstrip('\n') for line in codecs.open("done.txt", encoding = 'utf8'))
for line in lines_done:
    num_done_list.append(line)
# Записываем ключевые слова в файл построчно
with codecs.open("numbers_new.txt", 'w') as file:
    for row in num_done_list:
        numbers = keyword_for_numbers.extract_keywords(row)
        file.write('%s\n' % numbers)

#
# Часть с наименованием товара
#
# определяем новый словарь бибилиотеки FlashText
keyword_for_name = KeywordProcessor()
# Списки для создания словаря наименований, извлекаются из файлов построчно
name1 = []
name2 = []
# Извлекаем строки из файлов и добавляем в списки
lines1 = (line.rstrip('\n') for line in open("name1.txt"))
for line in lines1:
    name1.append(line)

lines2 = (line.rstrip('\n') for line in open("name2.txt"))
for line in lines2:
    name2.append(line)
# Создаем списки списков (в виде [a,[b]]) для создания словаря
name_list = [[] for _ in range(len(name1))]
name_full = [[] for _ in range(len(name1))]

for i in range(len(name1)):
    name_full[i].append(name1[i])
for i in range(len(name1)):
    name_list[i].append(name2[i])
    name_list[i].append(name_full[i])
# Преобразуем в словарь и добавляем в словарь библиотеки FlashText
name_dict = dict(name_list)
keyword_for_name.add_keywords_from_dict(name_dict)
# Создаем список для извлечения строк из заданного файла с ненормализованными данными
name_done_list = []

lines_done = (line.rstrip('\n') for line in codecs.open("done.txt", encoding = 'utf8'))
for line in lines_done:
    name_done_list.append(line)
# Записываем ключевые слова в файл построчно
with codecs.open("name_new.txt", 'w') as file:
    for row in name_done_list:
        names = keyword_for_name.extract_keywords(row)
        file.write('%s\n' % names)

#
# Часть записи в эксель
#
brand = []  #список брендов для записи в эксель
name = []  #список наименований
weight = []  #список веса/объема
# добавляем названия брендов в списки
lines_done = (line.rstrip('\n').rstrip("']").lstrip("['") for line in codecs.open("brands_new.txt", encoding = 'utf8'))
for line in lines_done:
    brand.append(line)
# добавляем названия товаров в списки
lines_done = (line.rstrip('\n').rstrip("']").lstrip("['") for line in codecs.open("name_new.txt", encoding = 'utf8'))
for line in lines_done:
    name.append(line)
# добавляем названия весов/объемов в списки
lines_done = (line.rstrip('\n').rstrip("']").lstrip("['") for line in codecs.open("numbers_new.txt", encoding = 'utf8'))
for line in lines_done:
    weight.append(line)
# создаем список cols для наименования колонок
cols = ['Наименование сокращенное', 'Бренд', 'Наименование из чека', 'Вес/объем']
# создаем список rows, в нем будут содержаться строки, добавляем в него ранее созданные списки с обработанной информацией
rows = [done_list, brand, name, weight]
# в переменную df записываем DataFrame от Pandas
df = pd.DataFrame({
    cols[0]:rows[0],
    cols[1]:rows[1],
    cols[2]:rows[2],
    cols[3]:rows[3]
})
# Записываем в файл эксель
df.to_excel('./normalized.xlsx')
