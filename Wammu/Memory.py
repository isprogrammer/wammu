# -*- coding: UTF-8 -*-
# Wammu - Phone manager
# Copyright (c) 2003 - 2004 Michal Čihař 
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA 02111-1307 USA
'''
Memory reader
'''

import Wammu.Reader
import Wammu.Utils
import gammu

class GetMemory(Wammu.Reader.Reader):
    def __init__(self, win, sm, datatype, type):
        Wammu.Reader.Reader.__init__(self, win, sm)
        self.datatype = datatype
        self.type = type

    def GetStatus(self):
        status = self.sm.GetMemoryStatus(Type = self.type)
        return status['Used'] 
        
    def GetNextStart(self):
        return self.sm.GetNextMemory(Start = True, Type = self.type)

    def GetNext(self, location):
        return self.sm.GetNextMemory(Location = location, Type = self.type)
                        
    def Get(self, location):
        return self.sm.GetMemory(Location = location, Type = self.type)

    def Parse(self, value):
        Wammu.Utils.ParseMemoryEntry(value)

    def Send(self, data):
        self.SendData([self.datatype, self.type], data)
