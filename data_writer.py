def swap_file_data():
    path_to_file1 = input("Enter path to 1st file: ")
    print(path_to_file1)
    print()

    path_to_file2 = input("Enter path to 2st file: ")
    print(path_to_file2)
    print()

    with open(path_to_file1, 'r') as file1_read:
        file1_data = file1_read.read()

        print(f"Data in 1st file : {file1_data}")

    with open(path_to_file2, 'r') as file2_read:
        file2_data = file2_read.read()

        print(f"Data in 2st file : {file2_data}")
    
    with open(path_to_file1, 'w') as file1_write:
        with open(path_to_file2, 'w') as file2_write:
            file1_write.write(file2_data)
            file2_write.write(file1_data)

swap_file_data()
