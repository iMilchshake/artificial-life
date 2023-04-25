import numpy as np

from cellular_automaton.ca import print_state, update, wolfram_code_to_rule

NUM_ITERATIONS = 40

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
