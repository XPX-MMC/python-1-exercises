def f_to_c(f):
    c = round((f - 32) * 5/9)
    return f"{f} degrees Fahrenheit is {c} degrees Celsius"

#print(f_to_c(22))

def c_to_f(c):
    f = round((c * 9/5 )+ 35)
    return f" {c} degrees Celsius is {f} degrees Fahrenheit"

#print(c_to_f(-6))