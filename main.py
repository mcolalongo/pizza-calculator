#!/usr/bin/env python3


from pizza import Pizza, PizzaAbundant

mypizza = Pizza(15, 70)
#mypizza.all_the_ingredients()
print(f"\npizza for {mypizza.npeople} people and {mypizza.hydr}% hydration")
mypizza.all_table()


morepizza = PizzaAbundant(15, 70)
#morepizza.all_the_ingredients()
print(f"\nfull belly pizza for {mypizza.npeople} same hydration")
morepizza.all_table()
