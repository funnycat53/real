fails = open("teksts.txt", "w", encoding="utf-8")       # r - read; w - write (vienkarsi pieraksta un izdzes visu ieprieksejo); a - append (pieraksta kko beigas, bet neko neizdzes)
fails.write("Goat talk")
fails.close