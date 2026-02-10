from car_management import CarManager

def find_car():
    for detail in CarManager.all_car.values():
        print(detail)
    car_id = input("Enter the car ID: ")
    try:
        return CarManager.all_car[car_id]
    except:
        print(f"Unable to find car {car_id}")

def menu_start():
    while True:
        user_input = input("----  WELCOME  ----\n" +
                            "1. Add a car\n" + 
                            "2. View all cars\n" +
                            "3. View total number of cars\n" +
                            "4. See a car's details\n" +
                            "5. Service a car\n" +
                            "6. Update mileage\n" +
                            "7. Quit\n")
        match user_input:
            case "1":
                inputs = {
                    "make": input("Enter make: "),
                    "model": input("Enter model: "),
                    "year": input("Enter year: "),
                    "mileage": input("Enter mileage: ")
                }
                print("\nAdded car with " + str(CarManager(**inputs)))
            case "2":
                print("\n")
                for detail in CarManager.all_car.values():
                    print(detail)
            case "3":
                print("\n" + f"Total cars: {CarManager.total_cars}")
            case "4":
                print("\n" + str(find_car()))
            case "5":
                print("\n")
                update_car = find_car()
                update_car.add_service(input("\nWhat service should I add? "))
                print("Updated to " + str(update_car))
            case "6":
                print("\n")
                update_car = find_car()
                update_car.update_mileage(input("\nWhat's the new mileage? "))
                print("Updated to " + str(update_car))
            case "7":
                return
            case "":
                return
            case _:
                continue
        input("\n---CONFIRM---")
        print("Thank you!\n")



if __name__ == "__main__":
    menu_start()