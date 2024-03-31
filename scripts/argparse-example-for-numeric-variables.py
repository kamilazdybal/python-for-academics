import numpy as np
import argparse

def argument_parser():

    parser = argparse.ArgumentParser()

    parser.add_argument('--input_variables',
                        type=int,
                        default=[0,1,2,3,4],
                        nargs="+",
                        help='Indices for the input variables')

    parser.add_argument('--n_epochs',
                        type=int,
                        default=1000,
                        help='Number of epochs')

    parser.add_argument('--learning_rate',
                        type=float,
                        default=0.001,
                        help='Learning rate')

    parser.add_argument('--initializer',
                        type=str,
                        default='GlorotUniform',
                        help='Initialization of weights')

    parser.add_argument('--random_seeds',
                        type=int,
                        default=[0,10],
                        nargs="+",
                        help='Min and max random seed')

    parser.add_argument('--decay',
                        type=bool,
                        default=False,
                        action=argparse.BooleanOptionalAction,
                        help='Use learning rate decay')

    return parser

parser = argument_parser()

args = parser.parse_args()

print(args)

print()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Case settings
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Populate parameter values from argument parser:
input_variables = vars(args).get('input_variables')
n_epochs = vars(args).get('n_epochs')
learning_rate = vars(args).get('learning_rate')
initializer = vars(args).get('initializer')
min_random_seed, max_random_seed = tuple(vars(args).get('random_seeds'))
decay = vars(args).get('decay')

print(decay)

print()

# List of random seeds to loop over:
random_seeds_list = [i for i in range(min_random_seed, max_random_seed)]

# Names of input variables:
input_names = np.array(['X' + str(i+1) for i in range(0,10)])

# Create a tag for this training session:
case_run_name = 'inputs-' + '-'.join(input_names[input_variables]) + '-n-epochs-' + str(n_epochs) + '-lr-' + str(learning_rate) + '-initializer-' + initializer

print(case_run_name)

print()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Neural network training with the current parameters starts here...
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

for i in random_seeds_list:

    print('Training session for random seed ' + str(i) + '...')

    # ...

    # ...

    # ...

print()
