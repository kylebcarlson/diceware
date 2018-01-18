from random import SystemRandom
from nosymbols import nosymbols

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

    print(get_words(get_numbers(), nosymbols))


if __name__ == '__main__':
    run()


