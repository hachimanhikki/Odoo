# -*- coding: utf-8 -*-
# from odoo import http


# class HrApplicant(http.Controller):
#     @http.route('/hr_applicant/hr_applicant/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_applicant/hr_applicant/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_applicant.listing', {
#             'root': '/hr_applicant/hr_applicant',
#             'objects': http.request.env['hr_applicant.hr_applicant'].search([]),
#         })

#     @http.route('/hr_applicant/hr_applicant/objects/<model("hr_applicant.hr_applicant"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_applicant.object', {
#             'object': obj
#         })
