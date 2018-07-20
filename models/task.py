# -*- coding: utf-8 -*-
# © 2018 Andrea Cometa (<http://www.andreacometa.it>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api

class Task (models.Model):

    _inherit = 'project.task'

    technical_reports_count = fields.Integer(compute='_compute_technical_reports_count', string="Technical reports")
    technical_reports_ids = fields.One2many('report.reports', 'report_id', string='Technical reports')
    #,domain=['|', ('stage_id.fold', '=', False), ('stage_id', '=', False)])


    def _compute_technical_reports_count(self):

        for t in self:
            t.technical_reports_count = len(r.id for r in t.technical_reports_ids)
