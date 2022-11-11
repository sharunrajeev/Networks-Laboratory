def compressor(data):
	tableSize = 256
	table = {chr(i): i for i in range(tableSize)}

	p = ""
	result = []
	
	for c in data:
		d = p + c
		if d in table:
			p = d
		else:
			result.append(table[p])
			table[d] = tableSize
			tableSize += 1
			p = c
	if p:
		result.append(table[p])
	return result

def decompression(compressed):
	tableSize = 256
	string = ""
	result = ""
	table = {i: chr(i) for i in range(tableSize)}
	for code in compressed:
		if not (code in table):
			table[code] = string + (string[0])
		result += table[code]
		if not(len(string) == 0):
			table[tableSize] = string + (table[code][0])
			tableSize += 1
		string = table[code]
	return result
			

def main():
	string = input("Enter a string: ")
	compressed = compressor(string)	
	print("Compressed data: ", compressed)
	print("Decompressed data: ", decompression(compressed))

main()	