# ByteBites UML Design

```mermaid
classDiagram
    class Customer {
        +name: str
        +purchase_history: list~Cart~
        +add_purchase(cart: Cart) None
        +is_verified() bool
    }

    class Item {
        +name: str
        +price: float
        +category: str
        +popularity_rating: float
    }

    class Products {
        +items: list~Item~
        +add_item(item: Item) None
        +filter_by_category(category: str) list~Item~
        +sort_by_price() list~Item~
        +sort_by_popularity() list~Item~
    }

    class Cart {
        +customer: Customer
        +items: list~Item~
        +add_item(item: Item) None
        +compute_total() float
    }

    Customer "1" -- "0..*" Cart : places
    Products "1" o-- "0..*" Item : holds
    Cart "0..*" o-- "0..*" Item : selected items

    note for Item "category e.g. Entrees, Sides, Drinks, Desserts\n0 <= popularity_rating <= 5"
    note for Products "sort_by_price(): lowest price first\nsort_by_popularity(): highest rating first\nboth return a new list; items is unchanged"
    note for Customer "is_verified() is true when purchase_history\nhas at least one Cart"
    note for Cart "compute_total() = sum of item prices"
```

## Class summaries

- **Customer**: a user of the app, identified by name. Their past Carts show they are a real user, and one past purchase is enough to count as verified.
- **Item**: one food or drink for sale, with a name, price, category (a plain string such as "Drinks" or "Desserts"), and a popularity rating from 0 to 5 stars.
- **Products**: the full menu of Items, which can be filtered by category and sorted by price or popularity.
- **Cart**: one transaction that belongs to one Customer. It holds the Items they picked and computes the total as the sum of their prices.
