# -*- coding: utf-8 -*-
{
    'name': "Alquileres",

    'summary': """
        Modulo de Odoo para prueba practica""",

    'description': """
        Modulo de Odoo para prueba practica
    """,

    'author': "Gustavo Loaiza",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/main_rental_menu.xml',
        'views/shop.xml',
        'views/building.xml',
        'views/floor.xml',
        'views/document.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/shop_demo.xml',
        'demo/floor_demo.xml',
        'demo/building_demo.xml',
        'demo/document_demo.xml',
    ],
}
