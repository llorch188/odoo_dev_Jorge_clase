{
    'name': "gestion_restaurante_jorge",

    'summary':  "Modelo de Platos para Gestión de Restaurante",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu_root.xml',
        'views/plato_view.xml',
        'views/menu_view.xml',
        'views/ingrendiente_view.xml',
    ],
    # only loaded in demonstration mode
    'installable' : True,
    'application' : True,
    
}

