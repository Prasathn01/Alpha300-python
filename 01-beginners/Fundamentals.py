# variables (type comes from the value itself)
song, artist, plays = "Hukum", "Anirudh", 1200
rating = 4.7

# comments: python ignores everything after the #

# datatypes
print(isinstance(song, str), isinstance(plays, int), isinstance(rating, float))   # True True True
for value in [True, complex(-1, 2.5), ["Hukum"], ("Anirudh",), range(3), {"mood": "mass"}, {"tamil"}]:
    print(type(value))
# bool, complex, list, tuple, range, dict, set

# arithmetic: + - * / % ** //
seconds = 245
print(seconds // 60, seconds % 60)    # 4 5  -> 4 min 5 sec
print(seconds / 60)                   # 4.083333333333333
print(plays + 300, plays - 200, plays * 2, 3 ** 4)   # 1500 1000 2400 81

# comparison: == != > >= < <=
old, new = 1200, 1350
print(old == new, old != new, new > old, new >= 1350, old < 1000, old <= 1200)
# False True True True False True

# logical: and, or, not
liked, downloaded = True, False
print(liked and downloaded, liked or downloaded, not liked)   # False True False

# or gives the first truthy value, and gives the first falsy value (else the last one)
print(0.0 or "shuffle", "repeat" or "shuffle", () or 0, 0 or ())
# shuffle repeat 0 ()
print(0.0 and "shuffle", "repeat" and "shuffle", () and 0, 7 and ())
# 0.0 shuffle () ()

# bitwise: & | ^ ~ << >>
p, q = 9, 5     # 1001, 0101
print(p & q, p | q, p ^ q, ~q, q << 3, p >> 2)   # 1 13 12 -6 40 2

# is / in
playlist = ["Hukum", "Arabic Kuthu", "Naa Ready"]
backup = playlist
print(backup is playlist, playlist[:] is playlist)   # True False  ([:] makes a copy)
print("Naa Ready" in playlist, "Rowdy Baby" in playlist)   # True False

# strings
album = "midnight"
album += " melodies"
print(album, "|", album.upper(), "|", album.title())   # midnight melodies | MIDNIGHT MELODIES | Midnight Melodies
print(album.islower(), "LOFI".isupper(), "LoFi".lower())          # True True lofi
print("lofi".isalpha(), "track01".isalnum(), "2024".isdecimal())  # True True True
print(album.startswith("mid"), album.endswith("dies"), "night" in album)   # True True True
print(album.find("melo"), album.replace("midnight", "morning"))   # 9 morning melodies
print(album.split(), " + ".join(album.split()))   # ['midnight', 'melodies'] midnight + melodies

# slicing [start:end:step]
print(album[:3], album[9:], album[::-1])   # mid melodies seidolem thgindim

# complex
w = complex(-1, 2.5)
print(w, w.real, w.imag)   # (-1+2.5j) -1.0 2.5

# built in functions
print(round(seconds / 60, 2), round(2.675, 2))   # 4.08 2.67  (2.67 because floats aren't stored exactly)
print(len(playlist), max(old, new))              # 3 1350

# lists
queue = ["Hukum", 3, "Arabic Kuthu", False, "Naa Ready", 4.5]
queue[2] = "Vaathi Coming"
queue += ["Jalabulajangu"]
print(queue[2:4])   # ['Vaathi Coming', False]
queue.pop()         # removes the last one
queue.insert(0, "Intro")
print(queue)        # ['Intro', 'Hukum', 3, 'Vaathi Coming', False, 'Naa Ready', 4.5]

# tuples (fixed, can't change them)
genres = ("lofi", "kuthu", "melody")
print(genres.index("melody"), genres)   # 2 ('lofi', 'kuthu', 'melody')

# dict
track = {"song": "Hukum", "plays": 1200}
track["plays"] = 1500
print(track)   # {'song': 'Hukum', 'plays': 1500}

# sets
my_taste = {"lofi", "kuthu", "jazz"}
friends = {"jazz"}
print(my_taste - friends)   # lofi and kuthu, any order

# functions
def skip():
    print("next song >>")

skip()
skip()
skip()
