#!/bin/bash

sudo apt install python-gi python-gi-cairo python3-gi python3-gi-cairo gir1.2-gtk-3.0
sudo cp -r . /opt/errorcalc
sudo cp /opt/errorcalc/.desktop/catron.png /usr/local/etc/
sudo chmod 777 -R /opt/errorcalc 
if [[ ! -e /usr/bin/errorcalc ]]; then
    sudo ln -s /opt/errorcalc/calculator.py /usr/bin/errorcalc
fi
sudo cp /opt/errorcalc/.desktop/error-calc.desktop /usr/share/applications