def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(0 <= entrada <= 24):
                return entrada
            else:
                print("Verifique os valores.")
        except Exception:
            print("A entrada precisa ser um número inteiro.")

def calcula_duracao(h_inicial, h_final):
    duracao = 0
    while(h_inicial != h_final):
        if(h_inicial == 24):
            h_inicial = 0
            if(h_inicial == h_final):
                break
        h_inicial += 1
        duracao += 1
    return duracao

def converte_hora(n):
    h = n // 1
    if(h > 23):
        h -= 24
    sobra_h = n % 1
    m = sobra_h * 60
    min = m // 1
    sobra_min = m % 1
    seg = sobra_min * 60
    if(seg > 30):
        seg = 0
        min += 1
    return [int(h), int(min) , int(seg)]

print("-" * 100)
print(f"{'Esse programa divide um período em quartos de hora.':^100}")
print("-" * 100)

#entradas
hora_inicial = verifica_entrada("Digite a hora inicial(ex: 20): ")
hora_final = verifica_entrada("Digite a hora final(ex: 6): ")
n_militares = verifica_entrada("Digite o número de militares(ex: 5): ")

#calcula a duração do periodo da ronda
duracao = calcula_duracao(hora_inicial, hora_final)
horas_ronda = duracao / n_militares

#divide a hora em h,m e s
hora_por_militar = converte_hora(horas_ronda)

#saida
print("=" * 100)
print(f"Cada militar tirará {hora_por_militar[0]}:{hora_por_militar[1]} h de ronda")
inicio = hora_inicial
final = hora_inicial + horas_ronda
for i in range(n_militares):
    h_inicial = converte_hora(inicio)
    h_final = converte_hora(final)
    print(f"{i + 1} - {h_inicial[0]:02d}:{h_inicial[1]:02d}-{h_final[0]:02d}:{h_final[1]:02d}")
    inicio += horas_ronda
    final += horas_ronda
print("=" * 100)