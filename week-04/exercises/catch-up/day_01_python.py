"""Monday exercises. Run this file for examples; import functions for practice."""


def even_in_first_five(numbers):
    # Limit the input first: this is not the first five even matches.
    return [number for number in numbers[:5] if number % 2 == 0]


def name_lists(names):
    first_initials, space_positions, initials = [], [], []
    for name in names:
        # This classroom exercise assumes exactly a first name and surname.
        parts = name.split(' ')
        if len(parts) != 2 or not all(parts):
            raise ValueError('Use a first name and surname separated by one space')
        position = name.index(' ')
        first_initials.append(name[0])
        space_positions.append(position)
        initials.append(name[0] + name[position + 1])
    return first_initials, space_positions, initials


def lists_without_duplicates(groups):
    # The items must be hashable, such as numbers or strings.
    return [group for group in groups if len(group) == len(set(group))]


def parse_over_100(text):
    text = text.strip()
    if not (text.isascii() and text.isdigit()):
        raise ValueError('Enter an unsigned whole number')
    number = int(text)
    if number <= 100:
        raise ValueError('The number must be greater than 100')
    return number


def ask_over_100(read=input, write=print):
    while True:
        try:
            return parse_over_100(read('Whole number greater than 100: '))
        except ValueError as error:
            write(str(error))


def divisors(number):
    if not isinstance(number, int) or isinstance(number, bool) or number < 1:
        raise ValueError('Use a positive integer')
    return [candidate for candidate in range(1, number + 1)
            if number % candidate == 0]


def is_factor(first, second):
    # The lesson asks whether either number is a factor of the other.
    return first in divisors(second) or second in divisors(first)


def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter = letter.lower()
    if len(letter) != 1 or letter not in alphabet:
        raise ValueError('Use one letter A-Z')
    return alphabet.index(letter)


def id_generator(name):
    if not name:
        raise ValueError('Name cannot be empty')
    return ''.join(str(alphabet_position(letter)) for letter in name)


def exercise_password(name):
    # Classroom arithmetic only; this is not a secure password generator.
    identifier = id_generator(name)
    return int(identifier) - sum(int(digit) for digit in identifier)


def is_prime(number):
    if not isinstance(number, int) or isinstance(number, bool):
        raise ValueError('Use an integer')
    if number < 2:
        return False
    for candidate in range(2, number):
        if number % candidate == 0:
            return False
    return True


def lambda_practice():
    # These are worked practice cases; the original lambda worksheet is absent.
    add = lambda first, second: first + second
    savings = [100, 200, 500]
    bonuses = list(map(lambda amount: round(amount * 1.1, 2), savings))
    squares = list(map(lambda number: number ** 2, [1, 2, 3, 4]))
    evens = list(filter(lambda number: number % 2 == 0, range(1, 7)))
    people = sorted([('Ada', 35), ('Alan', 30)], key=lambda person: person[1])
    return add(2, 3), bonuses, squares, evens, people


def main():
    print('Even values in first five:', even_in_first_five([1, 2, 3, 4, 5, 6]))
    print('Name lists:', name_lists(['Ada Lovelace', 'Alan Turing']))
    print('No duplicates:', lists_without_duplicates([[1, 2], [1, 1]]))
    print('Validated input:', parse_over_100('101'))
    print('Divisors of 12:', divisors(12))
    print('9 or 36 a factor of the other:', is_factor(9, 36))
    print('Position of T:', alphabet_position('T'))
    print('Bob ID and exercise password:', id_generator('Bob'), exercise_password('Bob'))
    print('Prime checks:', [(n, is_prime(n)) for n in [1, 2, 7, 9]])
    print('Lambda examples:', lambda_practice())
    # Uncomment to practise interactive input:
    # print(ask_over_100())


if __name__ == '__main__':
    main()
