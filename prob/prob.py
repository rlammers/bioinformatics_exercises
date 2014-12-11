import sys
import math

def main(argv):
	print("begin")
	if len(argv) == 2:
		dna_and_probs = readInputFile(argv[0])
		logprobs = calculateProbs(dna_and_probs)
		writeProbsToFile(logprobs, argv[1])
	else:
		usage()
		sys.exit(2)

def readInputFile(filename):
	with open(filename) as f:
		dna_string = f.readline().rstrip()
		probs = f.readline().split(' ')
		return [dna_string, probs]

def countGCAT(dna_string):
	gc = dna_string.count('G') + dna_string.count('C')
	at = dna_string.count('A') + dna_string.count('T')
	return [gc, at]

def calculateProbs(dna_and_probs):
	dna_string = dna_and_probs[0]
	probs = dna_and_probs[1]

	gcat_counts = countGCAT(dna_string)
	gc_count = gcat_counts[0]
	at_count = gcat_counts[1]

	results = []
	for prob in probs:
		gc_prob = float(prob)/2
		at_prob = (1-float(prob))/2
		gc_result = gc_prob**gc_count
		at_result = at_prob**at_count
		result = math.log(gc_result * at_result, 10)
		results.append(result)
	return results

def writeProbsToFile(results, outputfile):
	with open(outputfile, 'w') as f:
		f.write(" ".join(format(res, "1.3f") for res in results))

def usage():
	print("USAGE: prob.py inputfile outputfile")

if __name__ == "__main__":
	main(sys.argv[1:])