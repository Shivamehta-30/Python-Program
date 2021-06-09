city= {	"Charlotte": 183,"Tampa": 220,"Pittsburgh": 222,"Los Angeles": 475}
print("\t \tWelcom to makemytrip!")
nights = int(input("How many days/night?:"))
days = int(input("How many days of car rental:"))
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    user = input("Which city do you want to visit?:")
    while user not in city:
        user = input("Which city do you want to visit?:")
    return city[user]
def rental_car_cost(days):
        if days >= 7:
            cost = (days * 40)-50
        elif days >= 3:
            cost = (days * 40)- 20
        else:
            cost = days * 40
        return cost
def trip_cost(city, days,):
    print("Total trip cost =",rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city),"$")
trip_cost(city, days)