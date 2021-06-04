def optimal_change(item_cost, amount_paid):

    no_change_due = "No change due."
    change_due = amount_paid - item_cost    
    result_string = f"The optimal change for an item that costs {item_cost} with an amount paid of {amount_paid} is "
    # Catch if no change due before further handling.
    if change_due == 0:
        return no_change_due
    elif change_due < 0:
        return "You have underpaid."
    print(result_string)
    return result_string