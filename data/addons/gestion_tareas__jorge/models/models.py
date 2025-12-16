from odoo import models, fields, api

class gestion_tareas__jorge(models.Model):
    _name = 'gestion_tareas__jorge.gestion_tareas__jorge'
    _description = 'gestion_tareas__jorge.gestion_tareas__jorge'

    name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

