# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2015 TrustCode - www.trustcode.com.br                         #
#                                                                             #
#This program is free software: you can redistribute it and/or modify         #
#it under the terms of the GNU Affero General Public License as published by  #
#the Free Software Foundation, either version 3 of the License, or            #
#(at your option) any later version.                                          #
#                                                                             #
#This program is distributed in the hope that it will be useful,              #
#but WITHOUT ANY WARRANTY; without even the implied warranty of               #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
#GNU General Public License for more details.                                 #
#                                                                             #
#You should have received a copy of the GNU General Public License            #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
###############################################################################
{
    'name' : "base_customizacao",
    'version' : "1.0",
    'author' : "TrustCode",
    'description':'Módulo Base HgSoft',
    'website': 'http://www.trustcode.com.br',
    'depends' : ['base', 'crm' , 'l10n_br_base', 'l10n_br_data_base', 'l10n_br_account',
                 'l10n_br_data_account_product','l10n_br_sale'],   
    'data' : [
        'data/base_data.xml',
        'data/res_partner_view.xml',
        'data/sale_order_view.xml',
    ],
    'installable': True,
    'auto_install':False
}
