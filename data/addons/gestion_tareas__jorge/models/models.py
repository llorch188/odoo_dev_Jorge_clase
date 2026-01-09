from odoo import models, fields, api
from odoo.exceptions import UserError
import logging

# =================================================
# LOGGER
# =================================================
_logger = logging.getLogger(__name__)


# =================================================
# MODELO: Gestión de Tareas
# =================================================
class gestion_tareas__jorge(models.Model):
    _name = 'gestion_tareas__jorge.gestion_tareas__jorge'
    _description = 'Gestión de tareas'

    name = fields.Char(
        string="Título de la tarea"
    )

    description = fields.Text(
        string="Descripción",
        help="La descripción es obligatoria"
    )

    # =================================================
    # EXCEPCIONES + LOGS (CREATE)
    # =================================================
    @api.model_create_multi
    def create(self, vals_list):
        try:
            for vals in vals_list:
                if not vals.get('description'):
                    raise UserError("La descripción de la tarea es obligatoria.")

                _logger.info(
                    "Creando tarea: %s",
                    vals.get('name', 'Sin título')
                )

            return super().create(vals_list)

        except Exception as e:
            _logger.error("Error al crear tarea: %s", e)
            raise

    # =================================================
    # EXCEPCIONES + LOGS (WRITE)
    # =================================================
    def write(self, vals):
        try:
            if 'description' in vals and not vals.get('description'):
                raise UserError("La descripción no puede quedar vacía.")

            _logger.info(
                "Modificando tarea ID(s) %s con valores %s",
                self.ids,
                vals
            )

            return super().write(vals)

        except Exception as e:
            _logger.error("Error al modificar tarea: %s", e)
            raise
