#Trip Planner
def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    total = days * 40
    if days >= 7:
        return total - 50
    elif days >= 3 and days < 7:
        return total - 20
    else:
        return total

def spending_money(cash):
    return cash

def trip_cost(city,days,cash):
    return plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(days) + spending_money(cash)
    
print trip_cost("Los Angeles",5,600)