#
#
# def wealth_distribution(population, min_wage):
#     if sum(population) < len(population) * min_wage:
#         print("No equal distribution possible")
#     else:
#         for i in range(len(population)):
#             max_wage = max(population)
#             if population[i] < min_wage:
#                 diff = min_wage - population[i]
#                 if max_wage - diff >= min_wage:
#                     population[population.index(max_wage)] -= diff
#                     population[i] = min_wage
#         print(population)
#
#
# data = list(map(int, input().split(", ")))
# current_min_salary = int(input())
# wealth_distribution(data, current_min_salary)

population=[int(x) for x in input().split(", ")]
minimum_wealth=int(input())
for i in range(len(population)) :
    wealthiest=max(population)
    poorest=min(population)
    take_wealth=population.index(wealthiest)
    give_poorest=population.index(poorest)
    population[give_poorest]+=minimum_wealth-poorest
    population[take_wealth]-=minimum_wealth-poorest

if min(population)>=minimum_wealth:
    print(population)
else :
    print("No equal distribution possible")