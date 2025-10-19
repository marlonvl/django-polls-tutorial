import os
import sys
import django
from pathlib import Path

# Make project package importable for autodoc:
# añade la carpeta raíz del paquete (django-polls) al sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # ../../..
PROJECT_PARENT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_PARENT))
sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

# -- Project information -----------------------------------------------------
project = "django-polls"
author = "Marlon Ariel Vera Loor"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Intersphinx: enlazar a la docs de Django (stable)
intersphinx_mapping = {
    "django": ("https://docs.djangoproject.com/en/stable/", None),
}