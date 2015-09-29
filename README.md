# Fetch movie ratings from console
The script fetches the movie/movies rating(imdb) and displays that on the console.

### Api used
The script uses omdb api to fetch movie related data. Here's a link for that -> [omdb api](http://omdbapi.com).

### Modules required
One external module namely requests is required. One can get the module from [here](http://docs.python-requests.org/en/latest/user/install/#install)

### What if movie names in the folder are not proper (like xyz.2014.1080p.mp4) ?
The script makes some rough guesses to reduce such names to proper ones. It can reduce the above written name to 'xyz' and then make search for it. However, only few such patterns can be reduced. If the movie is not found, try renaming it or search for it by name.
