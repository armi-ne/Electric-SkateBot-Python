def executer(inS, inP, inAh, nomvpc):
    totnomv = inS * nomvpc
    totah, totwh, totrkm, totrmi = main_function(inS, inP, inAh, totnomv)
    return totah, totwh, totrkm, totrmi, totnomv


def main_function(series, parallel, amphour, totalnominalvoltage):
    total_amphour = float(amphour) * float(parallel)
    total_watthours = float(total_amphour) * float(totalnominalvoltage)
    total_range_km = total_watthours * 0.1
    total_range_mi = total_watthours * 0.0621371
    return total_amphour, total_watthours, total_range_km, total_range_mi
