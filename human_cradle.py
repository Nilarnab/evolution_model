import random
import matplotlib.pyplot as plt

no_of_prog = 3


def get_perc_intel(gen):
    cnt = 0
    for child in gen:
        if child == '11111':
            cnt += 1
        else:
            break

    return cnt*100/len(gen)


def flip_bit(bit, index):
    bit_list = list(bit)
    if bit_list[index] == '0':
        bit_list[index] = '1'
    else:
        bit_list[index] = '0'

    bit = ''.join(bit_list)
    return bit


def eliminate(gen):

    ability = dict()
    survivors = []
    for index in range(len(gen)):
        number = list(gen[index])
        number = [int(i) for i in number]
        one_bits = sum(number)

        ability[index] = one_bits

    ability = sorted(ability.items(), key=lambda x: x[1], reverse=True)

    # print("ability", ability)
    surviving_number = int(3*len(gen) / 4)
    cnt = 0
    for index in ability:
        survivors.append(gen[index[0]])
        cnt += 1
        #if cnt > surviving_number:
        #    break

    return survivors


def get_random_elements(progeny, choices):
    """

    :param progeny:  (list) total available options
    :param choices: (int) total no of choices
    :return: list: choices
    """
    # print("prog", progeny)
    return random.sample(progeny, choices)


def get_a_child(parent1, parent2):
    """

    :param parent1: (str) parent1
    :param parent2: (str) parent2
    :return: returns a child
    """

    # getting a new child without any new character
    parents = [parent1, parent2]
    child = ''
    for i in range(len(parent1)):
        choice = random.randint(0, 1)
        child += parents[choice][i]

    # determining how much change will be there
    # there can be atmost half of length change and at least one change
    no_of_changes = random.randint(1, int(len(parent1) / 4))  # new character
    indices_of_changes = random.sample(range(0, len(parent1)), no_of_changes)

    # setting new changes to the child
    for bit in indices_of_changes:
        child = flip_bit(child, bit)

    return child


def get_next_gen_of_one_family(parent1, parent2):
    children = []
    for choice in range(no_of_prog):
        children.append(get_a_child(parent1, parent2))

    return children


def get_next_gen_raw(prev_gen):
    # making two element pairs
    # making new families
    if len(prev_gen) <= 1:
        return []
    possibilities = [i for i in prev_gen]
    next_population = []
    # print("possibilities", prev_gen)

    while len(possibilities) > 1:
        new_gen = []
        # print("possibilities", possibilities)
        new_possibility = get_random_elements(possibilities, 2)
        # print("new indices", new_indices)
        possibilities.remove(new_possibility[0])
        possibilities.remove(new_possibility[1])

        new_gen.append(get_next_gen_of_one_family(new_possibility[0], new_possibility[1]))

        # print(new_gen)
        for gen in new_gen[0]:
            next_population.append(gen)

    return next_population


gen = ['00111', '00110']
intel = []
index = []
no_of_prog = random.randint(2, 4)
for i in range(15):
    talent = get_perc_intel(gen)
    index.append(i)
    intel.append(talent)
    print("level", i)
    # print(gen)
    gen = get_next_gen_raw(gen)
    length = len(gen)
    print("POPULATION", length)
    gen = eliminate(gen)
    if len(gen) == 0:
        print("SPECIES DID NOT SURVIVE")
        break
    print("percentage intelligent", talent)
    """
    if length != len(gen):
        print("elemination took place")
    else:
        print("no eleminations")
    """

print("final gen", gen)

talent = get_perc_intel(gen)
index.append(i + 1)
intel.append(talent)

cnt = 0
for child in gen:
    if child == '11111':
        cnt += 1
    else:
        break

if len(gen) > 5:
    plt.plot(index, intel)
    plt.show()
print("percentage intelligent", cnt*100/len(gen), "people intelligent", cnt)
