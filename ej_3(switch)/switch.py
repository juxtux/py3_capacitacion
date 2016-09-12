__author__ = 'Jorge Monardes'

""" Ejemplo3: switch para Python análogo a código Java:

switch(option){
    case '0':
        return 'Tu opción elegida es el número 0';
    case '1':
        return 'Tu opción elegida es el número 1';
    case '2':
        return 'Tu opción elegida es el número 2';
    case '3':
        return 'Tu opción elegida es el número 3';
    case '4':
        return 'Tu opción elegida es el número 4';
    case '5':
        return 'Tu opción elegida es el número 5';
    default:
        return 'Tu opción elegida no existe! Favor elige número entre 0 y 5';
}

"""

# Utilizando Python3 :

def mySwitch(option):

    opts = {
        "0": "Tu opción elegida es el número 0",
        "1": "Tu opción elegida es el número 1",
        "2": "Tu opción elegida es el número 2",
        "3": "Tu opción elegida es el número 3",
        "4": "Tu opción elegida es el número 4",
        "5": "Tu opción elegida es el número 5"
    }

    return opts.get(option, "Tu opción elegida no existe! Favor elige número entre 0 y 5")


opt = input("Ingresa opción de caso a tu elección entre 0 y 5:")

print(mySwitch(opt))

