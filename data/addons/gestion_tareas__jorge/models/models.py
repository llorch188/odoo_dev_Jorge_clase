from odoo import models, fields, api
from odoo.exceptions import UserError
import logging

# =================================================
# LOGGER
# =================================================
_logger = logging.getLogger(__name__)


# =================================================
# MODELO: TAREA
# =================================================
class GestionTarea(models.Model):
    _name = 'gestion_tareas__jorge.tarea'
    _description = 'Gestión de tareas'

    name = fields.Char(string="Título de la tarea")
    description = fields.Text(
        string="Descripción",
        required=True,
        help="La descripción es obligatoria"
    )

    historia_id = fields.Many2one(
        'gestion_tareas__jorge.historia',
        string='Historia de usuario',
        ondelete='set null'
    )

    tecnologia_ids = fields.Many2many(
        'gestion_tareas__jorge.tecnologia',
        relation='relacion_tarea_tecnologia',
        column1='tarea_id',
        column2='tecnologia_id',
        string="Tecnologías"
    )

    # =================================================
    # EXCEPCIONES + LOGS (CREATE)
    # =================================================
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('description'):
                _logger.error("Intento de crear tarea sin descripción")
                raise UserError("La descripción de la tarea es obligatoria.")

            _logger.info(
                "Creando tarea: %s",
                vals.get('name', 'Sin título')
            )

        return super().create(vals_list)

    # =================================================
    # EXCEPCIONES + LOGS (WRITE)
    # =================================================
    def write(self, vals):
        if 'description' in vals and not vals.get('description'):
            _logger.error("Intento de dejar una tarea sin descripción")
            raise UserError("La descripción no puede quedar vacía.")

        _logger.info(
            "Modificando tarea ID(s) %s con valores %s",
            self.ids,
            vals
        )

        return super().write(vals)


# =================================================
# MODELO: HISTORIA DE USUARIO
# =================================================
class GestionHistoria(models.Model):
    _name = 'gestion_tareas__jorge.historia'
    _description = 'Historia de usuario'

    name = fields.Char(
        string="Nombre de la historia",
        required=True
    )

    description = fields.Text(
        string="Descripción",
        required=True
    )

    proyecto_id = fields.Many2one(
        'gestion_tareas__jorge.proyecto',
        string='Proyecto',
        ondelete='cascade'
    )

    tarea_ids = fields.One2many(
        'gestion_tareas__jorge.tarea',
        'historia_id',
        string='Tareas'
    )


# =================================================
# MODELO: PROYECTO
# =================================================
class GestionProyecto(models.Model):
    _name = 'gestion_tareas__jorge.proyecto'
    _description = 'Proyecto'

    name = fields.Char(
        string="Nombre del proyecto",
        required=True
    )

    description = fields.Text(
        string="Descripción",
        required=True
    )

    historia_ids = fields.One2many(
        'gestion_tareas__jorge.historia',
        'proyecto_id',
        string='Historias del proyecto'
    )


# =================================================
# MODELO: TECNOLOGÍA
# =================================================
class GestionTecnologia(models.Model):
    _name = 'gestion_tareas__jorge.tecnologia'
    _description = 'Tecnología'

    name = fields.Char(
        string="Nombre de la tecnología",
        required=True
    )


# =================================================
# MODELO: SPRINT
# =================================================
class GestionSprint(models.Model):
    _name = 'gestion_tareas__jorge.sprint'
    _description = 'Sprint del proyecto'

    nombre = fields.Char(
        string="Nombre",
        required=True
    )

    fecha_ini = fields.Datetime(
        string="Fecha inicio",
        required=True
    )

    duracion = fields.Integer(
        string="Duración (días)",
        help="Cantidad de días que dura el sprint"
    )

    fecha_fin = fields.Datetime(
        compute='_compute_fecha_fin',
        store=True,
        string="Fecha fin"
    )

    proyecto_id = fields.Many2one(
        'gestion_tareas__jorge.proyecto',
        string='Proyecto',
        ondelete='set null'
    )

    # =================================================
    # COMPUTE
    # =================================================
    @api.depends('fecha_ini', 'duracion')
    def _compute_fecha_fin(self):
        for record in self:
            if record.fecha_ini and record.duracion:
                record.fecha_fin = record.fecha_ini + fields.Date.to_timedelta(record.duracion)
            else:
                record.fecha_fin = False
