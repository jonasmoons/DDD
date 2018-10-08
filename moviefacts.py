favo_movie = {
	"title" : "Interstellar",
	"director" : "Christopher Nolan",
	"year" : 2014,
	"duration" : 169
}

favo_movie["actors"] = "Matthew McConaughey", "John Lithgow", "Matt Damon"

for stats, value in favo_movie.items():
	value = favo_movie[stats]
	#print(f"{stats} : {value}")

	if stats == "duration":
		print(f"{stats} : {value} minutes")
	elif stats == "actors":
		value = ", ".join(value)
		print(f"{stats} : {value} ")


	#print(favo_movie)