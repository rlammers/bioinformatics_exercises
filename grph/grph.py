import sys


def main(argv):
    labels = []
    strings = []
    with open(argv[0]) as f:
        dna_string = ""
        for line in f:
            if line.startswith(">"):
                label = line[1:].rstrip()
                labels.append(label)
                dna_string = ""
            else:
                dna_string += line.rstrip()
                strings.append(dna_string)
                
    for dna in strings:
            dna[-3:]


if __name__ == "__main__":
    main(sys.argv[1:])
