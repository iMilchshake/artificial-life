import numpy as np

NUM_ITERATIONS = 40


def binatodeci(binary):
    return sum(val * (2**idx) for idx, val in enumerate(reversed(binary)))


def update(state: np.ndarray, rule: list, r: int):
    new_state = np.zeros_like(state)

    for index in range(2, len(state) - 2):
        input_area = state[index - r: index + r + 1]
        pattern_index = state_count(r) - (binatodeci(input_area)+1)
        new_state[index] = rule[pattern_index]  # apply rule

    return new_state


def state_count(r: int):
    return 2**(1 + 2*r)


def wolfram_code_to_rule(number: int, r: int):
    rule = list(map(int, bin(number)[2:].rjust(state_count(r), '0')))
    return rule


def print_state(state: np.ndarray, chars: str = ' X'):
    print(''.join(map(lambda c: chars[c], state)))


if __name__ == '__main__':
    # handle user inputs
    r = int(input('range: '))
    if r > 2 or r < 1:
        raise Exception('range can only be 1 or 2')

    wolfram_code = int(input('wolfram code: '))
    rule = wolfram_code_to_rule(wolfram_code, r)

    initialization = input('initialization method ([S]eed/[R]andom): ')
    if initialization == 'S':
        state = np.zeros(84, dtype=np.int8)
        state[42] = 1
    elif initialization == 'R':
        state = np.random.randint(0, 2, 84)
    else:
        raise Exception('only S and R are valid inputs')

    # run update loop
    print_state(state)
    for _ in range(NUM_ITERATIONS):
        state = update(state, rule, r)
        print_state(state)
