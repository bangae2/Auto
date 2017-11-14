import os
import time
import pyHook  # http://sourceforge.net/projects/pyhook/
from win32gui import GetWindowRect, GetClassName, GetWindowText

##http://sourceforge.net/projects/pywin32/files/pywin32/Build216/


curTime = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))

if not os.path.exists("Messages"):
    os.mkdir("Messages")
    print
    "Make Message Directory "
f = open("Messages\\messages" + curTime + ".txt", "w")


def Log(logStr):
    print
    "In logging "
    print
    str(logStr)
    f.write(logStr + "\n")


def OnMouseEvent(event):
    print
    "On Mouse Event "
    Log('MessageName:' + str(event.MessageName))
    Log('Message:' + str(event.Message))
    Log('Time:' + str(event.Time))
    Log('Window:' + str(event.Window))
    if event.Window != 0:
        Log('Window Rect:' + str(GetWindowRect(event.Window)))
        Log('Window Class Name:' + str(GetClassName(event.Window)))
        # Log('Window Text:' + str( GetWindowText(event.Window)))
        Log('WindowName:' + str(event.WindowName))
        Log('Position:' + str(event.Position))
        Log('Wheel:' + str(event.Wheel))
        Log('Injected:' + str(event.Injected))
        Log('---')

        # return True to pass the event to other handlers
        # return False to stop the event from propagating
    return True


def OnKeyboardEvent(event):
    print
    "On keyboard Event "
    Log('MessageName:' + str(event.MessageName))
    Log('Message:' + str(event.Message))
    Log('Time:' + str(event.Time))
    Log('Window:' + str(event.Window))
    if event.Window != 0:
        Log('Window Rect:' + str(GetWindowRect(event.Window)))
        Log('Window Class Name:' + str(GetClassName(event.Window)))
        Log('Window Text:' + str(GetWindowText(event.Window)))
        Log('WindowName:' + str(event.WindowName))
        Log('Ascii:' + str(event.Ascii) + str(chr(event.Ascii)))
        Log('Key:' + str(event.Key))
        Log('KeyID:' + str(event.KeyID))
        Log('ScanCode:' + str(event.ScanCode))
        Log('Extended:' + str(event.Extended))
        Log('Injected:' + str(event.Injected))
        Log('Alt' + str(event.Alt))
        Log('Transition' + str(event.Transition))
        Log('---')

    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True

    # create the hook mananger


hm = pyHook.HookManager()
# register two callbacks
hm.MouseAllButtonsDown = OnMouseEvent
hm.KeyDown = OnKeyboardEvent

# hook into the mouse and keyboard events
hm.HookMouse()
hm.HookKeyboard()

if __name__ == '__main__':
    import pythoncom

    pythoncom.PumpMessages()
