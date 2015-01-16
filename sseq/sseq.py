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
    if len(dna_strings) != 2:
        print("Do DNA string run multiple lines?")
        sys.exit(2)
    indexes = findsubseq(dna_strings[0], dna_strings[1])
    print_indices(indexes, argv[1])


def findsubseq(s, t):
    indexes = []
    cur_index = 0
    for c in t:
        found_index = s.find(c, cur_index) + 1
        indexes.append(str(found_index))
        if found_index > cur_index:
            cur_index = found_index
    return indexes


def print_indices(index_arr, filename):
    with open(filename, 'w') as f:
        space_sep = " ".join(index_arr)
        print(space_sep)
        f.write(space_sep)

if __name__ == "__main__":
    main(sys.argv[1:])