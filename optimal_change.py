from decimal import *
getcontext().prec = 4

def optimal_change(item_cost:float, amount_paid:float):
    change_due = Decimal(amount_paid) - Decimal(item_cost) 
    print(change_due)
    result_string = f"The optimal change for an item that costs {item_cost} with an amount paid of {amount_paid} is "
#The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."

    value_to_currency_dict = {
        '$100 bill': Decimal(100.00), 
        '$50 bill' : Decimal(50.00), 
        '$20 bill' : Decimal(20.00), 
        '$10 bill' : Decimal(10.00),
        '$5 bill' : Decimal(5.00),
        '$1 bill' : Decimal(1.00),
        'quarter' : Decimal(.25),
        'dime' : Decimal(.10),
        'nickel' : Decimal(.05),
        'penny' : Decimal(.01)
    }
    
    # [
    #     (100, "$100 bill"),
    #     (50, "$50 bill"),
    #     (20, "$20 bill"),
    #     (10, "$10 bill"),
    #     (5, "$5 bill"),
    #     (1, "$1 bill"),
    #     (.25, "quarter"),
    #     (.10, "dime"),
    #     (.05, "nickel"),
    #     (.01, "penny")
    # ]

    # Catch if no change due or underpaid before further handling.
    if change_due == 0:
        return "No change due."
    elif change_due < 0:
        return "You have underpaid."
    else:
        for key in value_to_currency_dict:
            a = change_due // value_to_currency_dict[key]
            print(value_to_currency_dict[key])
            print ("a is {a}")
            if a > 1 and value_to_currency_dict[key] != .01:
                result_string += f"{int(a)} {key}s, "

            elif a > 1 and value_to_currency_dict[key] == .01:
                pennies_str = "pennies"
                result_string += f"{int(a)} {pennies_str}"
            elif a == 1 and value_to_currency_dict[key] == .01:
                result_string += f"and {a} {key}"
            elif a == 1:
                result_string += f"1 {key}, "
            change_due = change_due % value_to_currency_dict[key]
            print(result_string)
            print(change_due)
    return result_string


optimal_change(62.13, 100)
