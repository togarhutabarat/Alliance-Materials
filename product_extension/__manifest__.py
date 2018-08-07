# -*- coding: utf-8 -*-
{
    'name': "Product Extension",

    'summary': """
        Product extensions for Alliance Material""",

    'description': """
        This module will add few additional fields in product form
    """,

    'author': "Togar Hutabarat",
    'website': "https://www.upwork.com/fl/togarhutabarat",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_view.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}