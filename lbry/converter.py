conversion_dict = {"MPH": 1.60934, "KPH": 0.621371, "KM": 0.621371,
"MI": 1.60934, "Wh_km": 0.1, "Wh_mi": 0.0621371, "CM": 0.393701, "INCH": 2.54}


def executer(value, original, desired):
    resulting_value_and_unit = main_converter(value, original, desired)
    return resulting_value_and_unit


def main_converter(value, original, desired):
    if original == "WH":
        resultkm = float(value) * conversion_dict["Wh_km"]
        resultmi = float(value) * conversion_dict["Wh_mi"]
        printthis = "{0:.2f} watt hours should get you: ".format(float(value)) + "{0:.2f}KM or ".format(resultkm) + "{0:.2f}MI".format(resultmi)
    else:
        result = float(value) * conversion_dict[original]
        printthis = "{0:.2f}".format(result) + desired
    return printthis
