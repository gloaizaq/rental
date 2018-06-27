# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Floor(models.Model):
    _name = 'rental.floor'

    number = fields.Integer(string="Numero")
    shop = fields.One2many('rental.shop', 'floor_id', string="Locales")
    building_id = fields.Many2one('rental.building', string="Edificio")

    _sql_constraints = [
        ('number_unique',
         'UNIQUE(number)',
         "Ya existe un piso con ese numero")
    ]
