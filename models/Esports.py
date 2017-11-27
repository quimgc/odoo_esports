# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Esports(models.Model):
    _name = "esports"
    name = fields.Char('Nom')