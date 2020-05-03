import sys

def jaccard(a, b):
    result = len(intersection(a,b))/float(len(union(a,b)))

    return result

def k_shingles(frase, k):
    if k > len(frase):
        return set([frase])
    else:
        shingles = []

        i = 0
        while i+k <= len(frase):
            shingle = frase[i:i+k]
            shingles.append(shingle)
            i += 1
    
    return set(shingles)

def union(a, b):
    result = []

    for item in a:
        result.append(item)
    for item in b:
        result.append(item)

    return set(result)

def intersection(a, b):
    result = []

    for item in a:
        if item in b:
            result.append(item)

    for item in b:
        if item in a:
            result.append(item)

    return set(result)


if __name__ == "__main__":
    a = set([1,2,3])
    b = set([3, 4])
    c = set([1,2,3,5,6,7,8])
    d = set([2,3,8,12,34,56])

    frase = [
            "hola mundo",
            "oh mundo cruel, en el que vive gente asi",
            "cruel es el mundo en donde la gente que vive es asi"
            ]

    print(jaccard(a,b))
    print('Indice de jaccard: ' + str(jaccard(a, b)))
    
    print(k_shingles(frase[0], 5))
    print('K shingles frase 1: ' + str(k_shingles(frase[1], 5)))
    print('K shingles frase 2: ' + str(k_shingles(frase[2], 5)))

    k_frase_1 = k_shingles(frase[1], 5)
    k_frase_2 = k_shingles(frase[2], 5)

    print('Indice de jaccard: ' + str(jaccard(k_frase_1, k_frase_2)))
