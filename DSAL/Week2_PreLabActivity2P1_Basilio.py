
Q1 = open("Q1.txt", "w+")
Q2 = open("Q2.txt", "w+")
Q3 = open("Q3.txt", "w+")
Q4 = open("Q4.txt", "w+")

files = [Q1, Q2, Q3, Q4]

quarters = [
        ['January', 'February', 'March'],
        ['April', 'May', 'June'],
        ['July', 'August', 'September'],
        ['October', 'November', 'December']
    ]

for i in range(0, 4, 1):
    for j in range(0, 3, 1):
        files[i].write(quarters[i][j])
        files[i].write("\n")
    files[i].close()

Q1 = open("Q1.txt", "r")
Q2 = open("Q2.txt", "r")
Q3 = open("Q3.txt", "r")
Q4 = open("Q4.txt", "r")

files = [Q1, Q2, Q3, Q4]

for i in range(0, len(files), 1):
    print(files[i].read().rstrip())
    files[i].close()


