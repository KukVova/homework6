import colorama


attributes_and_methods = dir(colorama)


print(attributes_and_methods)

colorama.init()

# Fore - зміна кольорів тексту
print(colorama.Fore.RED + 'Цей текст червоним кольором' + colorama.Style.RESET_ALL)
print('Цей текст буде в стандартному кольорі')
# Back - змінює колір фону текстів
print(colorama.Back.YELLOW + 'Текст на жовтому фоні' + colorama.Style.RESET_ALL)
print(colorama.Back.BLUE + colorama.Fore.RED + 'Текст на синьому фоні із червоним кольором' + colorama.Style.RESET_ALL)
# Style - вид тектсу
print(colorama.Style.BRIGHT + 'Цей текст жирним шрифтом' + colorama.Style.RESET_ALL)

print(colorama.Style.NORMAL + 'Цей текст нормальний' + colorama.Style.RESET_ALL)
print(colorama.Style.DIM + 'Згаснутий текст' + colorama.Style.RESET_ALL)

print(colorama.Cursor.POS(5, 10) + 'Текст на позиції (5, 10)')
# Очищення екрану
print(colorama.ansi.clear_screen())

colorama.deinit()