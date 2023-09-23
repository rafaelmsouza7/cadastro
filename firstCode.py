seunome=input('insira o seu nome:') #a variavel seu nome é o valor de input

print('boas vindas!',seunome,',''como você esta?') #boas vindas para o valor da variavel (seu nome)
print('a=bem b=mal')
a = "bem"
b = "mal"
resposta = input ('digite sua resposta:')
if resposta=='a':
    print('que bom!') #se a resposta for (a) mostre na tela (que bom!)

elif resposta== 'b':
    print("que pena:(") #se a resposta for (b) mostre na tela (que pena!)
idade=int(input('insira sua idade'))
if idade >= 18:
    print('cadastro concluido!')
else:
    print('voce deve ser maior de idade para se cadastrar.Erro!')
    sys.exit()
numerotel=input('insira o seu numero de telefone')
print('insira o codigo de confirmação enviado por sms:'),(input)