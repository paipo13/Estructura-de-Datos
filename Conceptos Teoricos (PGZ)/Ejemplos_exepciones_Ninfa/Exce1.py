#PRIMERA EXCPECION
x=10000
y=10000

try:
    if x<2000:
        print(x/y)
    else:
        print(x**y)
except ZeroDivisionError as e:
    print('division por CERO')
    print(e)
else:
    print('no hay errores')
    
    