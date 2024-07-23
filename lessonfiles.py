count = 0
lines = 0

playwrite = open("romeo.txt", "r")
print(playwrite.read())

# the code is taking in a file, and finding unique words in the file.

# Note here uses playwrite as a variable,
# but it is not a function, it is a file object.
with open("romeo.txt", "r") as playwrite:
    words = playwrite.read().split()
    unique = set(words)
    print(unique)
    
    # Notice here that the file is being read into a list.
with open("romeo.txt", "r") as file:
    for line in file:
        lines = lines + 1
        for word in line.split():
            count = count + 1
            print(word)
            print(count)
            print(lines)
            
# You can split a string into a list of words using split() method.
# The split() method splits a string into a list using a delimiter.
# The default delimiter is whitespace.

# The split() method returns a list of the words in the string, using the " " as the delimiter string.
with open("romeo.txt", "r") as file:
    # The split() method splits a string into a list using a delimiter
    # this will fail without the read() method.
    words = file.read().split()
    print("Words:", words)
    print(words[0])
    print(len(words))