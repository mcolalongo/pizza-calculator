# pizza-calculator
This repository contains my pizza dough calculator depending on the hydration and no. people

## How to use it
You could check the main.py file. Though:

```python
from pizza import Pizza

# Initialize the Pizza Obj
mypizza = Pizza(npeople, hydratation) # The class constructor needs two arguments, guest people and dough hydration.

tot = mypizza.get_doughTotalWeightKg() #--> returns the dough total weight considering 250g dough per pizza.
flour = mypizza.get_doughflour() # Amount of flour to use for the dough mixture
H2O = mypizza.get_doughH2O()   # Amount of water to use for the dough mixture considering the imposed hydration.

# Print all the information needed
mypizza.all_the_ingredients()
```
