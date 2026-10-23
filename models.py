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
