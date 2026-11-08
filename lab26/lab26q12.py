import numpy as np

# Generate random expression values between 0 and 100
gene_expression = np.random.rand(5, 10) * 100

print("Original gene expression matrix:")
print(gene_expression)
row_means = np.mean(gene_expression, axis=1, keepdims=True)

normalized_expression = gene_expression - row_means

print("Row means:")
print(row_means)

print("Normalized gene expression:")
print(normalized_expression)
sample_totals = np.sum(normalized_expression, axis=0)

print("Total expression of each sample:")
print(sample_totals)
threshold = 50

# Identify samples with total expression greater than threshold
selected_samples = sample_totals > threshold

print("Samples exceeding threshold:")
print(selected_samples)

# Get the sample indices
sample_indices = np.where(selected_samples)[0]

print("Sample indices:", sample_indices)