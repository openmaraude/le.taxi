---
layout: one-section
title: Documentation technique
---

# Contexte

Le _Registre de Disponibilité des Taxis_ est un Point d’Echange de Taxis (ou TXP : Taxi Exchange Point) dont la finalité est de faciliter la mise en relation des taxis et leurs clients. Les clients peuvent utiliser des _Moteurs de recherche de Taxis_ pour héler des taxis géolocalisés par des _Opérateurs de Taxis_.

Le _Registre de Disponibilité des Taxis_ sert d’intermédiaire entre les _Moteurs de recherche de Taxis_ et les _Opérateurs de Taxis_.

# Implémentation

La présente documentation donne un aperçu des APIs REST du _Registre de Disponibilité des Taxis_. Ces APIs REST fournissent un accès aux ressources du registre (data entities) via des Identifiants Uniformes de Ressources (ou URI : Uniform Resource Identifier). Pour utiliser ces APIs REST, votre application fait une requète HTTPS et analyse la réponse reçue. Les méthodes utilisées sont les méthodes HTTP standard comme `GET` , `PUT` et `POST`. Ces APIs REST opèrent sur HTTPS, ce qui permet de les utiliser aisément depuis n’importe quel langage de programmation. Le format d’entrée et de sortie pour les APIs REST du _Registre de Disponibilité des Taxis_ est [JSON](http://www.json.org/).

La documentation complètes des APIs REST du _Registre de Disponibilité des Taxis_ est librement accessible ici : <https://api.taxi/doc/>.

# Authentification

L’authentification de l’application accédant au _Registre de Disponibilité des Taxis_ est faite lors de chaque requète en incluant une en-tête HTTP X-API-KEY.

Les clés d’API sont accessibles pour les développeurs accrédités ici : <https://api.taxi/user_key>.

Si vous souhaitez implémenter l’API du _Registre de Disponibilité des Taxis_, vous pouvez commencer par étudier la documentation, librement accessible, puis demandez une clé d’API en écrivant à l’adresse : apikey -[at]- le.taxi

# Infrastructure

Les environnements des développement, recette et production sont les suivants :

| | Requètes HTTPS | Géolocalisation UDP | Documentation |
|---|---|---|---|
| DEV | dev.api.taxi | geoloc.dev.api.taxi | [Documentation](https://dev.api.taxi/documentation) |
| TEST | test.api.taxi | geoloc.test.api.taxi | [Documentation](https://test.api.taxi/documentation) |
| PROD | api.taxi |	geoloc.api.taxi | [Documentation](https://api.taxi/documentation) |
{: .table }