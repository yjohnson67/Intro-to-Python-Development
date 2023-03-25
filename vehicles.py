def main():
    #Create a dictionary that contains data about six vehicles.
    #The key for each vehicle in the dictionary is the vehicle's
    #identification number (VIN). The value for each vehicle is
    #A list that contains the year, manufacturer, model, color,
    #engine design, and engine displacement.
    vehicles_dict = {
        # VIN: [year, manufacturer, model, color, eng_design, eng_displace]
        "1J4GL48K4UF993861": [2002, "Jeep", "Liberty", "blue", "V6", 3.7],
        "1YVGF22C8AN381568": [2002, "Mazda", "626", "white", "I4", 2.0],
        "WP0AA0926HG410293": [1987, "Porsche", "924S", "red", "I4", 2.5],
        "5TDZA23CXTU102983": [2006, "Toyota", "Sienna", "gold", "V6", 3.3],
        "1GKKVRED5ZL382610": [2011, "GMC", "Acadia", "charcoal", "V6", 3.5],
        "2T3BF4DV9QR146782": [2012, "Toyota", "RAV 4", "green", "I4", 2.5]
    }

    MANUFACTURER_INDEX = 1
    MODEL_INDEX = 2
    COLOR_INDEX = 3

    

    #Keep asking the user for a vehicle indentification number (vin) unitl a valid one is given.
    while True:
    #Ask the user for a vehicle identification number (VIN).
        vin = input("Please enter a VIN: ")

    #Check if the vin is a key that is in the vehicles dictionary.
        if vin in vehicles_dict:


        #Find the data for the vehicle that the user wants.
            vehicle_data = vehicles_dict[vin]
        
            #Print the manufacturer, model, and color of the vehicle.
            #Don't print the year, engine design, or displacement.
            print(f"Manufacturer: {vehicle_data[MANUFACTURER_INDEX]}")
            print(f"Model: {vehicle_data[MODEL_INDEX]}")
            print(f"Color: {vehicle_data[COLOR_INDEX]}")

            #break out of the loop since a valid VIN was entered.
            break
        else:
            #Print a message stating that the VIN entered
            #By the user is not in the dictionary.
            print(f"{vin} is not in the dictionary.")

            #Continue the loop to ask the user for another vin.
            continue

#If this file was executed like this:
#> python teach_solution.py
#Then call the main function. However, if this file
#Was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()