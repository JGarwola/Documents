reset
set title "number of particles"
set xlabel "block index"
set ylabel "N"
unset key
plot'< grep etot worm.out'u 0:1 with lines,''using 0:2:3 with errorbars
pause 3
reread
