from pyDatalog import pyDatalog

sum = 0
for i in range(100):
    sum += i

median_of_numbers = (1/100 * (sum))

pyDatalog.create_terms('Sum_of_numbers, Average_of_numbers,Median_of_numbers,Factorial, N,Prod_series_of_numbers_sqrt')

Factorial[N] = N*Factorial[N-1]
Factorial[1]=1

print((Sum_of_numbers==((0+999999) * 1000000) / 2) # геометрическая прогрессия
& (Average_of_numbers == ((0 + 999999) * 1000000) / 2 / 1000000) # математичкое ожидание, можно рассматривать как арифметическую прогрессию (закон больших чисел)
& (Median_of_numbers == median_of_numbers)
& (Prod_series_of_numbers_sqrt == Factorial[100]))# **10000