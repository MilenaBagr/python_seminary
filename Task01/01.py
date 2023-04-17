
km_day = int(input('Введите, сколько км в день вы проезжаете: '))
dist = int(input('Введите, маршрут какой длины вам нужно проехать в км: '))
#days = int(km/km_day + km%km_day)
days = int((km_day + dist - 0.01)//km_day)
print(f'Для того, чтобы проехать {dist} км вам потребуется {days} дней.')