import numpy as np

from cellular_automaton.ca import decimal_values_to_rule, print_state, update

if __name__ == '__main__':
    r = 3
    rule = decimal_values_to_rule([48, 88, 22, 104, 26, 13], r)

    # test right direction
    state = np.zeros(84, dtype=np.int8)
    state[12] = 1
    state[14] = 1
    state[15] = 1

    # run update loop
    print_state(state)
    for _ in range(20):
        state = update(state, rule, r)
        print_state(state)

    # test left direction
    state = np.zeros(84, dtype=np.int8)
    state[12] = 1
    state[13] = 1
    state[15] = 1

    # run update loop
    print_state(state)
    for _ in range(20):
        state = update(state, rule, r)
        print_state(state)