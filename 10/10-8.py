def readingAndDisplayingAFile(file):
  try:
    with open(file, 'r') as file_object:
      file = file_object.read()
      print(file)
  except FileNotFoundError:
#   print("Извените, указанный файл отсутствует")
    pass

readingAndDisplayingAFile('cats.txt')
readingAndDisplayingAFile('dogs.txt')