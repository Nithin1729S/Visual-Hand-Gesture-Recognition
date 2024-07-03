import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Replace this with your actual data
true_labels = list("abcdefghiklmnopqrstuvwxy")  # Replace with your actual labels
predicted_labels = list("abcdefphiklmncpqraauvwxy")  # Replace with your actual predicted labels

# Create confusion matrix
labels = list(set(true_labels + predicted_labels))
cm = confusion_matrix(true_labels, predicted_labels, labels=labels)

# Plot confusion matrix
fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.matshow(cm, cmap='viridis')
plt.title('Confusion Matrix')
plt.colorbar(cax)

# Add labels to the plot
plt.xticks(np.arange(len(labels)), labels)
plt.yticks(np.arange(len(labels)), labels)

# Add text annotations
for i in range(len(labels)):
    for j in range(len(labels)):
        plt.text(j, i, str(cm[i, j]), ha='center', va='center', color='white' if cm[i, j] > np.max(cm) / 2 else 'black')

plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

