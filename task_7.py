def digit_root(number):
    while number > 9:
        sum_digits = 0  # складывать в эту переменную цифры входного числа
        while number > 0:
            sum_digits += number % 10  # извлекать последнюю цифру 
            number = number // 10         # отбрасывать последнюю цифру от числа
        number = sum_digits
    return number