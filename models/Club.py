# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Club(models.Model):
    _name = "esports"
    name = fields.Char('Nom')

class Persona(models.Model):
    _name = "persona"
    name = fields.Char('Nom')
    edat = fields.Integer('Edat')