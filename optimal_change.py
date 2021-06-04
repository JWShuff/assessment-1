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
    # This change_bool flips when our return string is appended to, 
    # used to determine proper string formation when no further change is due
    change_bool = False

    # Catch if no change due or underpaid before further handling.
    if change_due == 0:
        return "No change due."
    elif change_due < 1:
        return "You have underpaid."
    # Need this to catch issues introduced by conversion above to integer values
    elif (amount_paid - item_cost) < .009:
        return "You aren't paying with legal tender."

    # Begin main logic for string generation
    else:
        # From top of currency dict to bottom, evaluate change due against value of a key
        for key in value_to_currency_dict:
            # Tracks the # of bills of a given currency due by taking floor of change divided by value of key 
            a = change_due // value_to_currency_dict[key]
            # EXIT CONDITION
            # (Pennies included, because if first string append op is the final, 
            # it will be pennies or other precise amount of change), and return result_string
            if change_due % value_to_currency_dict[key] == 0:
                if change_bool == False:
                    if a > 1:
                        if key != "penny":
                            result_string += f"{a} {key}s."
                            return result_string
                        else:
                            result_string += f"{a} pennies."
                            return result_string
                    else:
                        result_string += f"{a} {key}."
                        return result_string
                #Appends final string of units to result_string, and returns.
                else:
                    if a > 1 and key != "penny":
                        result_string += f"and {a} {key}s."
                        return result_string
                    elif a == 1 and key != "penny":
                        result_string += f"and 1 {key}."
                        return result_string
                    elif a == 1 and key == "penny":
                        result_string += f"and 1 {key}."
                        return result_string
                    elif a > 1 and key == "penny":
                        result_string += f"and {a} pennies."
                        return result_string
            # Base logic for appending {a} # of $bill/coins that aren't pennies.
            elif  a > 1:
                result_string += f"{a} {key}s, "
                change_bool = True
            elif a == 1:
                result_string += f"1 {key}, "
                change_bool = True
            # Modulo of change_due gives remaining value for which to make change.
            change_due = change_due % value_to_currency_dict[key]
            # Back to top of the For Key loop to begin again.
