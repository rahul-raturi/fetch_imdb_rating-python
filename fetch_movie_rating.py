#!/usr/bin/env python2

import requests
from string import digits
from os import system, listdir


def fetch_rating(movie):
	search_url = "http://omdbapi.com/?t="+movie+"&r=json"
	movie_data = requests.get(search_url).json()
	if movie_data['Response'] == "False":
		return ' ', ' ' 
	return movie_data['Title'], movie_data['imdbRating']


def display_results(movies):
	system('clear')
	top_bar = '{0: ^50}'.format('Title') + '|' + '{0: ^9}'.format('Rating')
	print top_bar
	print '-'*len(top_bar)

	for movie in movies:
		movie = movie.encode('ascii', 'ignore')
		title, rating = fetch_rating(movie.lower())
		if title == ' ':
			title = movie 
		if(len(title) > 50):
			title = title[0:47] + '...'
		print '{0: <50}'.format(title)+'|'+'{0: ^9}'.format(rating)
	
	print '-'*60


def is_year_or_reso(wrd):
	if wrd == '720p' or wrd == '480p' or wrd == '1080p':
		return True
	if len(wrd) != 4:
		return False
	for x in wrd:
		if x not in digits:
			return False
	
	return True


def format_movie_names(files_list):
	movies = list()

	for name in files_list:
		tmp = (name.split('('))[0]
		if (tmp.split('.'))[-1] in ['mp4', 'mkv', 'avi']:
			tmp = ' '.join((tmp.split('.'))[0:-1])
		tmp = ' '.join(tmp.split('.'))
		tmp = ' '.join(tmp.split('_'))
		##To remove years stuck with names of movies
		tmp_ls = tmp.split(' ')
		for i in range(len(tmp_ls)):
			if is_year_or_reso(tmp_ls[i]):
				tmp = ' '.join(tmp_ls[0:i])
				break

		movies.append(tmp)
	
	return movies



def main():
	movies = list()

	system('clear')
	print '{0: ^40}'.format('Search for movie ratings')
	print '-'*40
	print '1 -> Enter movie title'
	print '2 -> Search a local directory for movies'
	choice = raw_input(': ')
	if choice == '1':
		movies.append(raw_input("Enter movie name: "))
	elif choice == '2':
		while True:
			direc = raw_input("Enter directory: ")
			try:
				ls = listdir(direc)
				movies.extend(format_movie_names(ls))
				display_results(movies)
				break

			except OSError:
				print "\nNo such directory, Try again!\n"
	
main()
