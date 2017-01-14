#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(args[0], args[1])
    except Exception as err:
        sys.stderr.write("Exception: %s\n" % str(err))
        return None
