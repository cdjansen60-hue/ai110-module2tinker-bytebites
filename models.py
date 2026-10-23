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
        pass

    def filter_by_category(self, category: str) -> list[Item]:
        # Return a new list of items whose category matches.
        pass

    def sort_by_price(self) -> list[Item]:
        # Return a new list, lowest price first.
        pass

    def sort_by_popularity(self) -> list[Item]:
        # Return a new list, highest rating first.
        pass


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.purchase_history: list[Cart] = []

    def add_purchase(self, cart: Cart) -> None:
        pass

    def is_verified(self) -> bool:
        # True once the customer has at least one past purchase.
        pass


class Cart:
    def __init__(self, customer: Customer):
        self.customer = customer
        self.items: list[Item] = []

    def add_item(self, item: Item) -> None:
        pass

    def compute_total(self) -> float:
        # Sum of item prices; 0 for an empty cart.
        pass
