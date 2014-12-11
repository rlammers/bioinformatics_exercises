import sys
import math

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
		for prob in probs:
			gc_prob = float(prob)/2
			at_prob = (1-float(prob))/2
			result = math.log(gc_prob**countGC(dna_string)*at_prob**countAT(dna_string), 10)
			print(result)


def countGC(dna_string):
	return dna_string.count('G') + dna_string.count('C')

def countAT(dna_string):
	return dna_string.count('A') + dna_string.count('T')

def usage():
	print("USAGE: prob.py inputfile outputfile")

if __name__ == "__main__":
	main(sys.argv[1:])