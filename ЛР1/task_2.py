# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44  # Информационный объем дискеты в Мб
list_amount = 100  # Количество страниц в книге
string_amount = 50  # Число строк на странице
symbol_amount_at_list = 25  # Количество символов в строке
symbol_storage = 4  # Объем одного символа в байт

book_volume = symbol_storage * symbol_amount_at_list *\
              string_amount * list_amount
volume_in_byte = 1024 ** 2 * volume
books_count = volume_in_byte // book_volume

print("Количество книг, помещающихся на дискету:", int(books_count))
