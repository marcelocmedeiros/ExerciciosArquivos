'''
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.

O arquivo de entrada possui o seguinte formato:

200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato:

[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256

'''
# open abre o arq. ip.txt com os endereços de entrada como leitura "r"
f=open("D:\Programs\Projects\ListaExercicioPythonBr\ExerciciosArquivos\ip.txt","r")
# crio um lista com método readlines() q retorna o arq todo só que cada linha separada com um valor especifico dentro de uma lsita, ou seja um elemento de uma lista
lista = f.readlines()
# fechei o arq
f.close()
# criei duas listas de IP’s valido e invalido para armazenar depois da verificação
ipvalido = ""
ipnaovalido = ""
# Com For percorro a lista de IP’s gerando a lista2
for i in range (len(lista)):
    # uso método rsplit(“.”) para retirar o ponto a direita dos IP’s
    lista2 = lista[i].rsplit(".")
    # Com If verifico se o IP é válido e adiciono na lista ipvalido se não adiciono na lista ipinvalido
    if (int(lista2[0])<=255 and int(lista2[1])<=255 and int(lista2[2])<=255 and int(lista2[3])<=255):
        ipvalido += lista[i] + "\n" # \n quebra de linha para cada valor add
    else:
        ipnaovalido += lista[i] + "\n" # \n quebra de linha para cada valor add
# com método open crio arq ipvalido.txt no modo escrita
f=open("D:\Programs\Projects\ListaExercicioPythonBr\ExerciciosArquivos\ipvalido.txt","w")
# escrevo
f.write(ipvalido)
# fecho
f.close()
print("IP's Válidos\n",ipvalido)
# com método open crio arq ipinvalido.txt no modo escrita
f=open("D:\Programs\Projects\ListaExercicioPythonBr\ExerciciosArquivos\ipnaovalido.txt","w")
f.write(ipnaovalido)
f.close()
print("IP's Inválidos\n",ipnaovalido)
print ("arquivos gerados com sucesso!")
