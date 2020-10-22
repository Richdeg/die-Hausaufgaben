
import numpy

def Metod_Gaussa(arr):
    for k in range(arr.shape[0] - 1):
        #поиск строки с максимальным элементом
        max_elem = 0
        str = 0
        for i in range (k, arr.shape[0]):
            if abs(arr[i,k]) > abs(max_elem):
                max_elem = arr[i,k]
                str = i
        #выход из цикла в случае нулевых значений
        if max_elem == 0: break
        #меняем строки местами
        change = numpy.repeat(arr[k], 1)
        arr[k], arr[str] = arr[str], change
        #делим полученную строку на max_elem
        arr[k] = arr[k] / max_elem
        #домножаем строку на коэффициенты и вычитаем ее из остальных строк
        for i in range (k + 1, arr.shape[0]):
            arr[i] = arr[i] - arr[k] * arr[i,k]
    return arr

#Задаем вещественные матрицы
A = numpy.array([[1.,3,2,-1,-11],[-1,-5,-5,-3,9],[4,0,0,0,-12],[-1,-4,-4,1,18]])
B = numpy.array([[0.,-3,-2,-2,0,4],[1,-4,0,-4,-5,-14],[2,2,1,4,-4,-13],[2,-3,-1,-1,1,-1],[4,-5,-3,-3,4,-1]])

#Вывод на экран
print(Metod_Gaussa(A))
print(" ")
print(Metod_Gaussa(B))

