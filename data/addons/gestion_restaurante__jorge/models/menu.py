from odoo import models, fields


class Menu(models.Model):
    _name = 'gestion_restaurante_jorge.menu'
    _description = 'Menú del restaurante'

    name = fields.Char(
        string='Nombre del menú',
        required=True,
        help='Nombre identificativo del menú'
    )

    descripcion = fields.Text(
        string='Descripción',
        help='Descripción del menú'
    )

    fecha_inicio = fields.Date(
        string='Fecha de inicio',
        required=True,
        help='Fecha en la que el menú empieza a estar disponible'
    )

    fecha_fin = fields.Date(
        string='Fecha de fin',
        help='Fecha en la que el menú deja de estar disponible'
    )

    activo = fields.Boolean(
        string='Activo',
        default=True,
        help='Indica si el menú está activo'
    )

    platos = fields.One2many(
        comodel_name='gestion_restaurante_jorge.plato',
        inverse_name='menu_id',
        string='Platos',
        help='Platos incluidos en este menú'
    )