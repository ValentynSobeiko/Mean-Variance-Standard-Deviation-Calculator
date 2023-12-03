import numpy as np  # Import NumPy Library as np

def calculate(lst):  # Define the calculate Function
    if len(lst) != 9: # Check if the length of the input list is not equal to 9. If it's not, a ValueError is raised.
        raise ValueError('List must contain nine numbers.')

    value = np.array(lst).reshape(3, 3) # Reshape the List to a 3x3 Array

# Calculate Mean, Variance, Standard Deviation, Max, Min, and Sum.

    calc = dict()
    calc["mean"] = [value.mean(0).tolist(), value.mean(1).tolist(), value.mean()]
    calc["variance"] = [value.var(0).tolist(), value.var(1).tolist(), value.var()]
    calc["standard deviation"] = [value.std(0).tolist(), value.std(1).tolist(), value.std()]
    calc["max"] = [value.max(0).tolist(), value.max(1).tolist(), value.max()]
    calc["min"] = [value.min(0).tolist(), value.min(1).tolist(), value.min()]
    calc["sum"] = [value.sum(0).tolist(), value.sum(1).tolist(), value.sum()]

    return calc

# Example Usage
result = calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(result)
