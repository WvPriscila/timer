def criar_lista_segundos(total_segundos):
    lista_segundos = []
    if total_segundos == None:
         lista_segundos.append(total_segundos)
         return lista_segundos
    if total_segundos < 0:
        total_segundos = abs(total_segundos)
        while total_segundos >= 60:
            lista_segundos.append(60)
            total_segundos -= 60
        if total_segundos > 0:
            lista_segundos.append(total_segundos)
        return [-x for x in lista_segundos]
    if total_segundos == 0:
        return [0]
    while total_segundos >= 60:
        lista_segundos.append(60)
        total_segundos -= 60
    if total_segundos > 0:
        lista_segundos.append(total_segundos)
    return lista_segundos
ra = criar_lista_segundos(None)
rb = criar_lista_segundos(-199)
rc =  criar_lista_segundos(-19)
rd = criar_lista_segundos(0)
re = criar_lista_segundos(199)
rf = criar_lista_segundos(19) 
print(f" {ra} \n {rb} \n {rc} \n {rd} \n {re} \n {rf} ")
