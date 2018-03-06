# Battery Converter
# Plan, take in 1) Parallel, 2) Series, 3) Amp Hours of cells, 4) Nominal Voltage of Cells.
# Returns 1) total amp hours, watt hours, range estimates, 


def executer(a, b, c, d):
    input_p, input_s, input_ah, nominal_voltage = a, b, c, d
    nominal_voltage_calculated = float(d)*float(b)
    total_ah, total_wh, range_est_km, range_est_mi = main_battery_function(a, b, c, nominal_voltage_calculated)
    return nominal_voltage_calculated, total_ah, total_wh, range_est_km, range_est_mi


def main_battery_function(a, b, c, d):
    result_ah = float(c)*float(a)
    result_wh = float(result_ah)*float(d)
    result_range_km = float(result_wh)*0.1
    result_range_mi = float(result_wh)*0.0621371
    return result_ah, result_wh, result_range_km, result_range_mi
