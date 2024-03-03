set_0 = {"Comedy", "Drama", "Adventure", "Western", "Horror", "Science Fiction"}
set_1 = {"Action", "Melodrama", "Western", "Horror", "Mystery", "Comedy"}

print(
    f"""intersection set : {set_0.intersection(set_1)} \U0001f607
difference set 0 : {set_0.difference(set_1)} \U0001f608
difference set 1 : {set_1.difference(set_0)} \U0001f609
symmetric difference eset : {set_0.symmetric_difference(set_1)} \U0001f610"""
)
