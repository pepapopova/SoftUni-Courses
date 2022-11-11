cat_breed = input()
gender = input()
breed_is_valid = True

if gender == "m":
    if cat_breed == "British Shorthair":
        lifespan = 13
    elif cat_breed == "Siamese":
        lifespan = 15
    elif cat_breed == "Persian":
        lifespan = 14
    elif cat_breed == "Ragdoll":
        lifespan = 16
    elif cat_breed == "American Shorthair":
        lifespan = 12
    elif cat_breed == "Siberian":
        lifespan = 11
    else:
        breed_is_valid = False
        print(f"{cat_breed} is invalid cat!")
elif gender == "f":
    if cat_breed == "British Shorthair":
        lifespan = 14
    elif cat_breed == "Siamese":
        lifespan = 16
    elif cat_breed == "Persian":
        lifespan = 15
    elif cat_breed == "Ragdoll":
        lifespan = 17
    elif cat_breed == "American Shorthair":
        lifespan = 13
    elif cat_breed == "Siberian":
        lifespan = 12
    else:
        breed_is_valid = False
        print(f"{cat_breed} is invalid cat!")

if breed_is_valid:
    lifespan *= 12
    cat_months = lifespan / 6
    print(f"{int(cat_months)} cat months")