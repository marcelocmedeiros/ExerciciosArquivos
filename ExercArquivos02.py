'''
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

    alexandre       456123789
    anderson        1245698456
    antonio         123456456
    carlos          91257581
    cesar           987458
    rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
----------------------------------------------------------------
Nr.  Usuário        Espaço  utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
'''

def conversao(num):
    return ((num/1024)/1024)

def percentual(lista,num):    
    return ((float(num)*100)/sum(lista))

f=open("usuarios.txt","r")
lista = f.readlines()
f.close()
# variável result vai cria o formato da tabela
result="ACME Inc.               Uso do espaço em disco pelos usuários\n"
result+="----------------------------------------------------------------\n"
result+="Nr.\tUsuário\t\tEspaço utilizado\t% do uso\n"

# para fazer a tabela temos que add o obj interavel com For em cada listas especificas
listaUsuario=[]
listaEspaco=[]
listaUtilizacao=[]

for i in lista:
    listaUsuario.append(i[0:16]) # add usuario
    listaEspaco.append(conversao(int(i[16:]))) # add espaço que chama def conversão 

for i in range (len(listaUsuario)):
    # add  utilizacao que chama def persentual
    listaUtilizacao.append(percentual(listaEspaco, listaEspaco[i])) 
    # variável result add uma linha a cada laço For 
    result += str(i+1) + "\t" + listaUsuario[i]  +  str("%.2f" %(listaEspaco[i])) + "\tMB" + "\t\t" + str("%.2f" %(listaUtilizacao[i])) + "\n"

print (result)
