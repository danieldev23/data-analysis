file = open('raw-data.txt', "r")

data = file.readline()

data = data.split("\\n")

for i in range(len(data)):
	data[i] = data[i].replace("\\n", "")
	data[i] = data[i].replace("\\t", "")
# 	data[i] = data[i].replace("\\r", "")

# for j in range(len(data)):
# 	tags =  

file = open('clean.txt', 'w')
for i in range(len(data)):
	file.write(data[i] + "\n")