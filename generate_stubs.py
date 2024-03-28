#run in Gaffer Python editor with: exec(open('/media/jakubvondra/Data/dev/gaffer/Gaffer-Python-Stubs/generate_stubs.py').read())

import inspect
import os, sys
import importlib

target = "/media/jakubvondra/Data/dev/gaffer/Gaffer-Python-Stubs/stubs" #where ever the stubs should be put in
source = os.environ['PYTHONPATH'].split(":")[0].split(";")[0] # should be python folder inside gaffer instalation dir 


# getting the argument hints of a Boost method by intentionaly givign it bad arguments and catchign the exception, as inspect fails for these methods 
def get_init_args(f):
	out = []
	try:
		f("a","a","a","a","a","a","a","a")
	except Exception as e:
		e_list = (str(e).splitlines())
		if (e_list[0]=='Python argument types in'):
			for i in e_list:
				if i.strip().startswith("__init__"):
					out.append(i.strip())
	return(out)

def generate_stubs(source_path,target_path):
	print(f'trying to genrate stubs from {source_path}')

	modules = []
	for f in os.listdir(source_path):
		if ( os.path.isdir(os.path.join(source_path,f)) and f != "__pycache__"):
			try:
				importlib.import_module(f)
				modules.append(f)
			except:
				print("could not import module " + f)
		elif f.endswith(".so"):
			try:
				importlib.import_module(f.split(".")[0])
				modules.append(f.split(".")[0])
			except:
				print("could not import module " + f)
				
	for m in modules:
		print(f'generating stubs for {m}')
		out_path = os.path.join(target_path,m+".pyi")
		with open(out_path, 'w') as f:
			f.truncate(0) #erase content
			for name, obj in inspect.getmembers(sys.modules[m]):

				#the construction method for the class
				if inspect.isbuiltin(obj.__new__):
					f.write('\n')
					f.write(f'def {name} (*args):\n')
					arg_options = get_init_args(obj.__init__)
					f.write(f"      '''\n")
					for o in arg_options:
						f.write(f"{o}\n")
					f.write(f"\n'''      ")
					f.write('\n    ...\n')

				# the class methods
				if inspect.isclass(obj):
					f.write('\n')
					f.write(f'class {name}:\n')
					try:
						for func_name, func in inspect.getmembers(obj):
								if not func_name.startswith('__'):
									try:
										f.write(f'    def {func_name} {inspect.signature(func)}:\n')
									except:
										f.write(f'    def {func_name} (self, *args, **kwargs):\n')
									f.write(f"      '''{func.__doc__}'''")
									f.write('\n    ...\n')
					except:
						pass
	print("stub generating finished")

generate_stubs(source,target)