#!/bin/bash
recordings_path="${HOME}/Library/Caches/MockServer/recordings"
recording_path="${recordings_path}/tmp.mp4"
mkdir -p "${recordings_path}"

xcrun simctl io booted recordVideo --codec=h264 "${recording_path}" --force