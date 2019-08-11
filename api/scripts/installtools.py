import sys
from subprocess import call

script_path = "api/scripts"


def install_packages(requirements_file):
    return_code = call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
    if return_code is not 0:
        raise Exception("unable to install one or more packages")


def call_scripts(scripts, script_path):
    for script in scripts:
        return_code = call([sys.executable, script_path + "/" + script])
        if return_code is not 0:
             raise Exception("script: " + script + " failed to execute")


def setup(name, requirements_file, scripts):
    try:
        print(" ==============" + name + "============== ", end="\n\n\n")
        print("Installing packages", end="\n")    
        install_packages(requirements_file)
    
        print("\n")    
        print("========= Calling scripts ============== ", end="\n\n\n")        
        call_scripts(scripts, script_path)
   
    except Exception as inst:
        print("The following error ocurred: " + str(inst))