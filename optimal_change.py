from unittest import result


def optimal_change(item_cost:float, amount_paid:float):
    change_due = int(round(amount_paid * 100)) - int(round(item_cost*100))
    result_string = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is "
#The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."

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
        for key in value_to_currency_dict:
            a = change_due // value_to_currency_dict[key]
            # print(key)
            # print (f"a is {a}")

            #exit condition
            if change_due % value_to_currency_dict[key] == 0:
                if a > 1 and key != "penny":
                    result_string += f"and {a} {key}s."
                elif a == 1 and key != "penny":
                    result_string += f"and 1 {key}."
                elif a == 1 and key == "penny":
                    result_string += "and 1 {key}."
                elif a > 1 and key == "penny":
                    result_string += f"and {a} pennies."
            elif  a > 1:

                result_string += f"{int(a)} {key}s, "

            elif a == 1:
                result_string += f"1 {key}, "
            
            change_due = change_due % value_to_currency_dict[key]

    return result_string

