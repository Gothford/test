def month_name(nmbr,lang):
    rumonth=['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
    engmonth=['january','february','march','april','mai','june','july','august','september','october','november','december']
    if 'ru' in lang:
        return rumonth[nmbr-1]
    else:
        return engmonth[nmbr-1]

print(month_name(3,'eng'))
