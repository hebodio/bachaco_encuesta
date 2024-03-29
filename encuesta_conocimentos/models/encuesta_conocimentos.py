# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the Odoo plugin for Dia !
from openerp import api, fields, models

class bachaco_encuesta(models.Model):
    _name = 'bachaco.encuesta'
    #_rec_name = ''
    nombres = fields.Char('Nombres', size=50, help= 'Ingrese su primer y segundo nombre')
    apellidos = fields.Char('Apellidos', size=50, help='Ingrese su primer y segundo apellido')
    sexo = fields.Selection([('m', 'Masculino'), ('f', 'Femenino')], 'Sexo')
    estado_id = fields.Many2one('estado', 'Estado', help='Seleccione el estado de su domicilio')
    municipio_id = fields.Many2one('municipio', 'Municipio', help='Seleccione el municipio de su domicilio')
    parroquia_id = fields.Many2one('parroquia', 'Parroquia', help='Seleccione la parroquia de su domicilio')
    domicilio = fields.Text('Domicilio')
    correo = fields.Char('Correo', size=50)
    telefono_personal = fields.Char('Telefono Personal', size=15)
    telefono_otro = fields.Char('Otro Telefono', size=15)
    disposicion_participar = fields.Boolean('Dispuesto a participar', default=True)
    disposicion_desde_cantidad = fields.Integer('En cuanto tiempo')
    disposicion_desde_lapso = fields.Selection([('dias','Dias'), ('meses','Meses'), ('anios', 'Años')], 'Periodo')
    disposicion_hasta_cantidad = fields.Integer('por cuanto tiempo')
    disposicion_hasta_lapso = fields.Selection([('dias','Dias'), ('meses','Meses'), ('anios', 'Años')], 'Periodo')
    dispocicion_figura_productiva = fields.Many2many('bachaco.figuras_productivas', 'figuras_productivas_encuesta_rel', 'encuesta_id', 'figuras_productivas_id', 'Figura productiva')
    disposicion_sumarse_unidades = fields.Boolean('dispuesto a sumarse a otras UP')
    disposicion_sumarse_nomina = fields.Boolean('dispuesto a sumarse a la nomina institucional')
    caracterizacion_rol_ids = fields.Many2many('bachaco.roles', 'encuesta_roles_rel', 'encuesta_id', 'roles_id', 'Roles')
    caracterizacion_tenologias_base_ids = fields.Many2many('bachaco.elementos_framework', 'encuesta_tecnologias_base_rel', 'encuesta_id', 'elementos_fw_id','Tecnologias base')
    caracterizacion_componentes_fwork_ids = fields.Many2many('bachaco.elementos_framework', 'encuesta_companentes_fw_rel', 'encuesta_id', 'elementos_fw_id', 'Componentes del Framework')
    caracterizacion_modulos_ids = fields.Many2many('bachaco.elementos_framework', 'encuesta_modulos_fw_rel', 'encuesta_id', 'elementos_fw_id', 'Modulos del Framework')
    caracterizacion_conocimento_proc_adm_ids = fields.Many2many('bachaco.procesos_gestion', 'encuesta_procesos_adm_rel', 'encuesta_id', 'procesos_id', 'Procesos de Gestion Publica')


class bachaco_figuras_productivas(models.Model):
    _name = 'bachaco.figuras_productivas'
    _rec_name = 'denominacion'
    denominacion = fields.Char('Denominacion', size=50)
    siglas = fields.Char('siglas', size=20)
    encuesta_ids = fields.Many2many('bachaco.encuesta', 'figuras_productivas_encuesta_rel', 'figuras_productivas_id', 'encuesta_id', 'Figura productiva')


class bachaco_elementos_framework(models.Model):
    _name = 'bachaco.elementos_framework'
    _rec_name = 'denominacion'
    denominacion = fields.Char('denominacion', size=50)
    tipo_elemento_id = fields.Many2one('bachaco.tipos_de_elementos_fw', 'Tipo de Elemento')
    encuestado_tecnologias_base_ids = fields.Many2many('bachaco.elementos_framework', 'encuesta_tecnologias_base_rel', 'elementos_fw_id', 'encuesta_id', 'Conocedores del tema')
    encuestados_componetes_fw_ids = fields.Many2many('bachaco.elementos_framework', 'encuesta_companentes_fw_rel', 'elementos_fw_id','encuesta_id',  'Conocedores del tema')
    escuestado_modulos_ids = fields.Many2many('bachaco.elementos_framework', 'encuesta_modulos_fw_rel', 'elementos_fw_id', 'encuesta_id', 'Conocedores del tema')


class bachaco_roles(models.Model):
    _name = 'bachaco.roles'
    _rec_name = 'denominacion'
    denominacion = fields.Char('Denominacion', size=50)
    labor = fields.Text('Labor que ejecuta')
    encuestado_roles_ids = fields.Many2many('bachaco.roles', 'encuesta_roles_rel', 'roles_id', 'encuesta_id', 'Dispuestos a asumir e rol')


class bachaco_procesos_gestion(models.Model):
    _name = 'bachaco.procesos_gestion'
    _rec_name = 'denominacion'
    denominacion = fields.Char('Denominacion', size=50)
    encuestado_procesos_adm_ids = fields.Many2many('bachaco.procesos_gestion', 'encuesta_procesos_adm_rel', 'procesos_id', 'encuesta_id', 'conocedores del Proceso')


class bachaco_tipos_de_elementos_fw(models.Model):
    _name = 'bachaco.tipos_de_elementos_fw'
    _rec_name = 'denominacion'
    denominacion = fields.Char('Denominacion', size=50)


