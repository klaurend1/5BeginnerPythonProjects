print("Enter the photon's frequency here (in Hz): ")

# Get the frequency as input from the user
frequency_input = input("Frequency: ")

# Replace 'x10^' with 'e' and convert to float
frequency_str = frequency_input.replace('x10^', 'e')
frequency = float(frequency_str)

# Planck's constant
h = 6.626e-34

# Calculate the energy of the photon
energy = frequency * h

# Display the result
print("The energy of the photon is:", energy)
