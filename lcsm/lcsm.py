import sys


def main(argv):
    dna_strings = []
    with open(argv[0]) as f:
        dna_str = None
        for line in f:
            if line.startswith(">"):
                if dna_str is not None:
                    dna_strings.append(dna_str)
                    dna_str = ""
            else:
                if dna_str is None:
                    dna_str = ""
                dna_str += line.rstrip()
        if dna_str is not None:
            dna_strings.append(dna_str)
    print(dna_strings)


if __name__ == "__main__":
    main(sys.argv[1:])