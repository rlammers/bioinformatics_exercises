def main():
    # We need to get the length of the permutation from file
    with open('sample.in', 'r') as f:
        perm_len = int(f.read())

    # Now we want to generate the initial permutation
    initial_perm = []
    for i in range(perm_len):
        initial_perm.append(i+1)
    all_perms = []
    generate_perms(perm_len, initial_perm, all_perms)


# Heap's algorithm
def generate_perms(n, perm_list, all_perms):
    if n == 1:
        all_perms.append(perm_list)
    else:
        for i in range(0, n - 1):
            generate_perms(n - 1, perm_list, all_perms)
            if n % 2 == 0:
                perm_list[i], perm_list[n - 1] = perm_list[n - 1], perm_list[i]
            else:
                perm_list[0], perm_list[n - 1] = perm_list[n - 1], perm_list[0]
        generate_perms(n - 1, perm_list, all_perms)

    print(all_perms)


if __name__ == '__main__':
    main()
