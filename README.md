# pizza-calculator
This repository contains my pizza dough calculator depending on the hydration and no. people

## How to use it
You could check the main.py file. Though:
```
from pizza import Pizza

# Initialize the Pizza Obj
mypizza = Pizza(npeople, hydratation) # The class constructor needs two arguments, guest people and dough hydration.

mypizza.get_doughTotalWeightKg() #--> returns the dough total weight considering 250g dough per pizza.
mypizza.get_doughflour() # Amount of flour to use for the dough mixture
mypizza.get_doughH2O()   # Amount of water to use for the dough mixture considering the imposed hydration.
```
