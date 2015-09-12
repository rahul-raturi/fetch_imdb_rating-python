# Fetch movie ratings from console
The script fetches the movie/movies rating(imdb) and displays that on the console.

### Api used
The script uses omdb api to fetch movie related data. Here's a link for that -> [omdb api](http://omdbapi.com).

### Modules required
One external module named requests is required. One can get the module from [here](http://docs.python-requests.org/en/latest/user/install/#install)

### What if movie names in the folder are not proper (like xyz.2014.1080p.mp4) ?
The script makes some rough guesses to remove such inconsistencies. It can reduce the above written name to xyz and then search for it. However, only a limited amount of unnecessary information can be reduced. If the movie is not searched, try renaming it.
