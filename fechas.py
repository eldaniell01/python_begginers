from datetime import datetime, timedelta

#optener una fecha y hora actual
print(datetime.now())

#crear una fecha y hora especifica
fecha_especifica = datetime(2025, 1, 12)
print(fecha_especifica)

#formatear fechas
#strftime() para formatear fechas
#parle el objeto datetime y el formato especifico 

format_date = datetime.now().strftime("%d/%m/%Y")
print(format_date)

#operaciones con fechas (sumar y restar dias, minutos, horas, meses)
ayer = datetime.now()-timedelta(days=1)
print(ayer)

mañana = datetime.now()+timedelta(days=1)
print(mañana)

#obtener componentes individuales de una fecha
year = datetime.now().year
print(year)

month = datetime.now().month
print(month)

#calcular la diferencia entre 2 fechas

date1= datetime.now()
date2= datetime(2025, 2, 12, 15, 30, 0)
diferencia = date1 - date2
print(diferencia)