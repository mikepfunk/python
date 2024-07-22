# prompt user for name, then ask for a number to put after
# each letter.

# not defining cryptid here would result in error

name = input("Enter your name: ")
cryptid = ''
# if I take out the below loop, and do not initialize number, I get an error.

for i in name:
    number = input("Enter a number: ")
    if number == '':
        break
    name = name.replace(i, i + number)
print(name)

class CryptId:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        
    def display_info(self):
        print(f"Name: {self.name}\nNumber: {self.number}")
        # This is how you print each element of a list, using the len function.
        for i in range(len(name)):
            print(name[i])
        
    def counter(self):
        count = 0
        for i in self.name:
            count += 1
        return count
            
    def main():
        name = input("Enter your name: ")
        for i in name:
            number = input("Enter a number: ")
            if number == '':
                break
            name = name.replace(i, i + number)
        print(name)
        
    if __name__ == '__main__':
        main()
        
# Corrected part: This should be outside the class definition
if __name__ == '__main__':
    # Creating an instance of CryptId
    my_cryptid = CryptId(name, number)
    # Calling a method of the instance
    my_cryptid.display_info() # this is calling the display_info method
    print(my_cryptid.counter()) # this will print how many iterations the loop did.