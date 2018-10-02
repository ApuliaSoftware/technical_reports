# -*- coding: utf-8 -*-
# © 2018 Andrea Cometa (<http://www.andreacometa.it>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api
import requests
import json, ast


class ResPartner (models.Model):

    _inherit = 'res.partner'

    technical_reports_count = fields.Integer(
        compute='_compute_technical_reports_count', string="Technical reports")
    technical_reports_ids = fields.One2many('technical.report',
                                            'partner_id',
                                            string='Technical reports')
    distance = fields.Float(string="Distance (km)")

    def _compute_technical_reports_count(self):
        for t in self:
            t.technical_reports_count = len(t.technical_reports_ids)

    def get_distance_from_partner(self, from_partner):
        partner_link = 'http://router.project-osrm.org/route/v1/driving/' \
                       '{part_long},{part_lat};{comp_long},{comp_lat}' \
                       '?overview=false'\
            .format(part_long=str(self.partner_longitude),
                   part_lat=str(self.partner_latitude),
                   comp_long=str(from_partner.partner_longitude),
                   comp_lat=str(from_partner.partner_latitude)
                   )
        r = requests.get(partner_link)
        dict = r.json()
        data = ast.literal_eval(json.dumps(dict))
        print('---------------------------------------------------------------')
        print(dict)
        if "routes" in data:
            return data["routes"][0]['distance']
        return False

    @api.multi
    @api.onchange('partner_longitude', 'partner_latitude')
    def distance_calc(self):
        for partner in self:
            distance = self.get_distance_from_partner(
                self.env.user.company_id.partner_id)
            if distance:
                partner.distance = distance
