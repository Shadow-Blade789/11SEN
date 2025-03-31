# Creating a file
f = open("tasks.txt", "a")
f.write("MathsEx1,31/03/25\n")
f.write("FakeSubject,01/05/25\n")
f.write("Software,04/04/25\n")
f.write("MathsEx2,06/04/25)\n")
f.write("English,08/04/25\n")
f.close()
f = open("tasks.txt", "r")
line1 = f.readline()
print(line1)
f.close()

# try:
#     f = open("tasks.txt", "x")
# except:
#     f = open("tasks.txt", "a")
# Reading a file
f = open("Data/people.txt", "r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()


with open("Data/people.txt", "r") as f:
    line1 = f.readline()
    remaining = f.readlines()

print(line1)
print(remaining)