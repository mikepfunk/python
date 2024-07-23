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