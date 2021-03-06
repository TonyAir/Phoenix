import unittest
import wx
from unittests import wtc


#---------------------------------------------------------------------------

class IdManagerTest(wtc.WidgetTestCase):

    def test_idManager(self):
        id = wx.IdManager.ReserveId(5)
        self.assertTrue(id != wx.ID_NONE)
        wx.IdManager.UnreserveId(id, 5)


    def test_newIdRef01(self):
        id = wx.NewIdRef()
        assert isinstance(id, wx.WindowIDRef)
        id.GetValue()
        id.GetId()
        id.__int__()


    def test_newIdRef02(self):
        refs = wx.NewIdRef(5)
        assert len(refs) == 5
        for ref in refs:
            assert isinstance(ref, wx.WindowIDRef)


    def test_newIdRef03(self):
        """Check that Auto ID Management is enabled (--enable-autoidman)"""
        # This test is expected to fail if autoID mangagement is turned on
        # because a reference to the ID is not being saved, so it will be 
        # unreserved when the first widget is destroyed.
        
        id = wx.Window.NewControlId()
        b = wx.Button(self.frame, id, 'button')
        b.Destroy()

        self.myYield()

        with self.assertRaises(wx.wxAssertionError):
            b = wx.Button(self.frame, id, 'button')
            b.Destroy()


    def test_newIdRef04(self):
        """Ensure that an ID can be used more than once"""
        id = wx.NewIdRef() # but using this one should succeed

        b = wx.Button(self.frame, id, 'button')
        b.Destroy()

        self.myYield()

        b = wx.Button(self.frame, id, 'button')
        b.Destroy()


    def test_WindowIDRef01(self):
        ref1 = wx.WindowIDRef(wx.IdManager.ReserveId())
        ref2 = wx.WindowIDRef(wx.IdManager.ReserveId())

        val = ref1 == ref2
        assert type(val) == bool
        val = ref1 != ref2
        assert type(val) == bool
        val = ref1 > ref2
        assert type(val) == bool
        val = ref1 < ref2
        assert type(val) == bool
        val = ref1 >= ref2
        assert type(val) == bool
        val = ref1 <= ref2
        assert type(val) == bool

    def test_WindowIDRef02(self):
        d = {wx.NewIdRef(): 'one',
             wx.NewIdRef(): 'two'}
        keys = sorted(d.keys())
        for k in keys:
            val = d[k]

#---------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
