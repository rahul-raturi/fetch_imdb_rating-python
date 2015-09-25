#!/usr/bin/env python2

import requests
from string import digits
from os import system, listdir


def fetch_rating(movie):
	search_url = "http://omdbapi.com/?t="+movie+"&type=movie"
	print search_url
	movie_data = requests.get(search_url).json()
	if movie_data['Response'] == "False":
		return ' ', ' '
	return movie_data['Title'], movie_data['imdbRating']


def gather_results(movies_list):
	movies = list()
	for movie in movies_list:
		tmp = fetch_rating(movie)
		if tmp[0] == ' ':
			tmp[0] = movie
			tmp[1] = 'N/A'
		movies.append(tmp)
	return movies

def display_results(movies):
	system('clear')
	top_bar = '{0: ^50}'.format('Title') + '|' + '{0: ^9}'.format('Rating')
	print top_bar
	print '-'*len(top_bar)

	for movie in movies:
		if(len(movie[0]) > 50):
			title = title[0:47] + '...'
		print '{0: <50}'.format(movie[0])+'|'+'{0: ^9}'.format(movie[1])

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
		name = name.encode('utf-8', 'ignore')
		if name != None:
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
		movies.append('+'.join(raw_input("Enter movie name: ").split()))
		display_results(movies)
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
