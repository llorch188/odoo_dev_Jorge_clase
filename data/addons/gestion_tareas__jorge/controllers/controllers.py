# from odoo import http


# class GestionTareasJorge(http.Controller):
#     @http.route('/gestion_tareas__jorge/gestion_tareas__jorge', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_tareas__jorge/gestion_tareas__jorge/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_tareas__jorge.listing', {
#             'root': '/gestion_tareas__jorge/gestion_tareas__jorge',
#             'objects': http.request.env['gestion_tareas__jorge.gestion_tareas__jorge'].search([]),
#         })

#     @http.route('/gestion_tareas__jorge/gestion_tareas__jorge/objects/<model("gestion_tareas__jorge.gestion_tareas__jorge"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_tareas__jorge.object', {
#             'object': obj
#         })

