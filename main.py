import json
import pyperclip

with open("parser.json") as data_file:

    env_variables = ""
    vite_imports = {}

    data = json.load(data_file)

    for key, value in data.items():

        if key == "instructions":
            continue

        letters = [l for l in key]
        key_got_insertions = 0

        for index, letter in enumerate(key):

            if letter.isupper():
                letters.insert(index + key_got_insertions, '_')
                key_got_insertions += 1

        key_name = ''.join(letters).upper()
        if type(value) == str:
            value = f"'{value}'"
        env_variables += f"{key_name}={value}\n"
        vite_imports[key] = f"import.meta.env.{key_name}"

if env_variables and vite_imports:
    vite_imports = str(vite_imports).replace("'", "").replace(",", ",\n\t").replace("{", "{\n\t ").replace("}", "\n}")
    print(env_variables)
    print("-"*40, end="\n\n")
    print(vite_imports)

    pyperclip.copy(env_variables)
    pyperclip.copy(vite_imports)

else:
    print("-"*64, "You forgot to enter the data at parser.json :/", "-"*64, sep="\n")
