import numpy as np


def binatodeci(binary):
    return sum(val * (2 ** idx) for idx, val in enumerate(reversed(binary)))


def update(state: np.ndarray, rule: list, r: int):
    new_state = np.zeros_like(state)

    for index in range(3, len(state) - 3):
        input_area = state[index - r: index + r + 1]
        pattern_index = state_count(r) - (binatodeci(input_area) + 1)
        new_state[index] = rule[pattern_index]  # apply rule

    return new_state


def state_count(r: int):
    return 2 ** (1 + (2 * r))


def wolfram_code_to_rule(number: int, r: int):
    rule = list(map(int, bin(number)[2:].rjust(state_count(r), '0')))
    return rule


def decimal_values_to_rule(decimal_rules: list, r: int):
    rule = [0 for _ in range(state_count(r))]  # create empty rule
    for value in decimal_rules:
        rule[state_count(r) - (value + 1)] = 1
    return rule


def print_state(state: np.ndarray, chars: str = ' X'):
    print(''.join(map(lambda c: chars[c], state)))

