# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TableManager
                                 A QGIS plugin
 An Implementation of Borys Jurgiel's Table Manager for QGIS 3.0
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-06-05
        copyright            : (C) 2019 by Princy R.
        email                : princy.raza@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TableManager class from file TableManager.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .table_manager import TableManager
    return TableManager(iface)
