


## Programa de Cálculo de Teto de Gastos Anual

Este programa calcula o prejuízo anual de uma empresa baseado nos gastos e um teto de gastos estipulados pelo usuário. O objetivo é auxiliar no monitoramento financeiro ao longo de um período definido de anos, considerando também a inflação anual.

# Funcionalidades
1. Entrada de dados pelo usuário sobre o número de anos e o teto de gastos.
2. Cálculo dos gastos totais da empresa por ano, incluindo investimentos, despesas, e custos.
3. Verificação se os gastos totais excederam o teto de gastos estipulado.
4. Aplicação da inflação anual ao teto de gastos para o próximo ano.
5. Saída dos resultados, que pode ser exibida na tela ou salva em arquivos CSV.

# Dependências
Este programa não requer bibliotecas externas além do Python padrão. Ele utiliza as seguintes funções e métodos embutidos:
print(),
input(),
open(),
write().

# Instruções para Uso

Execute o script Python em um ambiente que suporte entrada e saída padrão, como um terminal.


# Entrada de Dados
O usuário será solicitado a fornecer:
1. A quantidade de anos para calcular os prejuízos.
2. O teto de gastos anual.
3. Os gastos anuais em investimentos, despesas, e custos de produção e serviço.

# Processamento
O programa calcula os gastos totais a cada ano e verifica se estes excedem o teto de gastos.
Se os gastos totais ultrapassarem o teto, o excesso é considerado como prejuízo e adicionado aos gastos do próximo ano.
A inflação anual é aplicada ao teto de gastos para o próximo ano, considerando uma média de 13,1%.

# Saída de Dados 
O usuário pode escolher entre exibir os resultados na tela ou salvar os resultados em arquivos CSV (teto_gastos.csv e gastos_totais.csv).

