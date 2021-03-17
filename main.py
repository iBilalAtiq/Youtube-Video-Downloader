from pytube import YouTube

url = "https://www.youtube.com/watch?v=aXHATNWXC2o"

my_Video = YouTube(url)

#For Title
print(my_Video.title)

#For Thumbnails
print(my_Video.thumbnail_url)

my_Video = my_Video.streams.get_highest_resolution()
my_Video.download()

# my_Video = my_Video.streams.first()
# for stream in my_Video:
# 	print(stream)
