import os
import importlib.util


spec = importlib.util.spec_from_file_location(name='import_module', location=os.path.join(os.getcwd(), 'import_module.py'))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

print('end')

