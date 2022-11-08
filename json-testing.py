import json

p1 = {
    "John Guzauckas": {"age": 24, "occupation": "teacher"},
    "Emma Guzauckas": {"age": 22, "occupation": "pharmacy technician"},
}
with open("data_file.json", "w") as write_file:
    json.dump(p1, write_file, indent=4)

with open("data_file.json", "r") as read_file:
    p2 = json.load(read_file)

print(p2)
