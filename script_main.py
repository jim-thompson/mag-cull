'''
Created on Apr 17, 2021

@author: jct
'''

from mag_cull import magcull_main
from script_log import setup_nslog, nslog

def script_main(nslog_, argv):
    setup_nslog(nslog_)
    nslog('In script_main: "Hello, world!"')
    magcull_main(argv)

    nslog("%d arguments" % len(argv))
    for f in argv:
        nslog("  <%s>" % f)

if __name__ == "__main__":
    mag_arg = '/Users/jct/Dropbox (Personal)/Development/python-workspace/magcull/test-data/20 CookBooks Collection PDF Pack 1'
    argv = [ "magcull", mag_arg]
    script_main(None, argv)
