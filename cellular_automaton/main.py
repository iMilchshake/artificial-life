import numpy as np


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


def wolfram_number_to_rule(number: int, r: int):
    rule = list(map(int, bin(number)[2:].rjust(state_count(r), '0')))
    return rule


def visualize_state(state: np.ndarray, chars: str = ' X'):
    print(''.join(map(lambda c: chars[c], state)))


if __name__ == '__main__':
    rule = 90
    r = 2

    state = np.zeros(84, dtype=np.int8)
    state[42] = 1
    rule = wolfram_number_to_rule(rule, r)

    print(rule)

    visualize_state(state)
    for _ in range(20):
        state = update(state, rule, r)
        visualize_state(state)
