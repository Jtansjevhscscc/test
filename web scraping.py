import requests
from bs4 import BeautifulSoup
from termcolor import colored
import os

os.system('cls')

# Liste de lien vide  (les liens sont ajoutés pendant la vérification)
liens_valides = []

# Possibilité de rajouter une boucle avec input pour ajouter des noms
noms = [
    # "88klauss88",
    # "jdlc59",
    # "delacencelleriejimmy",
    # "delacencellerie.jimmy",
    # "jimmydelacencellerie",
    # "jimmy.delacencellerie",
    # "xdehjxfkyhxktxky"
    "demoustierchristelle",
    "christelledemoustier",
    "demoustier.christelle",
    "jimmydelacencellerie",
    "christelle.demoustier",
    ]

# Vérifier si un compte Instagram existe (recherche du titre)
print('\033[38;2;138;58;185m' + '\n                                   In' + '\033[38;2;188;42;141m' + 'st' + '\033[38;2;205;72;107m' + 'a' + '\033[38;2;251;173;80m' + 'gr' + '\033[38;2;252;204;99m' + 'am' + '\033[37m')
liens_valides.append('\033[38;2;138;58;185m' + '\nIn' + '\033[38;2;188;42;141m' + 'st' + '\033[38;2;205;72;107m' + 'a' + '\033[38;2;251;173;80m' + 'gr' + '\033[38;2;252;204;99m' + 'am' + '\033[37m')
for nom in noms:
    url_instagram = f"https://instagram.com/{nom}/"
    reponse = requests.get(url_instagram)
    soup = BeautifulSoup(reponse.text, features="lxml")
    title_instagram = soup.find('title').text
    if title_instagram == "Instagram" or title_instagram == "":
        print(f"Le compte {nom} n'existe pas.")
    else:
        print(f"Le compte existe sous le nom {title_instagram}.")
        liens_valides.append(url_instagram)

# Vérifier si un compte Facebook existe (nombre d'image(s) sur la page)
print('\033[34m' + "\n                                   Facebook" + '\033[0m')
liens_valides.append('\033[34m' + "\nFacebook" + '\033[0m')
for nom in noms:
    url_facebook = f"https://www.facebook.com/{nom}"
    reponse = requests.get(url_facebook)
    soup = BeautifulSoup(reponse.text, features="lxml")
    title_facebook = soup.findAll('img')
    if len(title_facebook) != 1:
        print(f"Le compte existe sous le nom {nom}.")
        liens_valides.append(url_facebook)
    else:
        print(f"Le compte {nom} n'existe pas.")
		
# Vérifier si un compte Tiktok existe (recherche du titre)
print(colored("\n                                   ", "white") + colored("Tik", "white", "on_cyan") + colored("Tok", "white", "on_magenta"))
liens_valides.append(colored("\n", "white") + colored("Tik", "white", "on_cyan") + colored("Tok", "white", "on_magenta"))
for nom in noms:
    url_tiktok = f"https://www.tiktok.com/@{nom}"
    reponse = requests.get(url_tiktok)
    soup = BeautifulSoup(reponse.text, features="lxml")
    title_tiktok = soup.find('title').text
    if title_tiktok == " | TikTok":
        print(f"Le compte {nom} n'existe pas.")
    else:
        print(f"Le compte existe sous le nom {title_tiktok}.")
        liens_valides.append(url_tiktok)
		
# Vérifier si un compte Snapchat existe (recherche du titre)
print('\033[33m' + "\n                                   Snapchat" + '\033[0m')
liens_valides.append('\033[33m' + "\nSnapchat" + '\033[0m')
for nom in noms:
    url_snapchat = f"https://www.snapchat.com/add/{nom}"
    reponse = requests.get(url_snapchat)
    soup = BeautifulSoup(reponse.text, features="lxml")
    title_snapchat = soup.find('title').text
    if title_snapchat == "Snapchat":
        print(f"Le compte {nom} n'existe pas.")
    else:
        print(f"Le compte existe sous le nom {title_snapchat}.")
        liens_valides.append(url_snapchat)
		
# Modifier pour écire dans un fichier, à faire une fois le code terminé
print("")
print("")
print("")
for i in liens_valides:
    print(i)