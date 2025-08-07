
class Validaciones():
    """
    clase con metodos estaticos para validar los datos de entrada
    todos los metodos validan y devuelven el valor convertido al tipo correcto
    """
    @staticmethod
    def es_transporte(modo):
        """
        valida que el modo de transporte sea uno de los permitidos
        """
        modos_validos = ["Automotora", "Ferroviaria", "Aerea", "Navegable"]
        if modo not in modos_validos:
            raise TypeError(f"{modo} no es un modo de transporte válido.")
        return modo

    @staticmethod
    def es_entero(num):
        """
        valida que sea un numero etero
        acepta strings que se puedan convertir a entero 
        """
        if isinstance(num, str):
            try:
                num = float(num)
            except ValueError:
                raise TypeError(f"{num} no es un número válido.")
       
        if isinstance(num, float):
            if not num.is_integer():
                raise TypeError(f"{num} debe ser un número entero.")
            num = int(num)
        elif not isinstance(num, int):
            raise TypeError(f"{num} no es un número.")
       
        return num
   
    @staticmethod
    def es_float_positivo(num):
        """valida que sea un float positivo(incuye 0)"""
        try:
            num_float = float(num)
        except (ValueError, TypeError):
            raise TypeError(f"{num} no es convertible a float.")
       
        if num_float < 0:
            raise ValueError(f"{num_float} no es un float positivo.")
        return num_float
   
    @staticmethod
    def es_natural(num):
        """
        valida que sea un numero natural
        acepta strings que se pueden convertir
        """
        if isinstance(num, str):
            try:
                num = float(num)
            except ValueError:
                raise TypeError(f"{num} no es un número válido.")
       
        if isinstance(num, float):
            if not num.is_integer():
                raise TypeError(f"{num} debe ser un número entero.")
            num = int(num)
        elif not isinstance(num, int):
            raise TypeError(f"{num} no es un número.")
       
        if num < 0:
            raise ValueError(f"{num} no es un natural.")
        return num
   
    @staticmethod
    def es_cad(string):
        """valida que sea una cadena (str)"""
        if not isinstance(string, str):
            raise TypeError(f"{string} no es un string.")
        return string
   
    @staticmethod
    def es_velocidad(vel):
        """
        valida que sea una velocidad valida(numero positivo)"""
        try:
            vel_num = float(vel)
            if vel_num <= 0:
                raise ValueError(f"La velocidad {vel} debe ser positiva.")
            return vel_num
        except (ValueError, TypeError):
            raise TypeError(f"{vel} no es una velocidad válida.")