lista_mercado = []
print("Lista de Mercado")
while True:
    op = int(input("Escolha uma das opção\n \
1 - Adicionar um item\n \
2 - Remover um item\n \
3 - Verficiar a lista\n \
0 - Finalizar\n \
Digite a opção: "))
    if op == 1:
        item = input("Digite um item para adicionar: ")
        lista_mercado.append(item)
    
    elif op == 2:
        item = input("Digite um item para ser removido: ")
        indice_item = lista_mercado.index(item)
        del lista_mercado[indice_item]
    
    elif op == 3:
        for item in lista_mercado:
            print(item)
            
    elif op == 0:
        break