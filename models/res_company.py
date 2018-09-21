# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResCompany(models.Model):

    _inherit = 'res.company'

    labor_service_id = fields.Many2one('product.product',
                                 string="Labor service report")
    travel_costs_ids = fields.One2many(
        "technical.report.travel.costs", "travel_cost_id", string="Travel costs")
    travel_product = fields.Many2one('product.product')


