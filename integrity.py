data = input("Enter data: ")

if data == data[::-1]:
    print("Data Integrity Verified")
else:
    print("Data Corrupted")