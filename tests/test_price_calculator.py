"""价格计算器单元测试."""

import pytest

from src.price_calculator import PriceCalculator


class TestPriceCalculator:
    """PriceCalculator 单元测试."""

    def setup_method(self):
        """每个测试前初始化."""
        self.calc = PriceCalculator()

    def test_normal_calculation(self):
        """正常计算：原价100，优惠券10，积分5 => 85."""
        result = self.calc.calculate_final_price(100, 10, 5)
        assert result == 85

    def test_no_discount(self):
        """无优惠场景：原价100，无优惠券，无积分 => 100."""
        result = self.calc.calculate_final_price(100, 0, 0)
        assert result == 100

    def test_points_calculation(self):
        """积分计算：10元需要1000积分（1积分=0.01元）."""
        points = self.calc.calculate_points_needed(10)
        assert points == 1000
