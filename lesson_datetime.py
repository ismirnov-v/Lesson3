from datetime import datetime, date, timedelta
import platform
import locale

if platform.system() == 'Linux':
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF8')
if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, "russian")


str_date = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(str_date, "%d/%m/%y %H:%M:%S.%f")
print('---------------')
print(f'Вывод даты из строки: "{str_date}". \n\tПосле преобразования типа:\n\t{date_dt.strftime("Время: %H:%M:%S.%f Дата: %Y %m %d %A")}\n')
print('---------------')

delta_day = timedelta(days=1)
delta_month = timedelta(weeks=4)
delta_year = timedelta(days=365)

dt_now = datetime.now()
dt_yestarday = dt_now - delta_day
dt_month_before = dt_now - delta_month
dt_year_before = dt_now - delta_year

print(f'Cегодня: {dt_now.strftime("%A %d %B %Y")}')
print(f'Вчера: {dt_yestarday.strftime("%A %d %B %Y")}')
print(f'Месяцем ранее: {dt_month_before.strftime("%A %d %B %Y")}')
print(f'Год назад: {dt_year_before.strftime("%A %d %B %Y")}')