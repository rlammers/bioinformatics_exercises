import sys


def main(argv):
    if len(argv) == 2:
        with open(argv[0]) as f:
            # Put integer counts into an array
            counts = f.readline().split(sep=' ')
            num_offspring = calc_avg_offspring(counts)
            write_to_file(str(num_offspring), argv[1])
    else:
        print("USAGE: iev inputfile outputfile")
        sys.exit(2)


def calc_avg_offspring(counts):
    dom100_sum = float(counts[0]) + float(counts[1]) + float(counts[2])
    dom75_sum = float(counts[3])
    dom50_sum = float(counts[4])

    offspring100 = dom100_sum * 2
    offspring75 = dom75_sum * 0.75 * 2

    return offspring100 + offspring75 + dom50_sum


def write_to_file(output, outputfile):
    with open(outputfile, 'w') as f:
        f.write(output)

if __name__ == "__main__":
    main(sys.argv[1:])