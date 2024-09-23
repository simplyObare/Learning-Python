from shopping_cart import ShoppingCart


def test_can_add_item_to_cart():
   cart = ShoppingCart()
   cart.add_item("apple")
   assert cart.size == 1