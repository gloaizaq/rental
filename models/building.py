# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Building(models.Model):
    _name = 'rental.building'

    name = fields.Char(string="Nombre")
    address = fields.Text(string="Direccion")
    total_area = fields.Float(string="Area de terreno")
    built_area = fields.Float(string="Area construida")
    floors = fields.One2many('rental.floor', 'building_id', string="Pisos")
    real_value = fields.Float(string="Valor Real")
    fiscal_value = fields.Float(string="Valor Fiscal")

    _sql_constraints = [
        ('mane_unique',
         'UNIQUE(name)',
         "Ya existe un edificio con ese nombre")
    ]
