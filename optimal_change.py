def optimal_change(item_cost, amount_paid):

    no_change_due = "No change due."
    change_due = amount_paid - item_cost    
    result_string = f"The optimal change for an item that costs {item_cost} with an amount paid of {amount_paid} is "
#The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."

    value_to_currency_dict = {
        '$100 bill': 100, 
        '$50 bill' : 50, 
        '$20 bill' : 20, 
        '$10 bill' : 10,
        '$5 bill' : 5,
        '$1 bill' : 1,
        'quarter' : .25,
        'dime' : .10,
        'nickel' : .05,
        'penny' : .01
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
        return no_change_due
    elif change_due < 0:
        return "You have underpaid."
    
    print(value_to_currency_map)
    print(result_string)
    return result_string

optimal_change(100,200)