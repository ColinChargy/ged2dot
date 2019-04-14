#!/usr/bin/env python3
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

import os
import sys
import traceback
from com.sun.star.beans import PropertyValue  # type: ignore
import uno  # type: ignore


class GedcomBase(object):
    def __init__(self, context):  # type: ignore
        self.context = context

    def createUnoService(self, name):  # type: ignore
        return self.context.ServiceManager.createInstanceWithContext("com.sun.star.%s" % name, self.context)

    def toDict(self, args):  # type: ignore
        ret = {}
        for i in args:
            ret[i.Name] = i.Value
        return ret

    def toTuple(self, args):  # type: ignore
        ret = []
        for k, v in args.items():
            value = PropertyValue()
            value.Name = k
            value.Value = v
            ret.append(value)
        return tuple(ret)

    def printTraceback(self):  # type: ignore
        if sys.platform.startswith("win"):
            xPathSubstitution = self.context.ServiceManager.createInstance("com.sun.star.util.PathSubstitution")
            user = xPathSubstitution.getSubstituteVariableValue("user")
            path = uno.fileUrlToSystemPath(user + "/Scripts/python/log.txt")
            dir = os.path.dirname(path)
            if not os.path.exists(dir):
                os.makedirs(dir)
            sock = open(path, "a")
            traceback.print_exc(file=sock)
            sock.close()
        else:
            traceback.print_exc(file=sys.stderr)

# vim:set shiftwidth=4 softtabstop=4 expandtab:
