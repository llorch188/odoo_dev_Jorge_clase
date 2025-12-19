from odoo import models, fields

class Ingrediente(models.Model):
    _name = 'gestion_restaurante_jorge.ingrediente'
    _description = 'Ingrediente'

    name = fields.Char(
        string="Nombre",
        required=True,
        help="Nombre del ingrediente"
    )

    es_alergeno = fields.Boolean(
        string="Es alérgeno",
        help="Indica si el ingrediente es un alérgeno"
    )

    descripcion = fields.Text(
        string="Descripción",
        help="Descripción del ingrediente"
    )

    plato_ids = fields.Many2many(
        'gestion_restaurante_jorge.plato',
        'plato_ingrediente_rel',
        'ingrediente_id',
        'plato_id',
        string="Platos",
        help="Platos que usan este ingrediente"
    )
