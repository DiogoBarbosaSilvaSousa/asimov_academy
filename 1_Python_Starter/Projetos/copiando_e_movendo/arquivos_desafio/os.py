import os

os.getcwd()

os.listdir()

os.listdir('c:\\Users\\datascience\\')

# os.chdir()
actual_dir = os.getcwd()
os.chdir('c:\\Users\\datascience\\')
print(os.getcwd())
os.chdir(actual_dir)

os.mkdir('Pasta')

os.rename('teste.txt', 'teste2.txt')

os.mkdir('Pasta2')

os.mkdir('Pasta3')


#os.rename('Pasta3','Pasta2/Pasta3')
os.rename('Pasta2/Pasta3','Pasta3')
#os.rmdir('Pasta3')