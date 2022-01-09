# I found a math problem and then thought it would be
# possible to solve it through a computer simulation,
# so i developed this simulation to solve it.
# The problem is:

# Encontrei um problema matemático e a seguir achei que seria
# possível resolvê-lo através de uma simulação computacional,
# de modo que desenvolvi essa simulação para resolvê-lo.
# O problema é o seguinte:

# T-shirt problem:
#
# In order to make shirt A (sold for 80), a factory uses 1.5 meters of fabric,
# 1.2 hours of cutting and 2 hours of sewing. And to make shirt B (sold for 120),
# a factory spends 2 meters of fabric, 2 hours cutting and 3 hours sewing.
# Taking into account that the factory has 27 meters of fabric, 24 hours of cut and
# 45 hours of sewing per week, what is the ideal number of shirts A and B to be manufactured,
# to make the most profit, assuming all of them will be sold?

# Problema das camisetas:
#
# Para fazer a camisa A (vendida a 80 reais), uma fábrica gasta 1.5 metros de tecido,
# 1.2 horsa de corte e 2horas de costura. Para fazer a camisa B (vendida a 120 reais),
# uma fábrica gasta 2 metros de tecido, 2 horas de corte e 3 horas de costura.
# Levando em conta que que a fábrica dispõe de 27 metros de tecido, 24 horas de corte
# e 45 horas de costura por semana, qual o número ideal de camisas A e B a serem fabricadas,
# para se obter o maior lucro, supondo que todas serão vendidas?

from random import randint

SIMULATIONS = 100000
fabric = 27
cut = 24
sewing = 45
profit = 0
best_profit = 0
list_shirts = []
best_list_shirts = []
shirt_a = 0
shirt_b = 0
counter = 0

# Loop 100,000 simulations.
# Fazer um loop com 100 mil simulações.
for i in range(SIMULATIONS):

# Keep a loop as long as there is material for a shirt (either A or B).
# Manter um loop enquanto houver material para uma camisa (seja A ou B).
    while (fabric >= 1.5 and cut >= 1.2 and sewing >= 2) or (fabric >= 2 and cut >= 2 and sewing >= 3):

# Sort which type of shirt to manufacture A or B, discount the material,...
# ...add the profit, and place the shirt in the appropriate shirt list.
# Sortear qual tipo de camisa fabricar A ou B, descontar o material,...
# ...adicionar o lucro, e colocar a camisa na lista de camisas apropriada.
        r = randint(1, 2)
        if r == 1:
            fabric -= 1.5
            cut -= 1.2
            sewing -= 2
            profit += 80
            list_shirts.append("a")
        else:
            fabric -= 2
            cut -= 2
            sewing -= 3
            profit += 120
            list_shirts.append("b")

# If the profit of the while loop is greater than the biggest profit so far,...
# ...add the profit to the highest profit, and add the t-shirt list to the best list.
# Se o lucro do while loop for maior que maior lucro até o momento,...
# ...adiconar o lucro ao maior lucro, e adicionar a lista de camisetas à melhor lista.
    if profit > best_profit:
        best_profit = profit
        best_list_shirts = list_shirts

# Reset values of variables.
# Reiniciar valores das variáveis.
    list_shirts = []
    profit = 0
    counter += 1
    fabric = 27
    cut = 24
    sewing = 45

# Add best shirt list content to shirt variables.
# Adicionar conteúdo da melhor lista de camisetas às variáveis das camisetas.
for i2 in best_list_shirts:
    if i2 == "a":
        shirt_a += 1
    else:
        shirt_b += 1


