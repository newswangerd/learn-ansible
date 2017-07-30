from importlib import import_module

def validate_task(name, args):
    validator = import_validator(name)
    val = validator(args)
    did_pass = val.validate()
    print(val.get_message())
    return did_pass

def import_validator(name):
    name = name.split(".")
    mod = import_module("lib.validators." + name[0])
    mod = getattr(mod, name[1])
    return mod

# validate_task("playbook.PlaybookValidator", {})
