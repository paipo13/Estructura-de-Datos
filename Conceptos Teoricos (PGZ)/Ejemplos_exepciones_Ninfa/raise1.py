def dividir(num,deno):
    try:
        
        if deno==0:
            raise TypeError('Error porque se dividirá por cero')
        else:
            return(num/deno)
    except Exception as e:
        print(f'Error: {e}')

dividir(4,3)
dividir(4,0)
dividir(4,'3')

     