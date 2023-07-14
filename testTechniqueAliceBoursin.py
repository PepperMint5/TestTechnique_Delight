"""
Test technique Delight

testTechniqueAliceBoursin.py
@author : Alice Boursin

This code interacts with the Spotify API to obtain and analyze the album names of Orelsan. It compares the album names pair-wise to extract the longest common substring. The script then prints the list of these substrings, sorted by length.
"""

import numpy as np
import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials

# Identifiants de l'application Spotify
client_id = '5455b174dd284e5f96c4082e36b9a0d7'
client_secret = '9d3eb4146c5145028ab59309c17a940c'

# Initialisation de l'objet Spotipy
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Fonction pour obtenir les noms des albums d'un artiste
def get_album_names(artist_name):
    results = sp.search(q='artist:' + artist_name, type='artist')
    artist_id = results['artists']['items'][0]['id']
    albums = sp.artist_albums(artist_id)
    album_names = [album['name'] for album in albums['items']]
    return album_names

# Récupération des noms des albums d'Orelsan
artist_name = 'Orelsan'
album_names = get_album_names(artist_name)
print('Liste des albums d\'Orelsan : \n',album_names, "\n\n\n")

# Fonction pour extraire le substring commun le plus long
def extract_longest_common_substring(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    common_substring_lengths = np.zeros((len_s1 + 1, len_s2 + 1), dtype=int)
    max_len = 0
    end_index = 0

    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                common_substring_lengths[i][j] = common_substring_lengths[i - 1][j - 1] + 1
                if common_substring_lengths[i][j] > max_len:
                    max_len = common_substring_lengths[i][j]
                    end_index = i

    return s1[end_index - max_len: end_index]

#Exemple de recherche de substring
if len(album_names) >= 2:
    random_elements = random.sample(album_names, 2)
    print("Sélection de deux albums aléatoires : ", "\n", random_elements[0], "\n", random_elements[1],"\n")
    print("Plus grande sous chaine commune : ",extract_longest_common_substring(random_elements[0], random_elements[1]))

# Fonction pour afficher les substring triés par longueur
def print_substrings(album_names):
    substrings = []
    num_albums = len(album_names)

    for i in range(num_albums):
        for j in range(i+1, num_albums):
            common_substring = extract_longest_common_substring(album_names[i], album_names[j])
            if common_substring:
                substrings.append(common_substring)

    substrings.sort(key=len, reverse=True)
    for substring in substrings:
        print(substring)

#Exemple donné pour l'exercie 2
print("\n\nExemple exercice 2 \n")
album_names = ["aaaaaaaa communcommun bbbb", "commun ccccc", "rien"]
print("Extraction des substrings de ", album_names, "\n")
print_substrings(album_names)

#Nb: j'ai considéré qu'il y avait bien des chaines en commun entre "rien" et les deux premières chaines puisqu'on a le n dans rien et dans "commun".

#Exemple d'utilisation
print("Exemple avec tous les albums d\'Orelsan récupérés sur l'API Spotify : \n")
artist_name = 'Orelsan'
album_names = get_album_names(artist_name)
print_substrings(album_names)






















