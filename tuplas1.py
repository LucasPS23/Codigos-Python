from operator import pos


lanche = ('hamburguer','pizza','shake','pudim','batata frita') #Tuplas são imutáveis

# Diferentes jeitos de chamar a tupla
#print(len(lanche))

#for comida in lanche:
#    print(f'eu vou comer {comida}')

#for cont in range(0, len(lanche)):
#    print(f'eu vou comer {lanche[cont]}')
#    print(f'eu vou comer {lanche[cont]} na posição {cont}')


#for comida in enumerate(lanche):
#    print(f'eu vou comer {comida} na posição {pos}')
#print('comi muito')

print(sorted(lanche)) #Chama a tupla por ordem alfabetica
print(lanche)