global gline
global gx
global gy
global gdelay

global active_process
global selectFlag = false
global initFlag = true

global prc =
global prc_old = 
global old_time = 

f3::
param_init()
gui_init()
menu_init()
Gui, Show, x310 y166 h373 w475, Macro

Return

param_init() {
	gline = 
	gx =
	gy =
	gdelay =
	active_process =
	selectFlag = false
	initFlag = true
	prc = 
	prc_old =
}

gui_init() {
	Gui, main: new
	Gui, main: Add, Edit, vgline x12 y10 w270 h350, 
	Gui, main: Add, Text, x292 y10 w30 h20 , X :
	Gui, main: Add, Edit, vgx x332 y10 w40 h20 , 
	Gui, main: Add, Text, x382 y10 w30 h20 , Y :
	Gui, main: Add, Edit, vgy x422 y10 w40 h20 , 
	Gui, main: Add, Text, x292 y50 w80 h20 , Delay Time :
	Gui, main: Add, Edit, vgdelay x382 y50 w80 h20 , 1000
	Gui, main: Add, Text, x292 y80 w80 h20 , Loop Count :
	Gui, main: Add, Text, x292 y120 w170 h20 +Center, Capture ImagePath
	Gui, main: Add, Edit, x292 y150 w170 h20 , img/
	Gui, main: Add, Edit, x382 y80 w80 h20 , 1
	Gui, main: Add, Button, x292 y330 w80 h30 , Start
	Gui, main: Add, Button, x382 y330 w80 h30 , Stop
	; Generated using SmartGUI Creator 4.0
	
	Return
}
	
menu_init() {
	;Menu, FileMenu, Add, &New`tCtrl+N, M_New
	;Menu, FileMenu, Add, &Open`tCtrl+O, M_Open 
	;Menu, FileMenu, Add, &Open`tCtrl+S, M_Save
	
	Menu, fileMenu, Add, &Exit`tCtrl+Q, M_Exit
	Menu, editMenu, Add, Current Position`tAlt+F3, M_Position
	Menu, editMenu, add, &Select Window`tAlt+S, M_Program
	Menu, editMenu, add, &Record`tAlt+F1, M_Record
	Menu, editMenu, add, &RecordStop`tF12, M_RecordStop
	
	Menu, runMenu, add, &Start`tCtrl+F1, M_Start
	Menu, runMenu, add, &Stop`tCtrl+F2, M_Stop
	
	Menu, MyMenuBar, Add, &File, :fileMenu
	Menu, MyMenuBar, Add, &Edit, :editMenu
	Menu, MyMenuBar, Add, &Run, :runMenu
	Gui, Menu, MyMenuBar
}

get_delay() {
	elapsedTime := A_TickCount - old_time
	old_time := A_TickCount
	return elapsedTime
}

M_Start:
WinActivate, % "ahk_exe" active_process
GuiControlGet,lines, , gline
StringSplit, ll ,lines, `n
loop , %ll0%
{
	StringSplit, strs, ll%a_index%, :,
	
	if strs1 = SE
	{
		WinActivate, %strs2%
		winmove,%strs2%,,%strs3%,%strs4%
		winmove,%strs2%,,,,%strs5%,%strs6%	
	}
	if strs1 = ML
	{ 
		MouseClick, left,%strs2%, %strs3%
	}
	if strs1 = DE
	{
		GuiControlGet, t, ,gdelay
		sleep, %t%
	}
	
	if strs1 = DR
	{
		MouseClickDrag, Left, %strs2%, %strs3%, %strs4%, %strs5%, 100
	}
	
}

return

M_Stop:

return

M_Record:
old_time := A_TickCount
Loop
{
    Sleep, 40
	if GetKeyState("LButton") 
	{
		KeyWait, LButton, T0.13
		MouseGetPos, x,y ,win
		Winget, prc_old, processName, ahk_id %win%
		if(prc != prc_old)
		{
			WinGetPos,px,py,w,h, % "ahk_exe" prc_old
			GuiControlGet, line, , gline
			de := get_delay()
			GuiControl, , gline, % line "SE:ahk_exe "prc_old ":"px ":"py ":"w ":"h "`nDE:"de "`n"
		}
		if(ErrorLevel =1) {
			tooltip, drag
			KeyWait, LButton
			GuiControlGet, line, , gline
			MouseGetPos, x1,y1
			de := get_delay()
			GuiControl, , gline, % line "DR:"x ":"y ":"x1 ":"y1 "`nDE:"de "`n"
		} else {
			tooltip, 
			GuiControlGet, line, , gline
			de := get_delay()
			GuiControl, , gline, % line "ML:"x ":"y "`nDE:"de "`n"
		}
	}
	
	if GetKeyState("RButton") 
	{
		MouseGetPos, x,y ,win
		Winget, prc_old, processName, ahk_id %win%
		if(prc != prc_old)
		{
			WinGetPos,x,y,w,h, % "ahk_exe" prc_old
			GuiControlGet, line, , gline
			GuiControl, , gline, % line "SE:ahk_exe "prc_old ":"x ":"y ":"w ":"h "`nDE:2000`n"
		}
		
		GuiControlGet, line, , gline
		de := get_delay()
		GuiControl, , gline, % line "MR:"x ":"y "`nDE:"de "`n"
	}
	prc := prc_old
	GetKeyState, state,F12, P
	if GetKeyState("F12", P) 
	{
		prc_old:=
		prc:=
		break
	}
}
return

M_RecordStop:
	
return

M_Position() {

;WinActivate, Macro

old_time := A_TickCount
loop
{
	Sleep, 40
	if GetKeyState("LButton") 
	{
		MouseGetPos, mx,my, win
		Winget, prc_old, processName, ahk_id %win%
		if(prc != prc_old)
		{
			WinActivate,  % "ahk_exe" active_process
			WinGetPos,x,y,w,h, % "ahk_exe" prc_old
			GuiControlGet, line, , gline
			GuiControl, , gline, % line "SE:ahk_exe "prc_old ":"x ":"y ":"w ":"h "`nDE:2000`n"
		}
		
		GuiControlGet, line, , gline
		de := get_delay()
		MouseGetPos, mx,my
		GuiControl, , gline, % line "ML:"mx ":"my "`nDE:"de "`n"
		prc := prc_old
		prc_old:=
		break
		
	}
}
sleep, 2000
WinActivate, Macro
return
}

M_Program:
Tooltip,  프로그램을 선택해주세요
KeyWait, LButton, D 
KeyWait, LButton, U
WinGetActiveTitle, Title 
WinGet, active_id, id, % Title
Winget, active_process, processName, ahk_id %active_id%
RealwinSize(x, y, w, h)
GuiControl, , gline, % "SE:ahk_exe " active_process ":"x ":" y ":"w ":"h "`n"


selectFlag = true
gui, 1:new
gui, 1:-Caption - Border + AlwaysOnTop
gui, 1:color, 0xFF44AA
gui, 1:Show, % "X"x " Y"y " W"w " H"h, Area
WinSet, Transparent, 60, Area
tooltip
sleep, 3000
gui, 1:Destroy
WinActivate, Macro
return

M_Exit:

return

RealwinSize(ByRef Xpos, ByRef Ypos, ByRef width, ByRef height) {
WinGetPos,x,y,w,h, % "ahk_exe" active_process
SysGet, wFrame, 32
SysGet, wCaption, 4
Xpos :=x+wFrame
Ypos :=y+wFrame+wCaption
width:=w-wFrame*2
height:=h-wCaption-wFrame
return
}

^Esc::
ExitApp
