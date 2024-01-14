Formatters for continuously formatting the contents of GUI elements, emphasising speed so they can be called on each text event.

# Examples
## `wx.richtext`
```python
import wx.richtext
import pygments.formatters

# super duper minimal wx app setup
app = wx.App(False)
frame = wx.Frame(
    parent=None, 
    size=(720, 720)
)
frame.SetSizer(wx.BoxSizer(wx.VERTICAL))
frame.Show()
# make a rich text ctrl
ctrl = wx.richtext.RichTextCtrl(
    frame, 
    size=(720, 720)
)
frame.GetSizer().Add(ctrl, flag=wx.EXPAND)
# make a formatter
formatter = pygments.formatters.get_formatter_by_name("wx.richtext")
# bind the formatter to the rich text ctrl
formatter.bind(ctrl, lexer="python")
# start the app
app.MainLoop()

# any text you type into the rich text ctrl should now be formatted as you type!
```