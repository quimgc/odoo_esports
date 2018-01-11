# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Persona(models.Model):
    _name = 'esports.persona'
    dni = fields.Text('DNI',required = True)
    nom = fields.Char('Nom',size=40,required = True)
    cognom1 = fields.Char('1er Cognom',size=40,required = True)
    cognom2 = fields.Char('2on Cognom',size=40,required = True)
    tlf1 = fields.Integer('1er Teléfon',required = True)
    tlf2 = fields.Integer('2on Teléfon')
    email = fields.Text('Correu electrònic')
    adreca = fields.Text('Adreça',required = True)
    poblacio = fields.Text('Població',required = True)
    codiPostal = fields.Integer('Codi postal',required = True)

#     entrena = fields.One2many('esports.jugador', 'dni', 'Entrenador')
#     tutor = fields.One2many('esports.jugador', 'dni' ,'Tutor')
#
# class Jugador(models.Model):
#     _name = 'esports.jugador'
#     _inherit = 'esports.persona'
#     sexe = fields.Selection('Home','Dona',required = True)
#     dataNaix = fields.Date('Data naixement',required = True)
#
#     pertany = fields.Many2one('esports.categoria', 'descripcio', String='te categoria')
#     juga = fields.One2many('esports.posicio', 'posicio', String='te posicio')
#     entrena = fields.Many2one('esports.persona', 'dni' ,String='Es entrenat')
#     tutor = fields.Many2one('esports.persona', 'dni', String='El seu tutor')
#
# class Posicio(models.Model):
#     _name = 'esports.posicio'
#     posicio = fields.Selection([('Porter'),('Extrem'),('Lateral'),('Central'),('Pivot')],'Posicio')
#
#     juga = fields.One2many('esports.jugador', 'dni', 'Jugadors')
#
# class Categoria(models.Model):
#     _name = 'esports.categoria'
#     descripcio = fields.Selection([('Menor M F'),('Cadet M'),('Cadet F'),('Juvenil M'),('Juvenil F'),('Junior M'),('Junior F'),
#                                   ('Adult M'),('Adult F')], 'Descripcio')
#
#     pertany = fields.One2many('esports.jugador', 'dni', 'Jugadors')
