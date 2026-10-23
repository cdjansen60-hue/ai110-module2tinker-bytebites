# ByteBites UML Draft (no reference file)

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
    }

    class Cart {
        +items: list~Item~
        +add_item(item: Item) None
        +compute_total() float
    }

    Customer "1" o-- "0..*" Cart : purchase history
    Products "1" o-- "0..*" Item : holds
    Cart "1" o-- "0..*" Item : selected items
    Customer ..> Products : browses
```

## Plain-text version

```
+---------------------------+        +---------------------------+
|         Customer          |        |         Products          |
+---------------------------+        +---------------------------+
| name: str                 |browses | items: list[Item]         |
| purchase_history:         |------->+---------------------------+
|     list[Cart]            |        | add_item(item)            |
+---------------------------+        | filter_by_category(cat)   |
| add_purchase(cart)        |        |     -> list[Item]         |
| is_verified() -> bool     |        +-------------+-------------+
+-------------+-------------+                      | 1
              | 1                                  |
              | purchase history                   | holds
              | 0..*                               | 0..*
+-------------+-------------+        +-------------+-------------+
|           Cart            |        |           Item            |
+---------------------------+  0..*  +---------------------------+
| items: list[Item]         |------->| name: str                 |
+---------------------------+        | price: float              |
| add_item(item)            |        | category: str             |
| compute_total() -> float  |        | popularity_rating: float  |
+---------------------------+        +---------------------------+
```

## Class summaries

- **Customer**: a user of the app, identified by name, whose past Carts show they are a real user.
- **Item**: one food or drink for sale, with a name, price, category, and popularity rating.
- **Products**: the full menu of Items, which can be filtered by category.
- **Cart**: one transaction, holding the Items a customer picked and computing their total cost.
