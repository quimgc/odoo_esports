# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import Esports

# class esports(models.Model):
#     _name = 'esports.esports'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100