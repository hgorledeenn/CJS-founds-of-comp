from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=MdMnPrUxm1w"

# Options for yt-dlp
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # best quality available
    'merge_output_format': 'mp4',          # combine into mp4
    'outtmpl': '~/Downloads/%(title)s.%(ext)s',  # save in Downloads
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
