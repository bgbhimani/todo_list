"""
WSGI config for todo_list project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_list.settings')

application = get_wsgi_application()
app = application

# Traceback (most recent call last):
# File "/var/task/vc__handler__python.py", line 14, in <module>
# __vc_spec.loader.exec_module(__vc_module)
# File "<frozen importlib._bootstrap_external>", line 999, in exec_module
# File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
# File "/var/task/todo_list/wsgi.py", line 12, in <module>
# from django.core.wsgi import get_wsgi_application
# ModuleNotFoundError: No module named 'django'
# Python process exited with exit status: 1. The logs above can help with debugging the issue.
# Traceback (most recent call last):
# File "/var/task/vc__handler__python.py", line 14, in <module>
# __vc_spec.loader.exec_module(__vc_module)
# File "<frozen importlib._bootstrap_external>", line 999, in exec_module
# File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
# File "/var/task/todo_list/wsgi.py", line 12, in <module>
# from django.core.wsgi import get_wsgi_application
# ModuleNotFoundError: No module named 'django'
# Python process exited with exit status: 1. The logs above can help with debugging the issue.