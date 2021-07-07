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
	#personal
	applicant_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
	nationality = fields.Char()
	address = fields.Char()
	birth_date = fields.Date()
	citizenship = fields.Char()
	is_single = fields.Boolean()
	#work
	workplace = fields.Char()
	workp_experience = fields.Boolean()
	job_position = fields.Char()
	work_start_date = fields.Date()
	work_desc = fields.Text()
	#education
	study_place = fields.Char()
	specialty = fields.Char()
	admission_date = fields.Date()
	graduation_date = fields.Date()

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
