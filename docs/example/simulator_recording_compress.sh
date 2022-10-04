#!/bin/bash
recordings_path="${HOME}/Library/Caches/MockServer/recordings"
recording_path="${recordings_path}/tmp.mp4"
recording_compressed_path="${recordings_path}/tmp-compressed.mp4"
mkdir -p "${recordings_path}"
[ -e "${recording_compressed_path}" ] && rm "${recording_compressed_path}"

ffmpeg -i "${recording_path}" -vcodec h264 -b:v 600k -acodec mp3 "${recording_compressed_path}" -loglevel error

rm "${recording_path}"
mv "${recording_compressed_path}" "${recording_path}"