"""电商价格计算模块."""

import logging

logger = logging.getLogger(__name__)


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

        Raises:
            ValueError: 当参数为负数时抛出
        """
        for name, val in [
            ("original_price", original_price),
            ("discount_coupon", discount_coupon),
            ("points_value", points_value),
        ]:
            if not isinstance(val, (int, float)):
                raise TypeError(f"{name} must be a number")
            if val < 0:
                raise ValueError(f"{name} must be non-negative")

        total_discount = discount_coupon + points_value
        if total_discount > original_price:
            logger.warning(
                "折扣超价: original_price=%s, discount_coupon=%s, points_value=%s",
                original_price,
                discount_coupon,
                points_value,
            )
            return 0

        return original_price - total_discount

    def calculate_points_needed(self, price):
        """根据价格计算所需积分（1积分=0.01元）。

        Args:
            price: 需要抵扣的金额

        Returns:
            所需积分数量

        Raises:
            ValueError: 当参数为负数时抛出
        """
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        if price < 0:
            raise ValueError("price must be non-negative")
        return int(round(price * 100))
