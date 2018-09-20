@echo off


if exist "C:\Users\xt\Desktop\陕西NEI\ts-tester-win-1.0.0.11-setup.zip" goto Win7Choice

:Win7Choice
for /L %%i  in (2,1,3) do (
 winrar x -ad -y ts-tester-win-1.0.0.11-setup.zip D:\netfly\ & ren D:\netfly\ts-tester-win-1.0.0.11-setup ts%%i

 echo D:\netfly\ts%%i\config\config.xml
)

echo .

goto end

:end
echo 请按任意键退出。
@Pause>nul

