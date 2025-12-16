from odoo import models, fields


class Ingrediente(models.Model):
    _name = 'gestion_restaurante_jorge.ingrediente'
    _description = 'Ingrediente del restaurante'

    name = fields.Char(
        string='Nombre del ingrediente',
        required=True,
        help='Nombre del ingrediente'
    )

    es_alergeno = fields.Boolean(
        string='Es alérgeno',
        help='Indica si el ingrediente es un alérgeno'
    )

    descripcion = fields.Text(
        string='Descripción',
        help='Descripción del ingrediente'
    )

plato_ids = fields.Many2many(
    comodel_name='gestion_restaurante_jorge.plato',
    relation='plato_ingrediente_rel',
    column1='ingrediente_id',
    column2='plato_id',
    string='Platos',
    help='Platos que utilizan este ingrediente'
)
