dicionario = {
    1: {
        "nome": "Thiago",
        "email": "thiagohgcoutinho@gmail.com",
        "telefone": "(83) 99144-5979",
        "qualificacao": ["Bombeiro Militar", "Programador"]
    },
    2:{
        "nome": "Luiz",
        "email": "luizcarlos@gmail.com",
        "telefone": "(83) 99999-9999",
        "qualificacao": {
            "graduacao": "Sistemas para Internet",
            "pos": "Segurança de Dados"
        }
    }
}

print(dicionario[1])
print(dicionario[1]["nome"])
print(dicionario[1]["qualificacao"][1])
print(dicionario[2]["qualificacao"]["pos"])