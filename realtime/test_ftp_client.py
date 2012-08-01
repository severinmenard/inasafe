"""
InaSAFE Disaster risk assessment tool developed by AusAid and World Bank
- **Ftp Client Test Cases.**

Contact : ole.moller.nielsen@gmail.com

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'tim@linfiniti.com'
__version__ = '0.5.0'
__date__ = '19/07/2012'
__copyright__ = ('Copyright 2012, Australia Indonesia Facility for '
                 'Disaster Reduction')

import unittest
from realtime.ftp_client import FtpClient


class FtpClientTest(unittest.TestCase):
    """Test the ftp client used to fetch shake listings"""
    # TODO update tests so url host is not hard coded
    _expectedUrlLib2Files = ('ftp://118.97.83.243/20110413170148.inp.zip',
                             'ftp://118.97.83.243/20110413170148.out.zip')
    _expectedFtpLibFiles = (
        ('-rw-r--r--    1 1007     100          1379 Aug 25  2011 '
        '20110430030901.inp.zip'),
        ('-rw-r--r--    1 1007     100        268477 Aug 25  2011 '
        '20110430030901.out.zip')
        )
    def test_getDirectoryListingUsingUrlLib2(self):
        """Check if we can get a nice directory listing using urllib2"""
        myClient = FtpClient()
        myListing = myClient.getListing()
        myMessage = ('Expected this list:\n%s\nTo contain these items:\n%s' %
                      (myListing, self._expectedUrlLib2Files))
        for myExpectedFile in self._expectedFtpLibFiles:
            assert myExpectedFile in myListing, myMessage

    def test_getDirectoryListingUsingFtpLib(self):
        """Check if we can get a nice directory listing using ftplib"""
        myClient = FtpClient(theBackend='ftplib')
        myListing = myClient.getListing()
        myMessage = ('Expected this list:\n%s\nTo contain these items:\n%s' %
                      (myListing, self._expectedUrlLib2Files))
        for myExpectedFile in self._expectedUrlLib2Files:
            assert myExpectedFile in myListing, myMessage

    def test_getFile(self):
        """Test that the ftp client can fetch a file ok"""
        myClient = FtpClient()
        myListing = myClient.getListing()
        myMessage = ('Expected outcome:\n%s\nActual outcome:\n%s' %
                      (myListing, self._expectedUrlLib2Files))
        for myExpectedFile in self._expectedUrlLib2Files:
            assert myExpectedFile in myListing, myMessage


if __name__ == '__main__':
    suite = unittest.makeSuite(FtpClientTest, 'test')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
