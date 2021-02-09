import os
import urllib.request

days = ['01d.png', '02d.png', '03d.png', '04d.png', '09d.png', '10d.png', '11d.png', '13d.png', '50d.png']
nights = ['01n.png', '02n.png', '03n.png', '04n.png', '09n.png', '10n.png', '11n.png', '13n.png', '50n.png']

base_url = 'https://openweathermap.org/img/w/'
img_dir = './img/'
if not os.path.exists(img_dir):
	os.makedirs(img_dir)

# Get the day weather icons
for name in days:
	file_name = img_dir+name
	if not os.path.exists(file_name):
		urllib.request.urlretrieve(base_url+name, file_name)

# Repeat the same thing for night weather icons
for name in nights:
	file_name = img_dir+name
	if not os.path.exists(file_name):
		urllib.request.urlretrieve(base_url+name, file_name)