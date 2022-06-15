"""
WSGI config for MedicalReportes5 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
import site
from django.core.wsgi import get_wsgi_application
from pathlib import Path



# Add project directory to the sys.path
path_home = str(Path(__file__).parents[1])
if path_home not in sys.path:
    sys.path.append(path_home)



# Add the app's directory to the PYTHONPATH
sys.path.append('C:\EntornosPython\MedicalReportes5')
sys.path.append('C:\EntornosPython\MedicalReportes5\MedicalReportes5')



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MedicalReportes5.settings')

application = get_wsgi_application()
