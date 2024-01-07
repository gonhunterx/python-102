# 7% investment return program 

class returnCalculator:
    def __init__(self, inital_investment, annual_rate, years):
        self.inital_investment = inital_investment
        self.annual_rate = annual_rate
        self.years = years
        
    def roi_calc(self): 
        final_calc = self.inital_investment * ((1 + self.annual_rate) ** self.years)

        return final_calc
            
    def display_roi(self):
        calc = self.roi_calc()
        print(f'Return on investment: ${calc:.2f}')

  



def main():
    returnCalc = returnCalculator(1000, .07, 10)
    returnCalc.display_roi()
main()