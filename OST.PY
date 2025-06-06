def hotel(nights):
    return 140*nights
def plane(city):
    if "charlotte" == city:
        return 183
    elif "tampa" == city:
        return 220
    elif "los angles" == city:
        return 475
    
    def rental(days):
        if days>=3 :
            return 40*days - 50
        elif days>=3 :
            return 40*days
    def cost(city , days, spending):
        return cost (days  )+ hotel(days)+ plane (city)+ rental
    print("cost of car rental:", rental(5))
    print("cost of plane ride:", hotel(7))
    print("total cost of the trip :", cost("los angles ", 7,500))
    print(cost("tampa", 6,500))