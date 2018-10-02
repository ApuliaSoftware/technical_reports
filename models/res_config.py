# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ProjectConfiguration(models.TransientModel):

    _inherit = 'project.config.settings'

    labor_service_id = fields.Many2one(
        related='company_id.labor_service_id', string="Labor service report")
    travel_costs_ids = fields.One2many(
        related="company_id.travel_costs_ids", string="Travel costs")
    travel_product = fields.Many2one(related='company_id.travel_product')
