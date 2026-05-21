import os
import subprocess
import json

os.makedirs("audios", exist_ok=True)

video_extensions = {".mp4", ".mkv", ".webm", ".mov", ".avi"}

def has_audio(filepath):
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json",
         "-show_streams", filepath],
        capture_output=True, text=True
    )
    info = json.loads(result.stdout)
    return any(s["codec_type"] == "audio" for s in info.get("streams", []))

files = os.listdir("videos")
for file in files:
    name, ext = os.path.splitext(file)
    if ext.lower() not in video_extensions:
        continue

    filepath = f"videos/{file}"

    if not has_audio(filepath):
        print(f"Skipping (no audio): {file}")
        continue

    try:
        yt_id = name.split("[")[1].split("]")[0]
        title = name.split(" [")[0].strip()
        title = title.replace("/", "-").replace("｜", "-").replace("  ", " ").strip()
    except IndexError:
        print(f"Skipping (unexpected format): {file}")
        continue

    output = f"audios/{yt_id}_{title}.mp3"
    print(f"{file} -> {output}")
    subprocess.run(["ffmpeg", "-i", filepath, output], check=True)