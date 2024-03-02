def product(lst):
    prod = lst[0]
    for item in lst[1:]:
        prod *= item
    return prod

print(product([1,2,3]))

# 2
def find_min(lst):
    return min(lst)

print(find_min([12,33]))

# 3
def find_primes(lst):
    primes = 0
    is_prime = False # assumption
    for item in lst:
        for i in range(2, item):
            if item % i == 0:
                primes += 1
                break
    return primes

print(find_primes([4, 5, 6, 7]))

# 4
lst = [1, 4, 6, 4, 7, 5, 12]
def remove_num(num):
    counter = 0
    new_lst = []
    for item in lst:
        if item == num:
            counter += 1
        else:
            new_lst.append(item)
    return new_lst, counter

new_list, n_removed_elements = remove_num(4)
print(n_removed_elements)

# 5
def match_lists(lst_1, lst_2):
    new_lst = []
    for item in lst_1:
        if item in lst_2:
            new_lst.append(item)
    return new_lst

print(match_lists([2,4,5], [1,5,4]))

# 6
def power(lst, power):
    new_lst = []
    for item in lst:
        new_lst.append(pow(item, power))
    return new_lst

print(power([2, 3, 4, 5], 3))