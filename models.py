# ByteBites backend models
#
# Customer - an app user with a name and purchase history (list of Carts);
#            verified once they have at least one past purchase.
# Item     - a food or drink for sale with a name, price, category string,
#            and a 0-5 star popularity rating.
# Products - the full menu of Items; can filter by category and sort by
#            price or popularity.
# Cart     - one transaction belonging to a Customer; holds the selected
#            Items and computes the total as the sum of their prices.

from __future__ import annotations

import math


class Item:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        if not 0 <= popularity_rating <= 5:
            raise ValueError("popularity_rating must be between 0 and 5")
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Products:
    def __init__(self):
        self.items: list[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def filter_by_category(self, category: str) -> list[Item]:
        # Return a new list of items whose category matches, ignoring case.
        return [item for item in self.items if item.category.lower() == category.lower()]

    def sort_by_price(self) -> list[Item]:
        # Return a new list, lowest price first.
        return sorted(self.items, key=lambda item: item.price)

    def sort_by_popularity(self) -> list[Item]:
        # Return a new list, highest rating first.
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.purchase_history: list[Cart] = []

    def add_purchase(self, cart: Cart) -> None:
        self.purchase_history.append(cart)

    def is_verified(self) -> bool:
        # True once the customer has at least one past purchase.
        return len(self.purchase_history) >= 1


class Cart:
    def __init__(self, customer: Customer):
        self.customer = customer
        self.items: list[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def compute_total(self) -> float:
        # Sum of item prices; 0 for an empty cart.
        return sum(item.price for item in self.items)


if __name__ == "__main__":
    menu = Products()
    burger = Item("Spicy Burger", 8.99, "Entrees", 4.5)
    soda = Item("Large Soda", 2.49, "Drinks", 3.8)
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(Item("Brownie", 3.25, "Desserts", 4.9))
    menu.add_item(Item("Iced Tea", 1.99, "Drinks", 4.1))

    print("Drinks:", [item.name for item in menu.filter_by_category("Drinks")])
    print("drinks:", [item.name for item in menu.filter_by_category("drinks")])
    print("Sides:", [item.name for item in menu.filter_by_category("Sides")])
    print("By price:", [item.name for item in menu.sort_by_price()])
    print("By popularity:", [item.name for item in menu.sort_by_popularity()])
    print("Menu order:", [item.name for item in menu.items])

    customer = Customer("Caleb")
    cart = Cart(customer)
    print("Empty total:", cart.compute_total())
    cart.add_item(burger)
    cart.add_item(soda)
    print("Total:", cart.compute_total())
    print("Total is 11.48:", math.isclose(cart.compute_total(), 11.48))
    print("Verified before:", customer.is_verified())
    customer.add_purchase(cart)
    print("Verified after:", customer.is_verified())
