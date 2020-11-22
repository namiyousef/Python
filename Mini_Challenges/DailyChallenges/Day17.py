"""
Author: Yousef Nami

Problem definition: This was a question from Hackerrank.

You are given a number of people that need to be shielded from the rain by Umbrellas. You are also
given a list that contains different sizes of umbrellas. You must find the minimum number of umbrellas
needed to shield all the people perfectly.

Example: requirement = 9, umbrellas = [5,4,3, 10]
    the minimum number of umbrellas needed is 2 (5 and 4).
    1 is not correct, because if you use 10 as the umbrella, you are wasting resources / it isn't a perfect
    fit

Date started: 22.11.2020
Date complete:
Results:

"""
from random import randint
def generate_numbers(max_req = 1000, max_list_length = 20, max_umbrella = 800):
    requirement = randint(1,max_req)
    umbrellas = []
    for i in range(randint(1,max_list_length)):
        umbrellas.append(randint(1,max_umbrella))
    return requirement, umbrellas

print(generate_numbers())

def getUmbrellas(requirement, sizes):
    # Write your code here
    sizes.sort(reverse = True)
    print(requirement, sizes)
    return -1 if get_num(requirement, sizes) == 0 else get_num(requirement, sizes)


def get_num(requirement, sizes, n=0):
    # n stores the number that carries forward from before. This is initialised to 0 at first
    c = 0
    for i in range(len(sizes)):
        if requirement % sizes[i] == 0:
            return n + requirement // sizes[i]
        elif requirement > sizes[i]:
            diff = requirement - (requirement // sizes[i]) * sizes[i]
            if diff > 0:
                n += get_num(diff, sizes[i+1:], requirement // sizes[i])
            break

    return n

#print(
#    getUmbrellas(
#        *generate_numbers()
#    )
#)
a = (19, [43, 8,6,3,2,1])
b = (10, [11, 8,3])
c = generate_numbers()
print(
    getUmbrellas(
        *c
    )
)













def recursive_while(max, len_umbs, n = 0, coeffs = []):
    i = 0
    while i <= max:
        if n == len_umbs:
            pass
        else:
            recursive_while(max, n + 1)
    i += 1

def george(target, umbs):
    max = target
    i = 0
    while i <= max:
        j = 0
        while j <= max:
            k = 0
            while k <= max:
                coeffs = [i,j,k]
                counter = 0
                for l in range(0, len(coeffs)):
                    counter += umbs[1] * coeffs[1]
                if counter == target and sum(coeffs) <= max:
                    answer = coeffs
                    max = sum(coeffs)
                k += 1
            j += 1
        i += 1

    try:
        print(answer)
    except:
        print('none found')