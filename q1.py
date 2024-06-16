def calculate_probability():
    # Transition probabilities
    P_C_given_P = 0.20  # Probability of switching to Coke given currently Pepsi purchaser
    P_P_given_P = 0.80  # Probability of staying with Pepsi given currently Pepsi purchaser
    
    # Probability of purchasing Coke after 2 purchases from now, given currently Pepsi purchaser
    P_C_after_2_purchases = P_P_given_P * P_C_given_P
    
    return P_C_after_2_purchases

# Calculate the probability
result = calculate_probability()
print("Probability of purchasing Coke after two purchases from now, given currently a Pepsi purchaser:", result)
