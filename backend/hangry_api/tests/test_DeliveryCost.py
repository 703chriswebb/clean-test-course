from api.controllers import Delivery
from django_mock_queries.query import MockModel, MockSet


def order_with_quantities(*quantities):
  order = MockSet()
  for quantity in quantities:
    order.add(MockModel(quantity=quantity))
  return order


def test_returns_highest_delivery_fee_for_more_than_10_items_over_5_miles():
  order = order_with_quantities(5, 5, 5)

  assert Delivery.calculate(order, 6) == 7.50


def test_returns_middle_delivery_fee_for_more_than_5_items_over_3_miles():
  order = order_with_quantities(2, 2, 2)

  assert Delivery.calculate(order, 4) == 5


def test_returns_base_delivery_fee_for_5_or_fewer_items():
  order = order_with_quantities(3, 1, 1)

  assert Delivery.calculate(order, 10) == 3.50


def test_returns_middle_fee_when_item_count_is_at_high_fee_boundary():
  order = order_with_quantities(10)

  assert Delivery.calculate(order, 6) == 5


def test_returns_middle_fee_when_distance_is_at_high_fee_boundary():
  order = order_with_quantities(11)

  assert Delivery.calculate(order, 5) == 5


def test_returns_base_fee_at_the_middle_fee_boundaries():
  order = order_with_quantities(5)

  assert Delivery.calculate(order, 3) == 3.50


def test_returns_base_fee_for_an_empty_order():
  assert Delivery.calculate(MockSet(), 10) == 3.50
