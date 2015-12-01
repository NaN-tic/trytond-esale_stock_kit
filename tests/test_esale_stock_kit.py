# This file is part of the esale_stock_kit module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class EsaleStockKitTestCase(ModuleTestCase):
    'Test Esale Stock Kit module'
    module = 'esale_stock_kit'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        EsaleStockKitTestCase))
    return suite