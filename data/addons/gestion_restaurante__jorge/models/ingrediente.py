from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

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
        comodel_name='gestion_restaurante_jorge.plato',
        relation='plato_ingrediente_rel',
        column1='ingrediente_id',
        column2='plato_id',
        string="Platos",
        help="Platos que usan este ingrediente"
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            _logger.info("Creando Ingrediente: %s", vals.get('name'))
        return super().create(vals_list)

    def write(self, vals):
        _logger.info("Modificando Ingrediente ID(s) %s con valores %s", self.ids, vals)
        return super().write(vals)
