#!/bin/sh

pyuic5 -o tableManagerUi.py tableManagerUi.ui
pyuic5 -o tableManagerUiClone.py tableManagerUiClone.ui
pyuic5 -o tableManagerUiInsert.py tableManagerUiInsert.ui
pyuic5 -o tableManagerUiRename.py tableManagerUirename.ui
pyrcc5 -o resources_rc.py resources.qrc
