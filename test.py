file1 = open("input.txt", "r+")
file2 = open("Output.txt", "w+")
file3 = open("input2.txt", "r+")
file4 = open("input3.txt", "r+")

data1 = file1.read()
data2 = file2.read()
data3 = file3.read()

file2.write(data1)
file2.write(data2)
file2.write(data3)

file1.close()
file2.close()
file3.close()
file4.close()
