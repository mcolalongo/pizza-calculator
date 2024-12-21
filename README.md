# pizza-calculator
This repository contains my pizza dough calculator depending on the hydration and no. people

## How to use it
You could check the main.py file. Though:

```python
from pizza import Pizza

# Initialize the Pizza Obj
mypizza = Pizza(npeople, hydratation) # The class constructor needs two arguments, guest people and dough hydration.

tot = mypizza.get_doughTotalWeightKg() # Returns the dough total weight considering 250g dough per pizza.
flour = mypizza.get_doughflour() # Amount of flour to use for the dough mixture
h2o = mypizza.get_doughH2O()   # Amount of water to use for the dough mixture considering the imposed hydration.

# Print all the information needed
mypizza.all_the_ingredients()
```

However, by experience, for a full belly and satisfying pizza for the guests x1 pizza per person is not sufficient. Better to use the PizzaAbundant() class
Therefore:
```python
from pizza import PizzaAbundant

# Initialize the Pizza Obj
mypizza = PizzaAbundant(npeople, hydratation) # The class constructor needs two arguments, guest people and dough hydration.

tot = mypizza.get_doughTotalWeightKg() # Returns the dough total weight considering 250g dough per pizza.
flour = mypizza.get_doughflour() # Amount of flour to use for the dough mixture
h2o = mypizza.get_doughH2O()   # Amount of water to use for the dough mixture considering the imposed hydration.

# Print all the information needed
mypizza.all_the_ingredients()
```
