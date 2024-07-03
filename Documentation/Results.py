import matplotlib.pyplot as plt

# Sample data for the number of occurrences for each alphabet (A to Z)
alphabets = list("ABCDEFGHIKLMNOPQRSTUVWXY")
frequency = [97, 95, 100, 100, 90, 100, 92, 99, 100, 94, 100, 90, 91, 95, 92, 93, 100, 95, 96, 97, 95, 97, 90, 99]

# Create a bar graph with better aesthetics
plt.figure(figsize=(10, 6))  # Adjust the figure size for better visibility

# Use a horizontal bar graph for better readability
plt.barh(alphabets, frequency, color='skyblue')

# Add labels, a title, and grid for better clarity
plt.xlabel('Accuracy (%)')
plt.ylabel('Alphabets')
plt.title('Accuracy of Recognition for Each Alphabet')
plt.grid(axis='x', linestyle='--', alpha=0.6)

# Display the percentage values on the bars
for i, value in enumerate(frequency):
    plt.text(value, i, f'{value}%', va='center')

# Show the graph
plt.show()

