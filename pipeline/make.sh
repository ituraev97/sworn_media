#!/bin/bash
# Full build of one episode: long + Shorts.  usage: make.sh <episode_dir> <workdir> [long|shorts|all]
# Needs episode.json, short1..N.json, thumb.json, meta.json in <episode_dir>. Output in <workdir>/out.
set -e
E=$(realpath "$1"); W=$(realpath -m "$2"); WHAT=${3:-all}; P=$(dirname "$(realpath "$0")")
export NODE_PATH=$(npm root -g)
mkdir -p "$W/out"
mux() { # $1 workdir $2 out.mp4 $3 crf
  ffmpeg -nostdin -v error -y -i "$1/video.mp4" -i "$1/mix.wav" -map 0:v -map 1:a -c:v libx264 -preset medium -crf "$3" -pix_fmt yuv420p \
    -c:a aac -b:a 192k -shortest -movflags +faststart "$2"
}
if [ "$WHAT" != shorts ]; then
  python3 "$P/tts.py" "$E/episode.json" "$W" 0.98
  python3 "$P/timeline.py" "$E/episode.json" "$W" long
  node "$P/render.js" "$W" "$E" "$W/video.mp4" 2
  python3 "$P/audio.py" "$W"
  mux "$W" "$W/out/long.mp4" 21
  S=$(stat -c %s "$W/out/long.mp4")
  if [ "$S" -gt 95000000 ]; then
    D=$(python3 -c "import json;print(json.load(open('$W/timeline.json'))['total'])")
    BR=$(python3 -c "print(int(92e6*8/$D/1000)-200)")
    ffmpeg -nostdin -v error -y -i "$W/video.mp4" -i "$W/mix.wav" -map 0:v -map 1:a -c:v libx264 -preset medium -b:v ${BR}k -maxrate $((BR*2))k -bufsize $((BR*2))k \
      -pix_fmt yuv420p -c:a aac -b:a 160k -shortest -movflags +faststart "$W/out/long.mp4"
  fi
  ffmpeg -nostdin -v error -y -i "$W/out/long.mp4" -vf "fps=1/8,scale=320:180,tile=8x10" -frames:v 1 "$W/out/contact_long.jpg"
  python3 "$P/describe.py" "$E" "$W" > /dev/null
  node "$P/thumb.js" "$E/thumb.json" "$E" "$W/out"
fi
if [ "$WHAT" != long ]; then
  for f in "$E"/short*.json; do
    n=$(basename "$f" .json | sed 's/short//'); SW="$W/s$n"; mkdir -p "$SW"
    python3 "$P/tts.py" "$f" "$SW" 1.05
    python3 "$P/timeline.py" "$f" "$SW" short
    node "$P/render.js" "$SW" "$E" "$SW/video.mp4" 2
    python3 "$P/audio.py" "$SW"
    mux "$SW" "$W/out/s$n.mp4" 19
    ffmpeg -nostdin -v error -y -i "$W/out/s$n.mp4" -vf "fps=1/4,scale=216:384,tile=12x1" -frames:v 1 "$W/out/contact_s$n.jpg"
  done
fi
for f in "$W"/out/*.mp4; do echo "$(basename $f) $(ffprobe -v error -show_entries format=duration -of csv=p=0 $f)s $(du -m $f | cut -f1)MB"; \
  ffmpeg -nostdin -i "$f" -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1; done
