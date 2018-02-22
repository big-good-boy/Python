from collections import OrderedDict

glossary = OrderedDict()

glossary['title'] = 'Первая буква каждого слова - прописная, остальные - строчные'
glossary['upper'] = 'Вся строка прописная'
glossary['lower'] = 'Вся строка строчная'
glossary['rstrip'] = 'Удаление пропусков в конце строки'
glossary['lstrip'] = 'Удаление пропусков в начале строки'
    
for determination in glossary:
    print("\n" + determination + ":\n\t" + glossary[determination])