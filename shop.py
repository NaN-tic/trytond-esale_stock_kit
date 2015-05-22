# This file is part esale_stock_kit module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelView
from trytond.pool import PoolMeta

__all__ = ['SaleShop']
__metaclass__ = PoolMeta


class SaleShop:
    __name__ = 'sale.shop'

    @classmethod
    def __setup__(cls):
        super(SaleShop, cls).__setup__()
        cls._buttons.update({
                'export_stocks_kit': {},
                })

    @classmethod
    @ModelView.button
    def export_stocks_kit(cls, shops):
        """
        Export Product Kits to External APP
        """
        for shop in shops:
            export_products = getattr(shop,
                'export_stocks_kit_%s' % shop.esale_shop_app)
            export_products()
