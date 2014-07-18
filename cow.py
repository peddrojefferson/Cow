#encoding:utf-8
import sys
c = ''

def moo(*args):
	print len(args)
	limit_top = ' ' + ('_' * (len(args[0])+1))
	limit_bottom = ' ' + ('-' * (len(args[0])+1))
	print args
	if sys.argv[1]:
		print limit_top
		print ("<%s >" %args ) 
		print limit_bottom
		print "        \   ^__^ "
		print "         \  (oo)\_______"
		print "            (__)\       )\/\ "
		print "                ||----w | "
		print "                ||     ||"

try:
	for i in sys.argv[1:]:
		c = c + ' ' + i
	moo(c)
except IndexError:
	print "input something!"
