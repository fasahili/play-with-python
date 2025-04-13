def del_dict_element(person, key_to_delete):
    if key_to_delete in person:
        del person[key_to_delete]
        print(f"'{key_to_delete}' was deleted.")
    else:
        print(f"'{key_to_delete}' not found.")

    print("Updated dictionary:", person)


person = {'name': 'John', 'age': 30, 'city': 'London'}
key_to_delete = 'age'
del_dict_element(person, key_to_delete)