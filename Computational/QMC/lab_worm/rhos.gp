reset
set term x11
set title "superfluid fraction"
unset key
set xlabel "block index"
set ylabel "superfluid fraction"
plot'<grep rhos_ worm.out' using 0:1 with lines,''using 0:2:3 with errorbars
pause 3
reread
