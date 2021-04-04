# 1. Create a greeting for your program.

# 2. Ask the user for the city that they grew up in.

# 3. Ask the user for the name of a pet.

# 4. Combine the name of their city and pet and show them their band name.

# 5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

your_name = input("Enter the name of the city you grew up in.\n")
your_pet = input("Enter the name of a pet.\n")
band_name = your_name + " " + your_pet
print(band_name)
