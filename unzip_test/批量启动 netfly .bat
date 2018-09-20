@echo off

for /L %%i  in (1,1,50) do (

 start /d "D:\netfly\ts%%i" netfly.exe

)

@Pause>nul