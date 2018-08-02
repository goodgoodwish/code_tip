
# 8.8 Permutation.

# Prefix

# for i, v in enumerate(char_list):

def perm(prefix, list_chr):
    if len(list_chr) == 1:
        print(prefix + list_chr[0])
    for x in list_chr:
        l_copy = list_chr[:]
        l_copy.remove(x)
        new_prefix = prefix + x
        # print(new_prefix, "".join(l_copy))
        perm(new_prefix, l_copy)

# Insert

def perm_i(list_chr):
    comb_list = perm_i()
    pass

def perm_i_iter(list_chr):
    prev_list = [[]]
    new_list = [[]]
    for end_loc in range(1, len(list_chr)):
        print("Pre str: ", list_chr[0:end_loc])
        prev_list = new_list[:]
        if end_loc == 1:
            prev_list.append([])
            prev_list[0].append(list_chr[0])
        next_char = list_chr[end_loc]
        for i in range(len(prev_list)):
            for insert_loc in range(0, len(prev_list[i])+1):
                new_list = prev_list[i][:]
                new_list.insert(insert_loc, next_char)
                print(new_list)

if __name__ == "__main__":
    # perm("", list("ab"))
    perm_i_iter(list("abc"))


