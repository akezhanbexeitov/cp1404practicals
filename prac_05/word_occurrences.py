from operator import itemgetter


def main():
    my_dict = {}
    text = input("Text: ")
    # text = "this is a collection of words of nice words this is a fun thing it is"
    words = text.split()

    for word in words:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    print(my_dict)

    words = list(my_dict.keys())
    words.sort()
    print(words)

    max_length = max((len(word) for word in words))
    for word in words:
        print("{:{}} : {}".format(word, max_length, my_dict[word]))


if __name__ == '__main__':
    main()