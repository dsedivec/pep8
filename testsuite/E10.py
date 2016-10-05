#: E101 W191
for a in 'abc':
    for b in 'xyz':
        print a  # indented with 8 spaces
	print b  # indented with 1 tab
#: E101:4:2 W191 W191 W191
if True:
	foo(
		bar(baz),
	        eek)
#: E101 E122 W191 W191
if True:
	pass

change_2_log = \
"""Change 2 by slamb@testclient on 2006/04/13 21:46:23

	creation
"""

p4change = {
    2: change_2_log,
}


class TestP4Poller(unittest.TestCase):
    def setUp(self):
        self.setUpGetProcessOutput()
        return self.setUpChangeSource()

    def tearDown(self):
        pass
#
#: E101 E101 W191 W191
def test_keys(self):
    """areas.json - All regions are accounted for."""
    expected = set([
	u'Norrbotten',
	u'V\xe4sterbotten',
    ])
#: W191:3:1 W191:4:1 W191:5:1
# This should not yield E101.
if True:
	if True \
	   or False:
		pass
#: W191:3:1 W191:4:1
# This should not yield E101.
if True:
	foo((x,)
	    for x in range(10))
#: E101:3:2 W191:2:1 W191:3:1 W191:4:1
if True:
	foo((
	    "this doesn't call for spaces for alignment, should get E101 here"
	))
#: W191:3:1 W191:4:1 W191:5:1
# This should not yield E101.
if True:
	floof(bar,
	      eekerson(
	          blah blah blah))
