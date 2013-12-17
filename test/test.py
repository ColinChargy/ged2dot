#!/usr/bin/env python3
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

import os
import sys
import unittest
sys.path.append(os.path.join(sys.path[0], ".."))
import ged2dot


class Test(unittest.TestCase):
    def convert(self, name, configDict={}):
        if len(configDict):
            config = ged2dot.Config(configDict)
        else:
            config = ged2dot.Config(["%src" % name])
        model = ged2dot.Model(config)
        model.load(config.input)
        try:
            os.unlink("%s.dot" % name)
        except OSError:
            pass
        sock = open("%s.dot" % name, "w")
        model.save(sock)
        sock.close()

    def test_hello(self):
        configDict = {
            'ged2dot': {
                'input': 'hello.ged',
                'rootFamily': 'F1'
            }
        }
        self.convert('hello', configDict)

    def test_noyeardate(self):
        configDict = {
            'ged2dot': {
                'input': 'noyeardate.ged',
                'rootFamily': 'F1'
            }
        }
        self.convert('noyeardate', configDict)

    def test_nohusb(self):
        # This tests if placeholder nodes are created for missing husbands.
        configDict = {
            'ged2dot': {
                'input': 'nohusb.ged',
                'rootFamily': 'F3'
            }
        }
        self.convert('nohusb', configDict)

    def test_nowife(self):
        # This tests if placeholder nodes are created for missing wifes.
        configDict = {
            'ged2dot': {
                'input': 'nowife.ged',
                'rootFamily': 'F3'
            }
        }
        self.convert('nowife', configDict)

    def test_screenshot(self):
        # This is the demo input from the README, make sure it works.
        # Also, this time use a config file path, to test that as well.
        self.convert('screenshot')

if __name__ == '__main__':
    unittest.main()

# vim:set shiftwidth=4 softtabstop=4 expandtab:
