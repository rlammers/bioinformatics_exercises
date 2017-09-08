import copy

def main():
    # We need to get the length of the permutation from file
    with open('sample.in', 'r') as f:
        perm_len = int(f.read())

    # Now we want to generate the initial permutation
    initial_perm = []
    for i in range(perm_len):
        initial_perm.append(i+1)
    all_perms = generate_perms(perm_len, initial_perm)
    print(all_perms)
    # format_and_print(all_perms)


# Heap's algorithm non-recursive
def generate_perms(n, perm_list):
    c = {}

    i = 0
    while i < n:
        c[i] = 0
        i += 1

    all_perms = [copy.deepcopy(perm_list)]

    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                perm_list[0], perm_list[i] = perm_list[i], perm_list[0]
            else:
                perm_list[c[i]], perm_list[i] = perm_list[i], perm_list[c[i]]

            # Add values not references
            all_perms.append(copy.deepcopy(perm_list))

            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return all_perms


def format_and_print(perms):
    print(len(perms))
    for x in perms:
        for y in x:
            print(str(y) + ' ', end='')
        print()


if __name__ == '__main__':
    main()
