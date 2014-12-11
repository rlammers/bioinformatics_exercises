import sys

def main(argv):
	if len(argv) == 2:
		readInputFile(argv[0])
	else:
		usage()
		sys.exit(2)

def readInputFile(filename):
	with open(filename) as f:
		dna_string = f.readline().rstrip()
		probs = f.readline().split(' ')
	print(dna_string)
	print(probs)

def usage():
	print("USAGE: prob.py inputfile outputfile")

if __name__ == "__main__":
	main(sys.argv[1:])