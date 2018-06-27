# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Shop(models.Model):
    _name = 'rental.shop'

    number = fields.Integer(string="Numero")
    area = fields.Float(string="Area")
    watermeter = fields.Integer(string="Medidor Agua")
    currentmeter = fields.Integer(string="Medidor Electrico")
