# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class hr_applicant(models.Model):
#     _name = 'hr_applicant.hr_applicant'
#     _description = 'hr_applicant.hr_applicant'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class hr_applicant(models.Model):
	_inherit = "hr.applicant"

	interviewer = fields.Many2one('hr.employee')
	responsible = fields.Many2one('hr.employee')


	@api.onchange('responsible')
	def _set_interviewer(self):
		for record in self:
			if record.responsible:
				record.interviewer = record.responsible

	# @api.onchange('stage_id')
	# def _set_department_head(self):
	# 	for record in self:
	# 		if record.stage_id = 'stage_job3':


	@api.onchange('stage_id')
	def _set_department_head(self):
		for record in self:
			if record.stage_id.id < 3:
				record.interviewer = record.responsible
			else:
				record.interviewer = record.department_id.manager_id


