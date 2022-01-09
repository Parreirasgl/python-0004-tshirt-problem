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

fabric = 27
cut = 24
sewing = 45
profit = 0
list_shirts = []
best_list_shirts = []
shirt_a = 0
shirt_b = 0

# Loop 100,000 simulations.
# Fazer um loop com 100 mil simulações.
for i in range(100000):

# Keep a loop as long as there is material for a shirt (either A or B).
# Manter um loop enquanto houver material para uma camisa (seja A ou B).
    while (fabric >= 1.5 and cut >= 1.2 and sewing >= 2) \
            or (fabric >= 2 and cut >= 2 and sewing >= 3):

# Sort which type of shirt to manufacture A or B, discount the material,...
# ...add the profit, and place the shirt in the shirt list.
# Sortear qual tipo de camisa fabricar A ou B, descontar o material,...
# ...adicionar o lucro, e colocar a camisa na lista de camisas.
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

