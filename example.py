"""
Example notification using prowl.
"""
import prowlpy

p = prowlpy.Prowl('dummy-username','dummy-password')
try:
    p.post('TestApp','Server Down',"The Web Box isn't responding to a ping")
    print 'Success'
except Exception,msg:
    print msg