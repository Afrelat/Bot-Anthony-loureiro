import binary_tree as bt

#  En résumé, le script crée une structure d'arbre binaire avec des messages pour guider l'utilisateur dans l'utilisation d'un bot Discord.
#  Les messages incluent des instructions sur l'utilisation de l'historique, des descriptions de Python et du bot Discord, ainsi qu'un message de fin pour terminer la session avec le bot.

def setup():
    arbre = bt.Binary_Tree()
    arbre.root = bt.Junction("```Voulez-vous accéder aux commandes [L] ou simplement partir [R]?```")
    arbre.root.add_junction("```Voulez-vous accéder aux commandes d'historique [L] ou aux commandes de jeu [R]?```", False)
    arbre.root.add_leaf("```Allez toucher de l'herbe```", True)

    arbre.root.left.add_leaf(
        "```Utilisez $ comme préfixe et :\n\t- S \"votre message\" pour l'enregistrer.\n\t- V \"index du message\" pour afficher l'historique à partir de l'index.\n\t- VF \"nom d'utilisateur\" pour afficher l'historique d'un utilisateur.\n\t- C pour effacer l'historique.\n\t- L pour connaître la longueur.\n\t- SAVE pour écraser le fichier json.\n\t- SA \"sujet\" pour parler d'un sujet.```",
        False)
    arbre.root.left.add_leaf("Pas de jeux pour l'instant", True)

    arbre.add_subject("python", "```Python est un langage de programmation de haut niveau et à usage général. Sa philosophie de conception met l'accent sur la lisibilité du code avec l'utilisation d'une indentation significative via la règle de l'off-side. Python est de type dynamique et collecté par le ramasse-miettes (garbage collector).```")
    arbre.add_subject("pourquoi", "```ce bot Discord est un projet pour mes cours de données```")

    return arbre