def print_results(mutations,mutation_type_result):
    if len(mutations) == 0:
        print("\nNo mutations found")
    else:
        print("\nTotal mutations:", len(mutations))
        print("Mutation type:", mutation_type_result)

        for number, mutation in enumerate(mutations, start=1):
            position = mutation[0] + 1
            old_base = mutation[1]
            new_base = mutation[2]

            print("\nMutation", number)
            print("Position:", position)
            print("Change:", old_base, "→", new_base)

#find substitutions
def substitution(original, mutated):
    mutations =[]
    for i in range(len(original)):
        if original[i] != mutated[i]:
            mutations.append((i, original[i], mutated[i]))
    return mutations
#find deletion
def deletion(original, mutated):
    mutations =[]
    i = 0
    j = 0

    while i < len(original) and j < len(mutated):
        if original[i] == mutated[j]:
            i += 1
            j += 1
        else:
            mutations.append((i, original[i], "-"))
            i += 1
    while i < len(original):
        mutations.append((i, original[i], "-"))
        i += 1
    return mutations
        
#INSERTION
def insertion(original, mutated):
    mutations=[]
    i = 0
    j = 0

    while i < len(original) and j < len(mutated):
        if mutated[j] == original[i]:
            i += 1
            j += 1
        else:
            mutations.append((j, "-", mutated[j]))
            j += 1
    while j < len(mutated):
        mutations.append((j, "-", mutated[j]))
        j += 1
    return mutations
    

#return the types
def mutation_type(original, mutated):
    if len(original) == len(mutated):
        return "Substitution"
    elif len(original) > len(mutated):
        return "Deletion"
    else:
        return "Insertion"
    
def analyze_dna(original, mutated):

    original = original.upper()
    mutated = mutated.upper()


    if original =="" or mutated =="":
        print("Error: DNA sequence cannot be empty.")
        return
    valid = "ATGC"

    for letter in original:
        if letter not in valid:
            print("Error: DNA can only contain A, T, G, and C.")
            return

    for letter in mutated:
        if letter not in valid:
            print("Error: DNA can only contain A, T, G, and C.")
            return

    mutation_type_result = mutation_type(original, mutated)
    if mutation_type_result == "Substitution":
        mutations = substitution(original, mutated)
    elif mutation_type_result == "Deletion":
        mutations = deletion(original, mutated)
    else:
        mutations = insertion(original, mutated)
    print_results(mutations,mutation_type_result)


def read_files(filename):
    with open(filename, "r") as file:
        dna = file.read()

        dna = dna.replace("\n", "")
        dna = dna.replace(" ", "")
    return dna.strip().upper()

original = read_files("original.txt")
mutated = read_files("mutated.txt")
analyze_dna(original, mutated)



