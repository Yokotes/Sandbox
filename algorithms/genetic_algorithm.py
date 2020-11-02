import random

# Evolution
def evolution(input_word, final_word):
    current_subject = input_word
    likeness = calc_fitness(current_subject, final_word)
    final_likeness = len(final_word)
    gen = 0

    while likeness != final_likeness:
        current_gen = next_gen(current_subject)
        gen_likeness = []
        print(gen, current_subject)

        for subject in current_gen:
            subject_likeness = calc_fitness(subject, final_word)
            gen_likeness.append(subject_likeness)

        max_likeness = max(gen_likeness)
        likeness = max_likeness
        current_subject = current_gen[gen_likeness.index(max_likeness)]

        gen += 1

    print(current_subject)
    return gen

# Next generation
def next_gen(gen):
    next_gen = [gen for i in range(10)]
    next_gen = mutate(next_gen)

    return next_gen

# Mutate
def mutate(gen):
    mutations = list('abcdefghijklmnopqrstuvwxyz ')
    mutated = gen
    
    for index, subject in enumerate(mutated):
        subject_list = list(subject)

        random_letter = random.randint(0, len(mutations)-1)
        random_pos = random.randint(0, len(subject)-1)

        subject_list[random_pos] = mutations[random_letter]

        subject = ''.join(subject_list)
        mutated[index] = subject

    return mutated

# Calculate fitness
def calc_fitness(word, final_word):
    if (len(final_word) != len(word)):
        return None

    fitness = 0
    for i, w in enumerate(word):
        if w == final_word[i]:
            fitness += 1

    return fitness 
    
    
# Put here input word and final word
evolution('liunhjfqascfd', 'viktor borzov')