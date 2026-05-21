import os
import subprocess
import json

os.makedirs("audios", exist_ok=True)

video_extensions = {".mp4", ".mkv", ".webm", ".mov", ".avi"}

def has_audio(filepath):
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_streams", filepath],
        capture_output=True, text=True
    )
    info = json.loads(result.stdout)
    return any(s["codec_type"] == "audio" for s in info.get("streams", []))

def next_index(audios_dir="audios"):
    existing = [f for f in os.listdir(audios_dir) if f.endswith(".mp3")]
    indices = []
    for f in existing:
        try:
            indices.append(int(f.split("_")[0]))
        except ValueError:
            pass
    return max(indices, default=0) + 1

files = sorted(os.listdir("videos"))
counter = next_index()

for file in files:
    name, ext = os.path.splitext(file)
    if ext.lower() not in video_extensions:
        continue

    filepath = f"videos/{file}"

    if not has_audio(filepath):
        print(f"Skipping (no audio): {file}")
        continue

    try:
        title = name.split(" [")[0].strip()
        title = title.replace("/", "-").replace("｜", "-").replace("  ", " ").strip()
        # strip hashtags
        title = " ".join(w for w in title.split() if not w.startswith("#")).strip()
    except Exception:
        print(f"Skipping (unexpected format): {file}")
        continue

    output = f"audios/{counter:02d}_{title}.mp3"

    # skip if already converted
    if os.path.exists(output):
        print(f"Already exists, skipping: {output}")
        counter += 1
        continue

    print(f"{file} -> {output}")
    subprocess.run(["ffmpeg", "-i", filepath, output], check=True)
    counter += 1