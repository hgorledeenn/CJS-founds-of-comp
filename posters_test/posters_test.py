import os
import subprocess

# 🎵 SONG DATA: title, artist, URL
videos = [
    {
        "name": "Vogue",
        "artist": "Madonna",
        "url": "https://www.youtube.com/watch?v=GuJQSAiODqI"
    },
    {
        "name": "Down Under",
        "artist": "Men At Work",
        "url": "https://youtu.be/XfR9iY5y94s?si=PBVIzbO3MTyuzLRX"
    },
    {
        "name": "We Didn't Start The Fire",
        "artist": "Billy Joel",
        "url": "https://youtu.be/eFTLKWw542g?si=6nEcHVGRxo-T5Div"
    },
    {
        "name": "Take On Me",
        "artist": "A-ha",
        "url": "https://youtu.be/djV11Xbc914?si=QfdUQgO5P8dDRi4L"
    },
    {
        "name": "The Mother",
        "artist": "Brandi Carlile",
        "url": "https://youtu.be/npSDM26xlzs?si=q7fcxWwyu9UTmCen"
    },
    {
        "name": "We Pray",
        "artist": "Coldplay",
        "url": "https://youtu.be/VlSEIa1zubs?si=sSkR5RISYNXvYyqt"
    },
    {
        "name": "Pennoyer v Neff",
        "artist": "The Greens",
        "url": "https://www.youtube.com/watch?v=07ROg1juqpE"
    }
]

# 📁 Root directories
parent_d = "/Users/hgorledeenn/Desktop/posters_test"
videos_dir = os.path.join(parent_d, "videos")
screenshots_dir = os.path.join(parent_d, "screenshots")
posters_dir = os.path.join(parent_d, "posters")

for d in [videos_dir, screenshots_dir, posters_dir]:
    os.makedirs(d, exist_ok=True)

os.chdir(parent_d)

for vid in videos:
    title = vid["name"]
    artist = vid["artist"]
    url = vid["url"]

    # A safe lowercase file identifier
    safe_name = f"{title.lower().replace(' ', '_')}_{artist.lower().replace(' ', '_')}"

    print(f"\n🎬 Processing {title} — {artist}...")

    # ---------- 1. Download video ----------
    video_path = os.path.join(videos_dir, f"{safe_name}.mp4")
    print("⬇️ Downloading video...")
    subprocess.run([
        "yt-dlp", "-f", "bestvideo+bestaudio/best",
        "-o", video_path, "--merge-output-format", "mp4", url
    ], check=True)

    # ---------- 2. Extract 1×1 frames ----------
    ss_subdir = os.path.join(screenshots_dir, safe_name)
    os.makedirs(ss_subdir, exist_ok=True)

    print("🖼 Extracting 1x1 color frames...")
    subprocess.run([
        "ffmpeg", "-i", video_path, "-vf", "scale=1:1",
        os.path.join(ss_subdir, "%06d.png")
    ], check=True)

    # ---------- 3. Combine vertically ----------
    poster_raw = os.path.join(posters_dir, f"{safe_name}_raw.png")
    print("🧩 Combining frames into vertical strip...")
    subprocess.run(
        f'convert -append "{ss_subdir}"/*.png "{poster_raw}"',
        shell=True, check=True
    )

    # ---------- 4. Resize to 4000×6000 ----------
    poster_final = os.path.join(posters_dir, f"{safe_name}.png")
    print("📏 Resizing to 3000x5000...")
    subprocess.run([
        "mogrify", poster_raw, "-resize", "3000x5000!", poster_raw
    ], check=True)

    # ---------- 5. Add 500px white border ----------
    print("🖼 Adding 500px white border...")
    subprocess.run([
        "mogrify", "-bordercolor", "white", "-border", "500", poster_raw
    ], check=True)

    # ---------- 6. Add title + artist ----------
    label = f"{title}, {artist}"
    print(f"📝 Adding title: {label}")
    subprocess.run([
        "mogrify", "-gravity", "north",
        "-pointsize", "200",
        "-font", "Butler",  # Make sure this font is installed; change if needed
        "-fill", "black",
        "-annotate", "+0+125", label,
        poster_raw
    ], check=True)

    print(f"✅ Finished poster: {poster_raw}")

print("\n🏁 All posters created successfully!")
