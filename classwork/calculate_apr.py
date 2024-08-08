'''
This is a program that calculates the amount of interest
on your balance on your credit card. The program should 
take in an input for the principal, the interest rate, and
the number of days the balance has been on the card. We
are going to use the formula: (Daily Rate) * 
(Average Daily Balance) * (Number of Days in Billing Cycle)

FYI ** I think the math is off, I am not 100% on how you
would calculate the interest on a credit card. But for
these purposes, it will work.

We also have to calculate the daily rate, which is the
interest rate divided by 365. The average daily balance
is the sum of the daily balances divided by the number of
days in the billing cycle. The daily balance is the
balance at the end of the day. The APR is the annual
percentage rate, which is the interest rate times the
number of days in the billing cycle. The APR is the
amount of interest you will pay on your balance.

This program will demonstrate how to make a class, called
CreditCard, that will calculate the interest on your 
credit card. The class will have the following 
methods:
'''

# This is a class that calculates the interest on a credit card
class CreditCard:
    def __init__(self, principal, rate, time):
        # Initialize the CreditCard object with principal, rate, and time
        self.principal = principal  # Store the principal amount
        self.rate = rate  # Store the interest rate
        self.time = time  # Store the number of days in the billing cycle
    
    # This is a method that gets the values of the class
    def get_values(self):
        try:
            self.principal = float(input("Enter the principal amount: "))
            self.rate = float(input("Enter the annual interest rate (as a percentage): "))
            self.time = float(input("Enter the time in years: "))
            return True
        except ValueError:
            return False
        
    # This is a method that gets the principal
    # When I had the input in each method, it
    # would return it after each input.
    # By calling it in the __init__ method, it
    # will only return the value once.
    def get_principal(self):
        #self.principal = float(input("Enter the principal: "))
        return self.principal
    
    # This is a method that gets the interest rate
    def get_rate(self):
        #self.rate = float(input("Enter Your Interest rate: "))
        return self.rate
    
    # This is a method that gets the number of days in the billing cycle
    def get_time(self):
        #self.time = float(input("Enter Days in your Billing Cycle: "))
        return self.time
    
    # This is a method that calculates the daily interest rate
    def daily_rate(self):
        return self.rate / 365
    
    # This is a method that calculates the APR
    def calc_apr(self):
        if not self.validate_inputs():  # Revalidate inputs before calculation
            return "Please Enter a valid input"
        # Calculate the APR - Don't need finally or else
        return self.principal * self.daily_rate() * self.time
    
    # This is a method that returns a string representation of the class
    def __str__(self):
        #return "The interest on your balance is: " + str(self.calc_apr())
        return (f"CreditCard(principal={self.principal}, rate={self.rate}, "
                f"time={self.time}, daily_rate={self.daily_rate()}, "
                f"Amount Owed={self.calc_apr()})")
        
    # This is a method that checks for errors in the input
    # and returns a boolean value
    def validate_inputs(self):
        try:
            if not isinstance(self.principal, (int, float)) or self.principal <= 0:
                raise ValueError("Principal must be a positive number.")
            if not isinstance(self.rate, (int, float)) or self.rate <= 0:
                raise ValueError("Rate must be a positive number.")
            if not isinstance(self.time, (int, float)) or self.time <= 0:
                raise ValueError("Time must be a positive number.")
        except ValueError as e:
            print(f"Input validation error: {e}")
            return False
        return True
        
    # This is a method that prints the values of the class
    def print_check(self):
        print(f"Principal:  {self.get_principal()}")
        print(f"Rate:  {self.get_rate()}")
        print(f"Time:  {self.get_time()}")
        print(f"Daily Rate:  {self.daily_rate()}")
        print(f"Amount Owed:  {self.calc_apr()}")
        
    def convert_to_dict(self):
        # Convert the CreditCard object attributes to a dictionary format
        return {
            "principal": self.principal,
            "rate": self.rate,
            "time": self.time,
            "daily_rate": self.daily_rate(),
            "Amount Owed": self.calc_apr()
        }

'''
# How do I create an object of a class?  An object is like a variable.
# How do I access the class and print these values? 
# How do I call the methods in a class?
#
# Here is how you create an object of a class and call
# the methods in the class.

# This is the main function and
# it is the entry point of the program
#
# So we ask for the users input, then they are passed
# to the CreditCard class, by creating an object of the
# class, called card.
'''


def main():
    # Create an object of class CreditCard with dummy initial values
    card = CreditCard(0, 0, 0)
    # Loop until valid inputs are provided
    while True:
        # Get input from the user and update the card object
        if not card.get_values():
            print("Invalid inputs. Please try again, enter a number greater than"
                " zero.\n")
            continue
        
        # Validate inputs which will check for errors
        try:
            card.validate_inputs()
        except ValueError as e:
            print(e)
            continue
        
        # If inputs are valid, break out of the loop
        break
    
    # Put values in a dictionary.
    card_dict = card.convert_to_dict()
    print(card_dict)
    
    # Print the values and the calculated APR
    card.print_check()
    print(card)

if __name__ == "__main__":
    main()