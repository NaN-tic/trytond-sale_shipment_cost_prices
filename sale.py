#This file is part sale_shipment_cost_prices module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'

    @classmethod
    def get_cost_line_on_change_product(self, product, price, sale=None):
        cost = super(Sale, self).get_cost_line_on_change_product(product, price, sale=None)
        cost['gross_unit_price'] = price
        cost['cost_price'] = price
        return cost
