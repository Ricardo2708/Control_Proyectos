#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyecto_Ultimate.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()


# Inicia el servidor con: python manage.py runserver

#? Si no has instalado jupyter : pip install jupyter ipython django-extensions
#? INSTALLED_APPS = [
#?     ...
#?     'django_extensions',
#? ]


# Inicia Jupyter con: python manage.py shell_plus --notebook
# Inicia Jupyter en remoto: jupyter notebook  --no-browser --ip 192.168.1.207 --port 8080 
# jupyter notebook --ip='5.183.11.81' --port=8888 --allow-root 