reset
set term x11
set title "one-body density matrix"
unset key
set xlabel "r (Angstrom)"
set ylabel "n(r)"
plot'nofr'using 1:2 with lines
pause 5
reread
