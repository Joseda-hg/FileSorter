from os import listdir
from os.path import isfile, join, exists
from shutil import move
import timeit

dir = f"C:/Users/mikut/Downloads/Psudo/DevSpace/PythonTestModel/testfold/"
lista = listdir(dir)
print(lista)

# for i in lista:
#     start = timeit.default_timer()
#     move(f"C:/Users/mikut/Downloads/Psudo/DevSpace/PythonTestModel/testfold/{i}",f"C:/Users/mikut/Downloads/Psudo/DevSpace/PythonTestModel/dest/{i}" )
#     stop = timeit.default_timer()
#     execution_time = stop - start
#     print("Executed in", str(execution_time), "seconds")


start = timeit.default_timer()

for i in lista:
    move(f"C:/Users/mikut/Downloads/Psudo/DevSpace/PythonTestModel/testfold/{i}",f"C:/Users/mikut/Downloads/Psudo/DevSpace/PythonTestModel/dest/{i}" )
    
stop = timeit.default_timer()
execution_time = stop - start  
print("Executed in", str(execution_time), "seconds")