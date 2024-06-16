# Importing numpy for matrix operations
import numpy as np

# Transition matrix based on the given probabilities
P = np.array([
    [0.9, 0.1],  # Transition probabilities for Coke today
    [0.2, 0.8]   # Transition probabilities for Pepsi today
])

# Initial state vector (today is Pepsi purchaser)
initial_state = np.array([0, 1])  # [P(Pepsi today), P(Coke today)]

# Function to perform matrix-vector multiplication
def matrix_vector_multiply(matrix, vector):
    return np.dot(matrix, vector)

# Calculate state after one purchase
state_tomorrow = matrix_vector_multiply(P, initial_state)

# Calculate state after two purchases
state_day_after_tomorrow = matrix_vector_multiply(P, state_tomorrow)

# Probability of purchasing Coke after two purchases from now
prob_coke_after_two_purchases = state_day_after_tomorrow[0]
# Probability of purchasing Pepsi after two purchases from now
prob_pepsi_after_two_purchases = state_day_after_tomorrow[1]

# Print the results
print(f"The probability of purchasing Pepsi after two purchases from now, given that the person is currently a Coke purchaser, is: {prob_coke_after_two_purchases:.2f}")
print(f"The probability of purchasing Pepsi after two purchases from now, given that the person is currently a Pepsi purchaser, is: {prob_pepsi_after_two_purchases:.2f}")

# Now calculate for initial state of Coke purchaser
initial_state_coke = np.array([1, 0])  # [P(Coke today), P(Pepsi today)]

# Calculate state after one purchase
state_tomorrow_coke = matrix_vector_multiply(P, initial_state_coke)

# Calculate state after two purchases
state_day_after_tomorrow_coke = matrix_vector_multiply(P, state_tomorrow_coke)

# Probability of purchasing Coke after two purchases from now
prob_coke_after_two_purchases_coke = state_day_after_tomorrow_coke[0]
# Probability of purchasing Pepsi after two purchases from now
prob_pepsi_after_two_purchases_coke = state_day_after_tomorrow_coke[1]

# Print the results
print(f"The probability of purchasing Coke after two purchases from now, given that the person is currently a Coke
       purchaser, is: {prob_coke_after_two_purchases_coke:.2f}")
print(f"The probability of purchasing Coke after two purchases from now, given that the person is currently a Pepsi 
      purchaser, is: {prob_pepsi_after_two_purchases_coke:.2f}")
