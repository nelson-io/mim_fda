# -*- coding: utf-8 -*-

def divisors(n):
    """Obtiene una lista con los divisores del parametro n
    

    Parameters
    ----------
    n : int
        Número natural del cual queremos obtener sus divisores

    Returns
    -------
    x : list
        Lista con todos los divisores del parámetro n.
        
        Si el parámetro n no es natural se arroja un error indicando
        que el parámetro no es un número natural

    """
    if n<0:
        raise ValueError('El parámetro n debe ser un número natural, no'
              ' puede ser negativo')
    
    elif isinstance(n, int) == False:
        raise ValueError('El parámetro n debe ser un número natural, debe ser entero')
    
   
    else:
        
        x = [i for i in range(1,int(n/2)+1) if n % i == 0]
        return x






def is_prime(x):
    """Función auxiliar de es_primo()"""
    if x == 1:
        return False
    elif len(divisors(x)) <= 1:
        return True
    else:
        return False

def es_primo(n):
    """Indica si un número es primo o no
    

    Parameters
    ----------
    n : int
        Número natural que nos interesa saber si es primo o no.

    Returns
    -------
    x : NoneType
        Se devuelve el print "sí" en la caso de que el parametro "n" sea
        primo y el string "no" en caso de que no lo sea.
        
        Si el parámetro n no es natural se arroja un error indicando
        que el parámetro no es un número natural        
        

    """
    
    if is_prime(n):
        return 'sí'
    else:
        return 'no'



def prime_numbers(i):
    """Función auxiliar de iesimo_primo()"""
    
    x = []
    n = 2
    while len(x) < i:
        if is_prime(n):
            x.append(n)
        n += 1
    return x
        
    



def iesimo_primo(i):
    """ Devuelve el i-esimo número primo consultado
    

    Parameters
    ----------
    i : int
        i-esimo número primo que deseo consultar

    Returns
    -------
    x : int
        i-esimo número primo.

    """
    
    x = prime_numbers(i)
    return x[-1]
        

    
    
    
    
    
    
    
    
    
    
    
    
    
