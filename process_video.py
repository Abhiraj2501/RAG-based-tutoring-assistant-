import os
import subprocess

os.makedirs("audios", exist_ok=True)

video_extensions = {".mp4", ".mkv", ".webm", ".mov", ".avi"}

files = os.listdir("videos")
for file in files:
    name, ext = os.path.splitext(file)
    if ext.lower() not in video_extensions:
        continue

    try:
        # Extract YouTube ID from [xxxxx] at the end
        yt_id = name.split("[")[1].split("]")[0]
        # Extract title — everything before ' ['
        title = name.split(" [")[0].strip()
        # Clean title for filesystem use
        title = title.replace("/", "-").replace("｜", "-").replace("  ", " ").strip()
    except IndexError:
        print(f"Skipping (unexpected format): {file}")
        continue

    output = f"audios/{yt_id}_{title}.mp3"
    print(f"{file} -> {output}")
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", output], check=True)

    