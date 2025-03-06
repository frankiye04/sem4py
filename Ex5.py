my_dict={"name":"Alice","age":"25","city":"New York"}
print("Dictionary:",my_dict)
key_to_check=input("Enter a key to check:")
if key_to_check in my_dict:
    print(f"Key'{key_to_check}'does not exist in the dictionary.")
    value_to_check=input("Enter a value to check;")
    if value_to_check in my_dict.values():
        print(f"value'{value_to_check}'exists in the dictionary.")
    else:
        print(f"Value'{value_to_check}'does not exist in the dictionary.")