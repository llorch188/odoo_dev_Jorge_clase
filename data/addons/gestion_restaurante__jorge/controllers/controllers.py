# from odoo import http


# class GestionRestauranteJorge(http.Controller):
#     @http.route('/gestion_restaurante__jorge/gestion_restaurante__jorge', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_restaurante__jorge/gestion_restaurante__jorge/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_restaurante__jorge.listing', {
#             'root': '/gestion_restaurante__jorge/gestion_restaurante__jorge',
#             'objects': http.request.env['gestion_restaurante__jorge.gestion_restaurante__jorge'].search([]),
#         })

#     @http.route('/gestion_restaurante__jorge/gestion_restaurante__jorge/objects/<model("gestion_restaurante__jorge.gestion_restaurante__jorge"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_restaurante__jorge.object', {
#             'object': obj
#         })

