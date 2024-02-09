# Create a list
original_list = [1, 2, 3, 4, 5]

# Copy the list using the slice function
copied_list = original_list[:]

# Modify the copied list to demonstrate independence
copied_list.append(6)

# Display the original and copied lists
print("Original list:", original_list)
print("Copied list:", copied_list)
