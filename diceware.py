from random import SystemRandom
from word_list import word_list


def get_numbers():
    numbers = []
    for _ in range(7):
        ints = [str(SystemRandom().randint(1, 6)) for x in range(5)]
        number = ''.join(ints)
        numbers.append(int(number))
    return numbers


def get_words(nums, word_list):
    words = [word_list.get(number) for number in nums]
    return ' '.join(words)


def run():

    print(get_words(get_numbers(), word_list))


if __name__ == '__main__':
    run()
