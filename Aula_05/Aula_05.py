t = str(" Aula 01 ")
print(f"{t:=^20}")
idade = int(input("Digite sua idade:"))
if idade >= 18:
    print("Pode entrar na festa!!!")
elif 16 <= idade < 18:
    print("É hora de voltar para casa!")
else:
    print("Vou chamar seus pais.")