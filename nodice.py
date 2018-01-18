from random import SystemRandom


def build_dict():
    f = open("dicewarewordlist.txt", "r").read().split(' ')
    x = [i for i in f if i != '']

    n = []
    w = []
    for i in x:
        if i.isdigit() and len(i) == 5:
            n.append(i)
        else:
            w.append(i)
    n = [int(i) for i in n]
    diceware = dict(zip(n, w))
    return diceware


def get_numbers():
    numbers = []
    for i in range(7):
        ints = [str(SystemRandom().randint(1,6)) for x in range(5)]
        number = ''.join(ints)
        numbers.append(int(number))
    return numbers


def get_words(nums, diceware):
    words = []
    for k in nums:
        if k in diceware:
            words.append(diceware[k])
    return ' '.join(words)


def run():

    print(get_words(get_numbers(), build_dict()))


if __name__ == '__main__':
    run()


