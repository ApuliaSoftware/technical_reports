# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class TravelCosts(models.TransientModel):

    _name = 'technical.report.travel.costs'

    from_km = fields.Float()
    to_km =fields.Float()
    fixed_cost =fields.Float()
    variable_cost=fields.Float()
    travel_cost_id = fields.Many2one("res.company", string="Technical report")