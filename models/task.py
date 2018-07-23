# -*- coding: utf-8 -*-
# © 2018 Andrea Cometa (<http://www.andreacometa.it>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Task (models.Model):

    _inherit = 'project.task'

    technical_reports_count = fields.Integer(
        compute='_compute_technical_reports_count', string="Technical reports")
    technical_reports_ids = fields.One2many('report.reports',
                                            'project_activity_id',
                                            string='Technical reports')

    def _compute_technical_reports_count(self):
        for t in self:
            t.technical_reports_count = len(t.technical_reports_ids)
