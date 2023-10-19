def find_currency( target_value):
    currency = [500, 200, 100, 50, 20, 10, 5,2,1]
    currency_combinations = {}

    for denom in currency:
        if target_value >= denom:
            count = target_value // denom
            target_value %= denom
            if count > 0:
                currency_combinations[denom] = count

    if target_value == 0:
        return currency_combinations

target_value = int(input("Enter the amount: "))
result = find_currency( target_value)
print(result)