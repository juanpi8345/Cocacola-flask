#Para que la fecha de el review sea mas amigable con el usuario
def date_format(value):
    months = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
    month = months[value.month - 1]
    return "{} de {} del {}".format(value.day,month,value.year)