# -*- coding: utf-8 -*-
{
    'name': "cat_breeder",

    'summary': "Cat Breeder Cattery",

    'description': """  """,

    'author': "PhamQChi",
    'website': "https://www.odoo-optimo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Pets',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/breeder_kitten_views.xml',
        'views/breeder_breed_views.xml',
        'views/breeder_kitten_list_template.xml',
        'report/breeder_kitten_report_templates.xml',
        'report/breeder_kitten_report.xml',
        'views/breeder_menus.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}

