def fahrenheit_to_celsius(temp_f):
    temp_f -= 32
    temp_f *= 5 / 9
    return round(temp_f, 3)
