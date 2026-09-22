def search(arr, employeeID, index):
    if index == len(arr):
        return -1

    if arr[index] == employeeID:
        return index

    return search(arr, employeeID, index + 1)


employees = [101, 205, 310, 415, 520]

employeeID = int(input("Enter Employee ID: "))

result = search(employees, employeeID, 0)

if result != -1:
    print("Employee ID found at index", result)
else:
    print("Employee ID not found")