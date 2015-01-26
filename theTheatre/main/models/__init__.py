import os
import re
import types
import importlib

model_names = []

model_dir = os.path.dirname(__file__)
if model_dir == '':
    model_dir = '.'

for filename in os.listdir(model_dir):
    if not re.match(r"^.*.py$", filename) or filename == "__init__.py":
        continue
    model_module = importlib.import_module(__name__ + "." + filename[:-3])
    for model_name in dir(model_module):
        model_class = getattr(model_module, model_name)
        if not isinstance(model_class, (type, types.ClassType)):
            continue
        globals()[model_name] = model_class
        model_names.append(model_name)

__all__ = model_names
