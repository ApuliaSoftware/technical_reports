# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ProjectProject (models.Model):

    _inherit = 'project.project'

    technical_reports_count = fields.Integer(
        compute='_compute_technical_reports_count', string="Technical reports")
    technical_reports_ids = fields.One2many('technical.report',
                                            'project_id',
                                            string='Technical reports')

    def _compute_technical_reports_count(self):
        for t in self:
            t.technical_reports_count = len(t.technical_reports_ids)
