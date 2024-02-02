#Question 1
def parallel(resistances):
   
   
    total_inverse_resistance = sum(1 / resistance for resistance in resistances)
    effective_resistance = 1 / total_inverse_resistance

    return effective_resistance

# Example usage:
resistor_values = [330, 1000, 2200]  
result = parallel(resistor_values)
print(f"Effective Resistance: {result} ohms")

#-------------------------------------------------------------
#Question 2
def potential_divider(voltage_supply, resistances):
    

    total_resistance = sum(resistances)
    
    voltage_drops = [voltage_supply * (resistance / total_resistance) for resistance in resistances]

    return voltage_drops

# Example usage:
voltage_supply_value = 9.0  
resistor_values =  [3000, 1000]  
result = potential_divider(voltage_supply_value, resistor_values)
print(f"Voltage Drops Across Resistors: {result} volts")

#----------------------------------------------------------------
#Question 3
def temperature_check(temperature, unit='C'):
    
    

    if unit == 'F':
        temperature = (temperature - 32) * 5/9  # Convert Fahrenheit to Celsius

    if temperature < 35.5:
        return "Hypothermic: The patient has a dangerously low body temperature."
    elif 35.5 <= temperature <= 37.5:
        return "Normal: The patient has a normal body temperature."
    else:
        return "Hyperthermic: The patient has an elevated body temperature."

# Example usage:
patient_temperature = 37.5 
temperature_unit = 'C'  # Replace with 'C' or 'F' based on the temperature unit
result = temperature_check(patient_temperature, temperature_unit)
print(result)
