from pytube import YouTube

def progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print("Download: " + str(round(percentage_of_completion, 2)) + "%")

    if (percentage_of_completion == 100):
        print("Successfully downloaded '" + yt.title + "' to \n" + filePath + "\n")

## Macbook File Path
# filePath = "/Users/lorenzcastillo/Downloads/Videos/Youtube Videos"

## Desktop File Path
filePath = "D:/Adobe Premiere Pro/Downloads"

link = input("\nEnter the YouTube link you want to download: \n")
yt = YouTube(link)

# Register the callback
yt.register_on_progress_callback(progress)

yd = yt.streams.filter(progressive=True).get_highest_resolution()
yd.download(filePath)