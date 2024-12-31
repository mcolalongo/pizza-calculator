class Pizza:

    def __init__(self, npeople, hydr):
        '''
        The constructor accepts no. of people at dinner and the dough hydration
        '''
        self.hydr = hydr
        self.npeople = npeople

    def get_doughTotalWeightKg(self):
        '''
        Method of Pizza class. It returns the total dough weight considering 0.250Kg per round pizza 

        Returns
        -------
        Total dough weight in Kg

        '''
        return self.npeople * 0.250
        

    def get_doughflour(self):
        '''
        This method calculates the flour to provide in the mixture for the dough preparation considered the hydration  
        Eq considered is: 1x + 0.75x = totalW
                          |     |        |
                       flour + H2O  = dough 
        Returns
        -------
        Total flour weight in kg (float)
        '''
        self.h = self.hydr / 100
        self.flour = self.get_doughTotalWeightKg()/(1 + self.h) # gives me x of the eq, as 1x is flour therefore 
        return self.flour  #in kg


    def get_doughH2O(self):
        '''
        This method calculates the water to provide in the mixture for the dough preparation considered the hydration  
        Eq considered is: 1x + 0.75x = totalW
                          |     |        |
                       flour + H2O  = dough 
        Returns
        -------
        Total H2O weight in kg (float)
        '''
        self.H2O = self.get_doughTotalWeightKg() - self.get_doughflour()
        return self.H2O 

    
    
    def all_the_ingredients(self):
        '''
        This method prints on screen all needed for the dough mixture 

        Returns
        -------
        print string 
        '''

        print('''
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀
            ⠀⠀⠀⠀⠀⠀⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇
            ⠀⠀⠀⠀⠀⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇
            ⠀⠀⠀⠀⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋⠀
            ⠀⠀⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁⠀⠀⠀⠀⠀
            ⠀⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠈⠓⠾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')
        print(f"Tonight you are going to have pizza for {self.npeople} people it seems\nYou selected a dough hydration of {self.hydr}%")
        print("-----------------------------------------------------------------------------------------------------------------")
        print(f"For {self.npeople} people is recommended a dough of {self.get_doughTotalWeightKg():.3f} kg in weight.\nPrepare the right container accordingly")
        print("-----------------------------------------------------------------------------------------------------------------")
        print(f"Out of the total {self.get_doughTotalWeightKg():.3f}kg, {self.get_doughflour():.3f}kg is flour and {self.get_doughH2O():.3f}kg is H2O")
        print("-----------------------------------------------------------------------------------------------------------------")


    def all_table(self):
        '''
        This method prints on screen all needed for the dough mixture but in a small table 

        Returns
        -------
        print all the needed ingredients in table format
        '''
        print("+-----------+-----------+-----------+\n| total(kg) | flour(kg) |  H2O(kg)  |\n+-----------+-----------+-----------+")
        print(f"|   {self.get_doughTotalWeightKg():.3f}   |   {self.get_doughflour():.3f}   |   {self.get_doughH2O():.3f}   |\n+-----------+-----------+-----------+")


class PizzaAbundant:

    """
    Class for full belly pizza. Usually 1 pizza per person is not enough to have, so usually 1.5 pizza per person is a golden rule.
    """
    
    def __init__(self, npeople, hydr):
        '''
        The constructor accepts no. of people at dinner and the dough hydration
        '''
        self.hydr = hydr
        self.npeople = npeople

    def get_doughTotalWeightKg(self):
        '''
        Method of Pizza class. It returns the total dough weight considering 0.250Kg per round pizza 

        Returns
        -------
        Total dough weight in Kg

        '''
        return self.npeople * 0.250 * 1.5
        

    def get_doughflour(self):
        '''
        This method calculates the flour to provide in the mixture for the dough preparation considered the hydration  
        Eq considered is: 1x + 0.75x = totalW
                          |     |        |
                       flour + H2O  = dough 
        Returns
        -------
        Total flour weight in kg (float)
        '''
        self.h = self.hydr / 100
        self.flour = self.get_doughTotalWeightKg()/(1 + self.h) # gives me x of the eq, as 1x is flour therefore 
        return self.flour  #in kg


    def get_doughH2O(self):
        '''
        This method calculates the water to provide in the mixture for the dough preparation considered the hydration  
        Eq considered is: 1x + 0.75x = totalW
                          |     |        |
                       flour + H2O  = dough 
        Returns
        -------
        Total H2O weight in kg (float)
        '''
        self.H2O = self.get_doughTotalWeightKg() - self.get_doughflour()
        return self.H2O 

    
    
    def all_the_ingredients(self):
        '''
        This method prints on screen all needed for the dough mixture 

        Returns
        -------
        print string 
        '''

        print('''
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀
            ⠀⠀⠀⠀⠀⠀⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇
            ⠀⠀⠀⠀⠀⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇
            ⠀⠀⠀⠀⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋⠀
            ⠀⠀⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁⠀⠀⠀⠀⠀
            ⠀⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠈⠓⠾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')
        print(f"Tonight you are going to have ABUNDANT pizza for {self.npeople} people it seems\nYou selected a dough hydration of {self.hydr}%")
        print("-----------------------------------------------------------------------------------------------------------------")
        print(f"For {self.npeople} people is recommended a dough of {self.get_doughTotalWeightKg():.3f} kg in weight.\nPrepare the right container accordingly")
        print("-----------------------------------------------------------------------------------------------------------------")
        print(f"Out of the total {self.get_doughTotalWeightKg():.3f}kg, {self.get_doughflour():.3f}kg is flour and {self.get_doughH2O():.3f}kg is H2O")
        print("-----------------------------------------------------------------------------------------------------------------")


    def all_table(self):
        '''
        This method prints on screen all needed for the dough mixture but in a small table 

        Returns
        -------
        print all the needed ingredients in table format
        '''
        print("+-----------+-----------+-----------+\n| total(kg) | flour(kg) |  H2O(kg)  |\n+-----------+-----------+-----------+")
        print(f"|   {self.get_doughTotalWeightKg():.3f}   |   {self.get_doughflour():.3f}   |   {self.get_doughH2O():.3f}   |\n+-----------+-----------+-----------+")