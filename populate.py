'''DEMO'''



import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PathOfGrace.settings")  # Replace with your project name
django.setup()

# Import your model
from chant.models import Language, Section, Song, Line, Category  # Replace with your app and model

# Ensure category exists
cat, _ = Category.objects.get_or_create(name="Melodies Joyeuses")#Melodies Joyeuses

# Ensure language exists and assign category
lang, _ = Language.objects.get_or_create(language_type="Créole", category=cat) #["Créole", "Français", "English"]

# Create the song and explicitly provide the 'language' field
song = Song.objects.create(
    title="Lè la vi mwen va fini",
    category = cat,
    category_number=2,  # Assuming this is a numeric field
    language=lang
    # Provide language to avoid NOT NULL constraint error
)

# Add category correctly
#song.category.add(cat)

# Create sections
verse_1 = Section.objects.create(song=song, section_type='verse')
chorus = Section.objects.create(song=song, section_type='chorus')
verse_2 = Section.objects.create(song=song, section_type='verse')
verse_3 = Section.objects.create(song=song, section_type='verse')
verse_4 = Section.objects.create(song=song, section_type='verse')

# Add lines
sections_lines = {
    verse_1: [
        "Lè la vi mwen va fini",
        "E mwen janbe rivyè a,",
        "Lè mwen wè briye",
        "yon maten glorye",
        "M ava konnen Redanmtè mwen",
        "Lè m a rive nan syèl la",
        "E souri Li va pou mwen yon byenveni."
    ],
    chorus: [
        "M ava wè Li, m a konnen Li,",
        "Lè ma kanpe bò kote Jezu Kri;",
        "Ma va wè Li, ma konnen Li",
        "Ak mak klou yo Li genyen nan min Li."
    ],
    verse_2: [
        "Ala kontan m a kontan",
        "Lè m a wè Li fasafas",
        "Ak tout gran amou",
        "Kap briye nan je Li!",
        "O! kè mwen va louwe Li",
        "Pou mizerikòd ak gras!",
        "Ki pare pou mwen",
        "yon bèl plas nan lakay Li."
    ],
    verse_3: [
        "Nan bèl peyi anwo a",
        "Mwen genyen kèk byenneme,",
        "Mwen sonje lè yo te di mwen orevwa",
        "Ak lajwa yo va chante",
        "Lè yo wè m ape rive,",
        "Men mwen ta vle wè",
        "Sovè mwen premyèman."
    ],
    verse_4: [
        "M ape antre nan vil la",
        "Ak yon ròb blan ki san tach",
        "Kote p ap gen soufrans ni tristès ankò;",
        "M ape chante ak zanj yo",
        "Nan yon si bèl amoni",
        "Men mwen ta vle wè",
        "Sovè mwen premyèman."
    ]
}

for section, lines in sections_lines.items():
    for line in lines:
        Line.objects.create(section=section, content=line)

print("✅ Data inserted successfully!")
