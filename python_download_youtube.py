# encoding : utf-8
# for python3

import os
from pytube import YouTube

yt = YouTube()
save_path = 'python_download_youtube'
def download(url):
	yt.url = url
	video = yt.get('mp4')
	if not os.path.exists(save_path):
		os.mkdir(save_path)
	try:
		video.download('./' + save_path +'/')
		print ("ダウンロードが完了しました")
	except AttributeError:
		print ("この動画はダウンロード出来ないようです，ごめんなさい")
		
if __name__ == '__main__':
	print ("ダウンロードしたい動画のURLを入力してください")
	input_url = input('>>> ')
	target_url = input_url
	download(target_url)
	