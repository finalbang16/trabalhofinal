print("Bem vindo ao software de cálculo de teto de gastos anual.\n")
print("Esse software foi desenvolvido com o intuito de facilitar o cálculo de prejuízo de uma empresa durante uma certa quantidade de anos estipulada pelo usuário.\n")

#entrada de dados: anos_total = o usuário indica a quantidade de anos
#teto_gastos = o usuário indica o gasto máximo da empresa por iteração
#gastos_investimento, gastos_despesas, gastos_custos, gastos_total = todos os gastos a serem considerados por iteração
#prejuizo = caso os gastos ultrapassem o teto, o prejuízo será adicionado aos gastos totais do próximo ano.
#inflacao = calculando com base nos ultimos 20 anos, o resultado aproximado
#flag_teto_est = identificador se o teto de gastos foi estourado ou não durante o ano
#tela_sim = string que define que o usuário prefere ver os resultados na tela
#tela_nao = string que define que o usuário prefere ver os resultados em um documento .csv
#tela_ou_arq = string definindo como o usuário receberá os resultados.

anos_total = int(input('Digite a quantidade de anos que deve ser calculado se a empresa teve prejuízo ou não. '))
teto_gastos = float(input('Digite o teto de gastos do ano especificado.\n'))
i = 1
aux = 0

arq_teto = open("teto_gastos.csv", "w")
arq_teto.write("Ano,Teto de Gastos\n")
arq_gastos = open("gastos_totais.csv", "w")
arq_gastos.write("Ano,Gastos Totais,Gastos de Investimento,Gastos de Despesas,Gastos de Produção e Serviço,Prejuízo\n")
flag_teto_est = 0
tela_sim = "S"
tela_sim2 = "s" #para checar caracteres minusculos
tela_nao = "N"
tela_nao2 = "n" #para checar caracteres minusculos

#processamento de dados

while (i <= anos_total): #o código será executado enquanto i=1 for menor ou igual a quantidade de anos estipulada pelo usuário
  print("Teto de gastos do ano {0}: {1}".format(i, teto_gastos))
  tela_ou_arq = input("Os resultados devem ser informados na tela? 'S' para sim e 'N' para nao, n escrevera os resultados em um documento .csv")

  # Loop para garantir que o usuário insira uma opção válida
  while (tela_ou_arq != tela_sim) and (tela_ou_arq != tela_sim2) and (tela_ou_arq != tela_nao) and (tela_ou_arq != tela_nao2):
    tela_ou_arq = input("Os resultados devem ser informados na tela? 'S' para sim e 'N' para nao, n escrevera os resultados em um documento .csv")

  gastos_investimento = float(input('Digite os gastos da empresa com investimentos diretos, como cursos e treinamento de colaboradores.\n'))
  gastos_despesas = float(input('Digite os gastos de manutenção e administração da empresa, como limpeza, aluguel e materiais necessários para o funcionamento.\n'))
  gastos_custos = float(input('Digite os gastos de matéria prima e salário de colaboradores da empresa.\n'))
  gastos_total = (gastos_investimento) + (gastos_despesas) + (gastos_custos) #cálculo do total de gastos
  prejuizo = 0
  aux = teto_gastos

  if (teto_gastos < gastos_total):
    prejuizo = gastos_total - teto_gastos
    flag_teto_est = 1

  if (tela_ou_arq == tela_sim) or (tela_ou_arq == tela_sim2): #comparação de strings para definir a saída de dados necessária
    print("Gastos totais do ano {0}: {1}\n".format(i,gastos_total)) #saída de dados 1
    print("Gastos de investimento: {0}\n".format(gastos_investimento))
    print("Gastos de desespesas: {0}\n".format(gastos_despesas))
    print("Gastos de produção e serviço: {0}\n".format(gastos_custos))
    if (flag_teto_est == 1):
      print("O teto de gastos da empresa foi ultrapassado no ano {0} por {1} reais".format(i, prejuizo))

  elif (tela_ou_arq == tela_nao) or (tela_ou_arq == tela_nao2):
    arq_teto.write("{0},{1}\n".format(i, teto_gastos))
    arq_gastos.write("{0},{1},{2},{3},{4},{5}\n".format(i, gastos_total, gastos_investimento, gastos_despesas, gastos_custos, prejuizo))

  inflacao = ((aux * 13.1) / 100) #considerando que a inflação dos últimos 20 anos foi 252%, a média inflacional por ano é de 13.1%
  # porém, isso não reflete o valor real da inflação considerando que é um número aleatório a cada ano
  teto_gastos += inflacao #esse cálculo adiciona a inflação ao teto de gastos inicial, para saber qual será o teto de gastos no próximo ano
  i+=1 #iteraçao
  gastos_total += prejuizo

arq_gastos.close()
arq_teto.close()

