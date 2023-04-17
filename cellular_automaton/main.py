import numpy as np


def binatodeci(binary):
    return sum(val * (2**idx) for idx, val in enumerate(reversed(binary)))


def update(state: np.ndarray, rule: list):
    new_state = np.zeros_like(state)

    for index in range(2, len(state) - 2):
        input_area = state[index - 1: index + 2]
        pattern_index = 7 - binatodeci(input_area)  # L=8
        new_state[index] = rule[pattern_index]  # apply rule

    return new_state


def wolfram_number_to_rule(number: int):
    rule = list(map(int, bin(number)[2:].rjust(8, '0')))   # TODO: assumes l=8
    return rule


def visualize_state(state: np.ndarray, chars: str = ' X'):
    print(''.join(map(lambda c: chars[c], state)))


if __name__ == '__main__':
    state = np.zeros(84, dtype=np.int8)
    state[42] = 1
    rule = wolfram_number_to_rule(90)

    visualize_state(state)
    for _ in range(40):
        state = update(state, rule)
        visualize_state(state)
