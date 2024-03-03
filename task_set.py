set_0 = {"Comedy", "Drama", "Adventure", "Western", "Horror", "Science Fiction"}
set_1 = {"Action", "Melodrama", "Western", "Horror", "Mystery", "Comedy"}
intersection_set = set_0.intersection(set_1)
difference_set_0 = set_0.difference(set_1)
difference_set_1 = set_1.difference(set_0)
symmetric_difference_set = set_0.symmetric_difference(set_1)

print(
    f"""intersection set : {intersection_set}
difference set 0 : {difference_set_0}
difference set 1 : {difference_set_1}
symmetric difference eset : {symmetric_difference_set}""")
