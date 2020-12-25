def function1():

	f = open("sam.txt","r")
	for line in f.readlines():
		print("-------")
		new_line = line.replace(line,'"'+line.strip("\n")+'",'+"\n")
		print(new_line)
		open("sam2.txt","a").write(new_line)

# a = "aaaaaaaaaabbbbbbbbbcccccccdaldkadla"
# b = a.replace('a','N')
# print(b)
# 
def function2():
	f = open("sam2.txt","r")
	for line in f.readlines():
		print("-------")
		new_line = line.replace(line,line.strip("\n").strip('",')+"\n")
		print(new_line)
		open("sam3.txt","a").write(new_line)

function1()
function2()
