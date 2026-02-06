import numpy as np
def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    
    print(f"Enter elements row-wise for {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    
    return np.array(matrix)
def display_matrix(title, matrix):
    print(f"\n{title}")
    print(matrix)
while True:
    print("\n===== Matrix Operations Tool =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

    choice = int(input("Choose an operation: "))

    if choice == 1:
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        if A.shape == B.shape:
            result = A + B
            display_matrix("Addition Result:", result)
        else:
            print("Matrices must have same dimensions!")

    elif choice == 2:
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        if A.shape == B.shape:
            result = A - B
            display_matrix("Subtraction Result:", result)
        else:
            print("Matrices must have same dimensions!")

    elif choice == 3:
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        if A.shape[1] == B.shape[0]:
            result = np.dot(A, B)
            display_matrix("Multiplication Result:", result)
        else:
            print("Columns of A must equal rows of B!")

    elif choice == 4:
        A = input_matrix("Matrix")
        result = A.T
        display_matrix("Transpose Result:", result)

    elif choice == 5:
        A = input_matrix("Matrix")
        if A.shape[0] == A.shape[1]:
            result = np.linalg.det(A)
            print("\nDeterminant:", result)
        else:
            print("Determinant only for square matrices!")

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
