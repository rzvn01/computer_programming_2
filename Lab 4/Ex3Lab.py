n = input("How many beers? : ")

beer_dictionary = {}

for i in range(int(n)):
    name = input("Beer Name: ")
    price = float(input("Beer price:"))
    quality = int(input("Beer Quality (0-5):"))
    beer_dictionary[name] = {
        "Price": price,
        "Quality": quality,
        "Quality for Money": quality / price
    }


sorted_beers = sorted(beer_dictionary.items(), key=lambda item: item[1]["Quality for Money"], reverse=True)

if sorted_beers:
    print("\nBeers sorted by Quality for Money:")
    for name, beer_info in sorted_beers:
        print(f"{name}, Quality for Money: {beer_info['Quality for Money']}")

    cheapest_beer = min(beer_dictionary.items(), key=lambda item: item[1]["Price"])
    worst_beer = min(beer_dictionary.items(), key=lambda item: item[1]["Quality"])

    print(f"\nThe Cheapest Beer is {cheapest_beer[0]}, Price: {cheapest_beer[1]['Price']}")
    print(f"The Worst Beer is {worst_beer[0]}, Quality: {worst_beer[1]['Quality']}")
else:
    print("No beers to display.")
