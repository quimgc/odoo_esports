# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Persona(models.Model):
    _name = "persona"
    name = fields.Char('Nom', required=True)