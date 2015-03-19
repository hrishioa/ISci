def main():
	print "Program Running..."

	inp = "LOLOLOLOLOLOLOL"

	for i in range(0,len(inp)):
		if(inp.lower()[i]=='l'):
			inp =  inp[0:i]+"1"+inp[i+1:len(inp)]
		if(inp.lower()[i]=='o'):
			inp = inp[0:i]+'0'+inp[i+1:len(inp)]

	print inp

if __name__ == '__main__':
	main()

