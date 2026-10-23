import pytest

from models import Cart, Customer, Item, Products


def make_menu():
    menu = Products()
    menu.add_item(Item("Spicy Burger", 10.00, "Entrees", 4.5))
    menu.add_item(Item("Large Soda", 5.00, "Drinks", 3.8))
    menu.add_item(Item("Brownie", 3.25, "Desserts", 4.9))
    menu.add_item(Item("Iced Tea", 1.99, "Drinks", 4.1))
    return menu


def names(items):
    return [item.name for item in items]


# A $10 burger and a $5 soda in one cart total $15.
def test_calculate_total_with_multiple_items():
    cart = Cart(Customer("Caleb"))
    cart.add_item(Item("Spicy Burger", 10.00, "Entrees", 4.5))
    cart.add_item(Item("Large Soda", 5.00, "Drinks", 3.8))
    assert cart.compute_total() == pytest.approx(15.00)


# A cart with nothing in it totals $0 instead of crashing.
def test_order_total_is_zero_when_empty():
    cart = Cart(Customer("Caleb"))
    assert cart.compute_total() == pytest.approx(0)


# Filtering "Drinks" returns only the drink items.
def test_filter_by_category_returns_only_matching_items():
    assert names(make_menu().filter_by_category("Drinks")) == ["Large Soda", "Iced Tea"]


# Filtering ignores case, so "drinks" matches "Drinks".
def test_filter_by_category_ignores_case():
    assert names(make_menu().filter_by_category("drinks")) == ["Large Soda", "Iced Tea"]


# Filtering a category with no items returns an empty list.
def test_filter_by_category_with_no_matches_is_empty():
    assert make_menu().filter_by_category("Sides") == []


# Sorting by price puts the cheapest item first.
def test_sort_by_price_lowest_first():
    assert names(make_menu().sort_by_price()) == ["Iced Tea", "Brownie", "Large Soda", "Spicy Burger"]


# Sorting by popularity puts the highest-rated item first.
def test_sort_by_popularity_highest_first():
    assert names(make_menu().sort_by_popularity()) == ["Brownie", "Spicy Burger", "Iced Tea", "Large Soda"]


# Sorting returns a new list and leaves the menu's own order alone.
def test_sorting_does_not_change_menu_order():
    menu = make_menu()
    menu.sort_by_price()
    menu.sort_by_popularity()
    assert names(menu.items) == ["Spicy Burger", "Large Soda", "Brownie", "Iced Tea"]


# A customer with no purchases is not verified.
def test_customer_not_verified_without_purchases():
    assert Customer("Caleb").is_verified() is False


# One past purchase is enough to verify a customer.
def test_customer_verified_after_one_purchase():
    customer = Customer("Caleb")
    customer.add_purchase(Cart(customer))
    assert customer.is_verified() is True


# A popularity rating outside 0-5 stars is rejected.
@pytest.mark.parametrize("rating", [-1, 5.1])
def test_item_rejects_rating_outside_zero_to_five(rating):
    with pytest.raises(ValueError):
        Item("Large Soda", 2.49, "Drinks", rating)
