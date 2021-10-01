key_location = "Chair"
locations = ["Garage", "Living Room", "Chair", "Bathroom", "Garden"]

for i in locations:
    if i == key_location:
        print("Key has been found in :", i)
        break
    else:
        print("Key was not found in :", i)
