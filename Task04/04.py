total_number = int(input('Сколько всего журавликов сделали Петя, Катя и Сережа вместе? '))

if total_number%3==0 and total_number%2 == 0:
    petya = (total_number//3)//2
    seryozha = petya
    katya = total_number - petya - seryozha
    print(f'Сережа сделал {seryozha} журваликов, Катя сделала {katya} журавликов, Петя сделал {petya} журавликов.')
else:
    print('Введено неверное количество журавликов.')