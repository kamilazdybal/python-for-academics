import numpy as np

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Case settings
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Set parameters:
input_variables = [0, 1, 2, 3, 4]
n_epochs = 1000
learning_rate = 0.001
initializer = 'GlorotUniform'
min_random_seed, max_random_seed = (0,10)

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
