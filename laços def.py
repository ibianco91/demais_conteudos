idades = [15, 18, 25, 50]
def verificacao(idade):
    if idade >= 18:
        print('{} tem permissão para dirigir'.format(idade))  
    else:
        print('{} nao tem permissão para dirigir'.format(idade))  

for idade in idades:
    verificacao(idade)