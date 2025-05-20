types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def delete_duplicates(tickets_dict):  # удалить дубли, оставив с самым высоким приоритетом
    distinct_tickets = []  # сохранить очищенные от дублей тикеты в новый список 
    result = {}
    
    for priority in sorted(tickets_dict.keys()):  # обработать тикеты по убыванию приоритета
        unique_tickets = []
        for ticket in tickets_dict[priority]:
            if ticket not in distinct_tickets:
                unique_tickets.append(ticket)
                distinct_tickets.append(ticket)
        result[priority] = unique_tickets

    return result

def join_tickets_to_types(types_dict, tickets_dict):  # связать критичность с уникальными тикетами
    filtered_tickets = delete_duplicates(tickets_dict)
    result = {}
    
    for priority, ticket_list in filtered_tickets.items():
        type_name = types_dict[priority]
        result[type_name] = ticket_list
    
    return result

tickets_by_type = join_tickets_to_types(types, tickets)  # получить итоговый словарь
print(tickets_by_type)