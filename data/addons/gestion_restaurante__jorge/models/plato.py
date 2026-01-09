from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class Plato(models.Model):
    _name = 'gestion_restaurante_jorge.plato'
    _description = 'Plato del restaurante'

    name = fields.Char(
        string='Nombre del plato',
        required=True,
        help='Nombre del plato que se ofrece en el restaurante'
    )

    precio = fields.Float(
        string='Precio',
        required=True,
        help='Precio del plato'
    )

    tiempo_preparacion = fields.Integer(
        string='Tiempo de preparación (minutos)',
        required=True,
        help='Tiempo estimado de preparación del plato en minutos'
    )

    disponible = fields.Boolean(
        string='Disponible',
        default=True,
        help='Indica si el plato está disponible para su venta'
    )

    categoria = fields.Selection(
        selection=[
            ('entrante', 'Entrante'),
            ('principal', 'Principal'),
            ('postre', 'Postre'),
            ('bebida', 'Bebida'),
        ],
        string='Categoría',
        required=True,
        help='Categoría a la que pertenece el plato'
    )

    description = fields.Text(
        string='Descripción',
        help='Descripción del plato'
    )

    menu_id = fields.Many2one(
        comodel_name='gestion_restaurante_jorge.menu',
        string='Menú',
        ondelete='set null',
        help='Menú al que pertenece este plato'
    )

    ingrediente_ids = fields.Many2many(
        comodel_name='gestion_restaurante_jorge.ingrediente',
        relation='plato_ingrediente_rel',
        column1='plato_id',
        column2='ingrediente_id',
        string='Ingredientes',
        help='Ingredientes que componen el plato'
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            _logger.info("Creando Plato: %s", vals.get('name'))
        return super().create(vals_list)

    def write(self, vals):
        _logger.info("Modificando Plato ID(s) %s con valores %s", self.ids, vals)
        return super().write(vals)
