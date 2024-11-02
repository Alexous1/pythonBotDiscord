
# Création du bot

Pour créer un bot, il faut d'abord créer une application dans lequel on va créer notre bot.
Pour ça, il suffit de vous rendre dans le portail des développeurs de Discord, cliquer sur New Application et donner un nom à votre application.
Ensuite, rendez-vous dans l'onglet Bot et cliquez sur 'Add Bot' pour créer un bot dans l'application.
Et voilà, vous avez créé votre premier bot 🤖

# Ajouter le bot à un serveur

Pour pouvoir utiliser votre bot, il va falloir l'ajouter à un serveur.
Pour inviter le bot sur un serveur, il faut générer une url d'authorisation avec OAuth2.
Heureusement pour nous, le portail des développeurs de Discord nous permet de générer très facilement cette url avec les bonnes permissions.
Dans l'onglet OAuth2, cochez la case 'bot'  et sélectionnez les permissions que vous souhaitez accorder à votre bot:

Ensuite, copiez l'URL générée (4) et accédez-y dans un nouvel onglet. Cette URL va vous permettre d'ajouter votre bot dans les serveurs sur lesquels vous disposez des droits nécessaires.
Sélectionnez votre serveur dans le menu déroulant et validez les permissions que vous souhaitez accorder à votre bot.

Puis faite votre code en python.
Il vous faudra juste remplacer le token prensent dans la dernière ligne du programme. Remplacer votre token par celui de votre bot ue vous trouverez dans l'onglet bot puis cliquer sur le token pour le copier
