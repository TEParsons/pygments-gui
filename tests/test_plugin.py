
def test_plugin_loaded():
    import pygments.formatters
    # define some names and the formatters they should return
    cases = {
        'wx.rtc': "WxRichTextCtrlFormatter",
        'wx.richtext': "WxRichTextCtrlFormatter",
    }
    # iterate through cases
    for name, cls in cases.items():
        # get formatter by name
        fmtr = pygments.formatters.get_formatter_by_name(name)
        # is it the correct class
        assert type(fmtr).__name__ == cls