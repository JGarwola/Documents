reset
set term x11
set title "static structure factor"
unset xlabel
unset ylabel
set hidden3d
set view 40,50
set ticslevel 0
set contour
set view 45,55
splot'sofk' with lines
pause 6
reread
