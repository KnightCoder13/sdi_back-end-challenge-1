def find_cheapest(seats_need):
    lowest_price = float('inf')
    lowest_car = None

    cars = [
        {"size": "S", "seats": 5, "price": 5000},
        {"size": "M", "seats": 9, "price": 8000},
        {"size": "L", "seats": 15, "price": 11000}
    ]

    for car in cars:
        cars_need = seats_need // car["seats"]
        if seats_need % car["seats"] > 0:
            cars_need += 1
        price = cars_need * car["price"]
        if price < lowest_price:
            lowest_price = price
            lowest_car = car["size"]

    return cars_need, lowest_car, lowest_price

if __name__ == "__main__":
    while True:
        try:
            seats_need = int(input("Enter number of seats needed: "))
            if(seats_need <= 0):
                print("Please enter a valid number")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
            continue

    cars_need, car, price = find_cheapest(seats_need)
    print(f"{car} x {cars_need}\nTotal = PHP {price}")