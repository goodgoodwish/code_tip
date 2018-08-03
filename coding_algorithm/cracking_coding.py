
# 8.8 Permutation.

# Prefix, Recursive

# for i, v in enumerate(char_list):

def perm(prefix, list_chr, new_list=[]):
    if len(list_chr) == 1:
        print(prefix + list_chr[0])
        new_list.append(prefix + list_chr[0])
    else:
        for x in list_chr:
            l_copy = list_chr[:]
            l_copy.remove(x)
            new_prefix = prefix + x
            print(x, new_prefix, "".join(l_copy))
            perm(new_prefix, l_copy, new_list)
    return new_list

# Insertion, Recursive

def perm_i(list_chr):
    comb_list = perm_i()
    pass

# Insertion, Iterative

def perm_i_iter(list_chr):
    prev_list = [[list_chr[0]],]
    new_list = []
    for step_loc in range(1, len(list_chr)):
        print("next step: ", step_loc, list_chr[step_loc])
        next_char = list_chr[step_loc]
        for p_idx in range(0, len(prev_list)):
            print(f"prev {p_idx} {prev_list[p_idx]} ")
            for insert_loc in range(0, len(prev_list[p_idx])+1):
                new_one = prev_list[p_idx][:]
                new_one.insert(insert_loc, next_char)
                print(f"new one: {new_one}")
                new_list.append(new_one)
        prev_list = new_list[:]
        new_list = []
    new_list = ["".join(xs) for xs in prev_list]
    return new_list

if __name__ == "__main__":
    # new_list = perm("", list("abc"), [])
    new_list = perm_i_iter(list("abc"))
    print(new_list)
