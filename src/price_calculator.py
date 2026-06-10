"""电商价格计算模块."""


class PriceCalculator:
    """价格计算器，支持优惠券和积分抵扣."""

    def calculate_final_price(self, original_price, discount_coupon, points_value):
        """计算最终支付价格。

        Args:
            original_price: 商品原价（正数）
            discount_coupon: 优惠券抵扣金额
            points_value: 积分抵扣金额

        Returns:
            最终支付价格
        """
        return original_price - discount_coupon - points_value

    def calculate_points_needed(self, price):
        """根据价格计算所需积分（1积分=0.01元）。

        Args:
            price: 需要抵扣的金额

        Returns:
            所需积分数量
        """
        return int(price / 0.01)
