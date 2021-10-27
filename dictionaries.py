#Dictionaries are special structures in python which allow to store information in key-value pairs

monthConversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}

monthConversionsByNumbers = {
    "01" : "January",
    "02" : "February",
}

print(monthConversions["Aug"])
print(monthConversions.get("Luv", "Not a valid Key")) #Second parameter is the default value in case the key is not found
print(monthConversionsByNumbers.get("02", "Number out of range"))