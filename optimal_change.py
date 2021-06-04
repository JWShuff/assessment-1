def optimal_change(item_cost, amount_paid):

    # Convert our change_due to an int by moving our input values two decimal places to the right
    change_due = int(round(amount_paid * 100)) - int(round(item_cost*100))

    # Result string with entry string interpolation:
    result_string = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is "

    # This dict must be in greatest to least bill order with current key search logic.
    value_to_currency_dict = {
        '$100 bill': 10000,
        '$50 bill' : 5000,
        '$20 bill' : 2000,
        '$10 bill' : 1000,
        '$5 bill' : 500,
        '$1 bill' : 100,
        'quarter' : 25,
        'dime' : 10,
        'nickel' : 5,
        'penny' : 1,
    }

    # Catch if no change due or underpaid before further handling.
    if change_due == 0:
        return "No change due."
    elif change_due < 0:
        return "You have underpaid."
    else:
        counter = 0
        for key in value_to_currency_dict:
            a = change_due // value_to_currency_dict[key]

            #exit condition
            if change_due % value_to_currency_dict[key] == 0:
                if counter == 0:
                    if a > 1:
                        if key != "penny":
                            result_string += f"{a} {key}s."
                        else:
                            result_string += f"{a} pennies."
                    else:
                        result_string += f"{a} {key}."
                else:
                    if a > 1 and key != "penny":
                        result_string += f"and {a} {key}s."
                    elif a == 1 and key != "penny":
                        result_string += f"and 1 {key}."
                    elif a == 1 and key == "penny":
                        result_string += f"and 1 {key}."
                    elif a > 1 and key == "penny":
                        result_string += f"and {a} pennies."

            elif  a > 1:
                result_string += f"{a} {key}s, "
                counter += 1
            elif a == 1:
                result_string += f"1 {key}, "
                counter += 1

            change_due = change_due % value_to_currency_dict[key]
            

    return result_string

