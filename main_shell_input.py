#!/usr/bin/env python3


from pizza import Pizza, PizzaAbundant

np = int(input("insert the n. of people for the pizza party: "))
hd = int(input("insert the dough hydration (in percentage like 65, 70 or 75...): "))

mypizza = Pizza(np, hd)
#mypizza.all_the_ingredients()
print(f"\npizza for {mypizza.npeople} people and {mypizza.hydr}% hydration")
mypizza.all_table()


morepizza = PizzaAbundant(np, hd)
#morepizza.all_the_ingredients()
print(f"\nfull belly pizza for {mypizza.npeople} same hydration")
morepizza.all_table()
