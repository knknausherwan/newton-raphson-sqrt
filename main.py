# Newton-Raphson for square root
k = 24  # Value to find the square root of
steps = 0
epsilon = 0.01  # Tolerance level for accuracy
guess = k / 2  # Initial starting guess

# Loop until the guess is close enough to the actual square root
while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k) / (2 * guess))
    steps += 1

print('Square root of', k, 'is about', guess, 'and it took about', steps, 'steps')
