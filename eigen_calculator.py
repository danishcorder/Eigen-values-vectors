import numpy as np

def get_eigenvectors_eigenvalues():
    """
    This function calculates eigenvalues and eigenvectors of a given matrix.
    It uses NumPy's linear algebra module for computation.
    """
    # Step 1: Get matrix dimensions from user
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    # Step 2: Validate matrix size
    if rows != cols:
        print("Error: Only square matrices (n x n) can have eigenvalues and eigenvectors.")
        return
    
    # Step 3: Get matrix elements from user
    print(f"Enter {rows}x{cols} matrix elements row-wise:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    
    # Step 4: Convert to NumPy array
    matrix_np = np.array(matrix)
    print("\nInput Matrix:")
    print(matrix_np)
    
    # Step 5: Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix_np)
    
    # Step 6: Format and display results
    print("\nEigenvalues:")
    print(eigenvalues)
    
    print("\nEigenvectors:")
    for i, vec in enumerate(eigenvectors.T):
        print(f"For eigenvalue {eigenvalues[i]}:")
        print(vec)
        print("-" * 30)

# Step 7: Test the function with sample matrices
if __name__ == "__main__":
    print("Testing with 2x2 matrix:")
    get_eigenvectors_eigenvalues()
    
    print("\n\nTesting with 3x3 matrix:")
    get_eigenvectors_eigenvalues()
