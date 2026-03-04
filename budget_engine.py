def estimate_budget(days, budget_type):
    if budget_type == "Low":
        stay = 1000
        food = 600
    elif budget_type == "Medium":
        stay = 3000
        food = 1200
    else:
        stay = 7000
        food = 2500

    transport = 1000
    daily = stay + food + transport

    return {
        "per_day": daily,
        "total": daily * days
    }