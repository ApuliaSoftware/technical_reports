# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class TechnicalReportTravelCosts(models.Model):

    _name = 'technical.report.travel.costs'

    from_km = fields.Float()
    to_km = fields.Float()
    fixed_cost = fields.Float()
    variable_cost = fields.Float()
    company_id = fields.Many2one("res.company")
