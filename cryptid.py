# prompt user for name, then ask for a number to put after
# each letter.

name = input("Enter your name: ")
cryptid = ''

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
    my_cryptid.display_info()
    
    print(cryptid)