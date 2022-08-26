
import sys
def xprint(msg=""):
    try:
        print("do try")
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back

    print('%s[%s]: %s' % (f.f_code.co_filename, str(f.f_lineno), msg))

def test_xprint():
    xprint()
    xprint("%d %s" %(10, "hello"))

test_xprint()