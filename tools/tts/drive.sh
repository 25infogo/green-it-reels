# usage: drive.sh slug... ; runs synth per slug with retries, total budget ~560s
end=$((SECONDS+540))
for s in "$@"; do
  for a in 1 2 3; do
    [ $SECONDS -ge $end ] && { echo "BUDGET"; exit 0; }
    timeout $((end-SECONDS)) python3 synth.py /home/claude/tts/vo $s > run_$s.log 2>&1; rc=$?
    grep -P "\.wav\t" run_$s.log | cut -f1,2 | sed "s/^/  /"
    grep -q SYNTH_DONE run_$s.log && { echo "$s OK"; break; } || echo "$s rc=$rc retry"
  done
done
