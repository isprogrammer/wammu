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
Main Wammu application
'''

import wx
import sys
import Wammu.Main
import Wammu.Error
from Wammu.Paths import *
from Wammu.Utils import Str_ as _

class WammuApp(wx.App):

    # wxWindows calls this method to initialize the application
    def OnInit(self):

        self.SetAppName('Wammu')
        self.SetVendorName('Michal Čihař')

        wx.InitAllImageHandlers()
        #spl = wx.SplashScreen(wx.Bitmap(MiscPath('splash')), wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 5000, None, -1)
        frame = Wammu.Main.WammuFrame(None, -1)

        frame.Show(True)
        frame.PostInit()
        self.SetTopWindow(frame)
        #spl.Destroy()


        # Return a success flag
        return True

def Run():
    try:
        sys.excepthook = Wammu.Error.Handler
    except:
        print _('Failed to set exception handler.')
    app = WammuApp()
    app.MainLoop()

