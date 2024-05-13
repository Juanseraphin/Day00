def miles_converter(distance):
    km = distance * 1.609
    return km

distance_miles = float (input("entrez une distance en miles"))


distancekm = miles_converter(distance_miles)


print (distance_miles, "miles équivaut a", distancekm, "km")