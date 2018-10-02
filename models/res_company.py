# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResCompany(models.Model):

    _inherit = 'res.company'

    labor_service_id = fields.Many2one('product.product',
                                 string="Labor service report")
    travel_costs_ids = fields.One2many(
        "technical.report.travel.costs", "company_id", string="Travel costs")
    travel_product = fields.Many2one('product.product')

    @api.multi
    def update_partner_distance(self):
        partners = self.env['res.partner'].search([
            ("id", "!=", self.partner_id.id),
            ("customer", "=", True),
            ("partner_latitude", "!=", 0.0),
            ("partner_longitude", "!=", 0.0)])
        print(partners)
        for p in partners:
            distance = p.get_distance_from_partner(
                self.partner_id)
            if distance:
                p.distance = distance

