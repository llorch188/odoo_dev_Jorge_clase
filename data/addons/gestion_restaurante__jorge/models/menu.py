from odoo import models, fields, api
from odoo.exceptions import UserError
import logging

# =================================================
# LOGGER
# =================================================
_logger = logging.getLogger(__name__)


# =================================================
# MODELO: Menú del Restaurante
# =================================================
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

    # =================================================
    # EXCEPCIÓN + LOGS (CREATE)
    # =================================================
    @api.model_create_multi
    def create(self, vals_list):
        try:
            for vals in vals_list:
                fecha_inicio = vals.get('fecha_inicio')
                fecha_fin = vals.get('fecha_fin')

                if fecha_inicio and fecha_fin and fecha_inicio > fecha_fin:
                    raise UserError(
                        "La fecha de inicio no puede ser posterior a la fecha de fin."
                    )

                _logger.info("Creando Menú: %s", vals.get('name'))

            return super().create(vals_list)

        except Exception as e:
            _logger.error("Error al crear menú: %s", e)
            raise

    # =================================================
    # EXCEPCIÓN + LOGS (WRITE)
    # =================================================
    def write(self, vals):
        try:
            for record in self:
                fecha_inicio = vals.get('fecha_inicio', record.fecha_inicio)
                fecha_fin = vals.get('fecha_fin', record.fecha_fin)

                if fecha_inicio and fecha_fin and fecha_inicio > fecha_fin:
                    raise UserError(
                        "La fecha de inicio no puede ser posterior a la fecha de fin."
                    )

            _logger.info(
                "Modificando Menú ID(s) %s con valores %s",
                self.ids,
                vals
            )

            return super().write(vals)

        except Exception as e:
            _logger.error("Error al modificar menú: %s", e)
            raise
