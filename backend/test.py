import json

# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     }
# }
#
#
# with open("data_file.json", "w") as write_file:
#     json.dump(data, write_file)
#
# with open("data_file.json") as read_file:
#     data_new = json.load(read_file)
#
# print(data_new)

# username = input("Введите имя: ")
#
# with open("data_file.json", "w", encoding="utf-8") as write_file:
#     json.dump(username, write_file, ensure_ascii=False)
#     print("Вас зовут:" + username)
#
# with open("data_file.json") as read_file:
#     data_new = json.load(read_file)
#     print("Добро пожаловать,"+ data_new + "!")


filename = "user.json"
try:
    with open(filename) as read_file:
        data_new = json.load(read_file)
        print("Добро пожаловать," + data_new + "!")
except:
    username = input("Введите имя: ")
    with open(filename, "w", encoding="utf-8") as write_file:
        json.dump(username, write_file, ensure_ascii=False)
        print("Вас зовут:" + username)
