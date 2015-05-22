#!/usr/bin/env python
# This file is part esale_stock_kit module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class eSaleStockKitTestCase(unittest.TestCase):
    'Test eSale Stock Kit module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('esale_stock_kit')

    def test0005views(self):
        'Test views'
        test_view('esale_stock_kit')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        eSaleStockKitTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
