# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2015 TrustCode - www.trustcode.com.br                         #
#              Danimar Ribeiro <danimaribeiro@gmail.com>                      #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#                                                                             #
###############################################################################


from openerp import models, api, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    rota = fields.Char(u'Url antiga', size=200)
    
class ProductCategory(models.Model):
    _inherit = 'product.category'
    
    rota = fields.Char(u'Url antiga', size=200)
    
class ProductPublicCategory(models.Model):
    _inherit = 'product.public.category'
    
    rota = fields.Char(u'Url antiga', size=200)

    

    
