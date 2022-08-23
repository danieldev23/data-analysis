import subprocess
start = 2000002
end = 2074719
# end = 2000009


file = open("raw-data.txt", "w")

for sbd in range(start, end):
	command = 'curl -F "SoBaoDanh=0' + str(sbd) + '" diemthi.hcm.edu.vn/Home/Show' 
	result = subprocess.check_output(command)

	file.write(str(result) + "\n")