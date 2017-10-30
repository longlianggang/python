@echo on
set path1=D:\work\auto_script\test.txt
set path2=D:\work\auto_script\test1.txt
set path3=D:\work\auto_script

for /f %%i in  ('dir /AD/B %path3% ^|findstr [0-9]') do copy /y %path1% %path3%\%%i\index.html


