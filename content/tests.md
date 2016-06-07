Title: Tests fonctionnels 
Description: Tests fonctionnels de votre intégration à la plateforme Le.Taxi

##### Comment tester votre intégration à la plateforme Le.Taxi

  Le cahier de recette est le suivant :
- vérification de la conformité aux CGU : respect de l'identité le.taxi, ergonomie, éléments de langage, ségrégation des offres non-maraude...

Pour un opérateur :
- enrôler un taxi avec numéro et commune d'ADS, numéro et département de carte professionnelle et immatriculation du véhicule
- enrôler un taxi avec les caractéristiques du véhicule et des services à bord
- bouton activer/désactiver le.taxi dans les paramètres
- bouton libre/occupé
- le taxi est visible lorsque dans sa zone et "libre"
- le taxi est invisble lorsque hors de sa zone ou "occupé"
- recevoir une course : confirmer, recevoir la reconfirmation client
- recevoir une course : confirmer, recevoir la non-reconfirmation client, information du chauffeur et repassage en libre
- recevoir une course : ne pas confirmer
- recevoir une course : constater le dépassement du délai d'attente de la confirmation par le chauffeur
- recevoir une course : confirmer, recevoir la reconfirmation client, puis annuler chauffeur
- recevoir une course : confirmer, recevoir la reconfirmation client, recevoir ensuite une annulation client, information du chauffeur et repassage en libre 
- signaler un client indélicat a posteriori

Pour un moteur de recherche :
- rechercher les taxis autour de soi
- afficher les détail d'un taxi : voir à minima son Opérateur, et éventuellement tout ou partie de ses caractéristiques
- héler un taxi : impossible avant d'avoir validé son numéro de mobile par un mécanisme de sécurité
- valider son numéro de mobile par un mécanisme de sécurité (ex: code par SMS)
- héler un taxi avec un numéro vérifié : recevoir la confirmation du chauffeur, afficher un message de re-confirmation conforme aux CGU, re-confirmer client
- héler un taxi avec un numéro vérifié : recevoir la confirmation du chauffeur, afficher un message de re-confirmation conforme aux CGU, ne pas re-confirmer client
- héler un taxi avec un numéro vérifié : recevoir la confirmation du chauffeur, afficher un message de re-confirmation conforme aux CGU, constater le dépassement du délai d'attente de la reconfirmation client
- héler un taxi avec un numéro vérifié : recevoir la non-confirmation du chauffeur, informer le client, retour au choix d'un taxi
- héler un taxi avec un numéro vérifié : recevoir la confirmation du chauffeur, afficher un message de re-confirmation conforme aux CGU, re-confirmer client, puis annuler client
- héler un taxi avec un numéro vérifié : recevoir la confirmation du chauffeur, afficher un message de re-confirmation conforme aux CGU, re-confirmer client, recevoir une annulation chauffeur, informer le client, retour au choix d'un taxi
- évaluer une course a posteriori


