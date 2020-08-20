# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    labor_service_id = fields.Many2one(
        related='company_id.labor_service_id', readonly=False)
    # travel_costs_ids = fields.Many2many(
    #     related="company_id.travel_costs_ids", readonly=False)
    travel_product = fields.Many2one(related='company_id.travel_product',
                                     readonly=False)
