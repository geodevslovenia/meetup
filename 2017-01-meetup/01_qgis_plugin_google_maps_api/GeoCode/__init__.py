# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoCode
                                 A QGIS plugin
 Geocoding using Google maps API
                             -------------------
        begin                : 2017-09-17
        copyright            : (C) 2017 by Nejc Dougan
        email                : nejc.dougan@gmail.com
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
    """Load GeoCode class from file GeoCode.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .geocode import GeoCode
    return GeoCode(iface)
