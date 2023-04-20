# Intialzing the city flights
city_flights= input("enter the city name: ")
#Intialising the number of nights staying at hotel
number_of_nights=int(input("enter the number of days staying at hotel:"))
#Intializing the  number of the days hiring a car
rental_days= int(input("Enter the number of tha days will be hirirng a car:"))

# The first function is- Hotel cost ans as to take number of nigths as arugument
def hotel_cost(number_of_nights):
    return (550* ( number_of_nights))
# The second function is- plane cost and as to take city as arugument and return cost flight
def plane_cost(city_flight):
    plane_cost = {"Germany":2500, "Italy":1500, "Switezerland":1200}
    return plane_cost.get(city_flight, 0)
# The  Third function is- Car rental ans as to take rental days as arugument
def car_rental(rental_days):
    return (90* (rental_days))


# The  last function is- Holiday cost ans as to take number of nigtts,city and rentaldays as arugument
def holiday_cost(number_of_nights,city_flight,rental_days):
    cost = (hotel_cost(number_of_nights) + plane_cost(city_flight) + car_rental(rental_days))
    return ("Total Holiday Cost:" + str(cost))
#print holiday_cost 
print(holiday_cost(number_of_nights,city_flights,rental_days) )