time_records = '1h 45m,360s,25m,30m 120s,2h 60s'  # строка с данными на входе

total_minutes = 0  # счётчик минут

time_entries = time_records.split(',')  # сначала разделим строку по запятым

for entry in time_entries:
    fragments = entry.split()  # теперь результат разбивки по запятым ещё раз поделим, но теперь по пробелам
    
    for fragment in fragments:
        if 'h' in fragment:
            hours = int(fragment.replace('h', ''))  # перевод часов в минуты
            total_minutes += hours * 60
        elif 'm' in fragment:
            minutes = int(fragment.replace('m', ''))  # минуты без перевода, просто добавим в счётчик
            total_minutes += minutes
        elif 's' in fragment:
            seconds = int(fragment.replace('s', ''))  # перевод секунд в минуты
            total_minutes += seconds / 60

total_minutes = int(total_minutes)  # отсечём дробную часть у итогового значения минут

print(total_minutes)  # общее количество минут