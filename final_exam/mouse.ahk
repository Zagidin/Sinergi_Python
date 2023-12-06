#Persistent
SetTimer, ClickLoop, 100

ClickLoop:
Click
Return

Numpad1:: ;
Toggle := !Toggle
if (Toggle)
    SetTimer, ClickLoop, 100
else
    SetTimer, ClickLoop, Off
return