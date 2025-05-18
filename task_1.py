time_records = '1h 45m,360s,25m,30m 120s,2h 60s'

#Счётчик минут
total_minutes = 0

# Сначала разделим строку по запятым
time_entries = time_records.split(',')

for entry in time_entries:
    # Теперь результат разбивки по запятым ещё раз поделим, но теперь по пробелам
    fragments = entry.split()
    
    for fragment in fragments:
        if 'h' in fragment:
            # Перевод часов в минуты
            hours = int(fragment.replace('h', ''))
            total_minutes += hours * 60
        elif 'm' in fragment:
            # Минуты без перевода, просто добавим в счётчик
            minutes = int(fragment.replace('m', ''))
            total_minutes += minutes
        elif 's' in fragment:
            # Перевод секунд в минуты
            seconds = int(fragment.replace('s', ''))
            total_minutes += seconds / 60

# Отсечём дробную часть у итогового значения минут
total_minutes = int(total_minutes)

print(total_minutes)