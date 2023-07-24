def count_wo(filename):
    word_c = {}

    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word_c[word] = word_c.get(word, 0) + 1
    return word_c

if __name__ == "__main__":
    filename = "data.txt"
    result = count_wo(filename)

    for word, count, in result.items():
        print(f"{word} : {count}")
