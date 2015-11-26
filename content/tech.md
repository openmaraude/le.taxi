Title: Documentation technique
Description: La documentation technique de la plateforme Le.Taxi


## Contexte
Le _Registre de Disponibilité des Taxis_ est un Point d'Echange de Taxis (ou TXP : Taxi Exchange Point) dont la finalité est de faciliter la mise en relation des taxis et leurs clients.
Les clients peuvent utiliser des _Moteurs de recherche de Taxis_ pour héler des taxis géolocalisés par des _Opérateurs de Taxis_.

Le _Registre de Disponibilité des Taxis_ sert d'intermédiaire entre les _Moteurs de recherche de Taxis_ et les _Opérateurs de Taxis_.


## Implémentation
La présente documentation donne un aperçu des APIs REST du _Registre de Disponibilité des Taxis_. Ces APIs REST fournissent un accès aux ressources du registre (data entities) via des Identifiants Uniformes de Ressources (ou URI : Uniform Resource Identifier). Pour utiliser ces APIs REST, votre application fait une requète HTTPS et analyse la réponse reçue. Les méthodes utilisées sont les méthodes HTTP standard comme <code>GET</code> , <code>PUT</code> et <code>POST</code>. Ces APIs REST opèrent sur HTTPS, ce qui permet de les utiliser aisément depuis n'importe quel langage de programmation. Le format d'entrée et de sortie pour les APIs REST du _Registre de Disponibilité des Taxis_ est <a href="http://www.json.org/">JSON</a>.

La documentation complètes des APIs REST du _Registre de Disponibilité des Taxis_ est librement accessible ici : <a href="https://api.taxi/documentation">https://api.taxi/documentation</a>.


## Authentification
L'authentification de l'application accédant au _Registre de Disponibilité des Taxis_ est faite lors de chaque requète en incluant une en-tête HTTP <code>X-API-KEY</code>.


Les clés d'API sont accessibles pour les développeurs accrédités ici : <a href="https://api.taxi/user_key">https://api.taxi/user_key</a>.

Si vous souhaitez implémenter l'API du _Registre de Disponibilité des Taxis_, vous pouvez commencer par étudier la documentation, librement accessible, puis demandez une clé d'API en écrivant à l'adresse : apikey -[a<nop>t]- le.taxi

## Infrastructure
Les environnements des développement, recette et production sont les suivants :

<table class="table table-striped table-bordered table-condensed">
<thead>
<th>
<td>Requètes HTTPS</td>
<td>Géolocalisation UDP</td>
<td>Documentation</td>
</th>
</thead>
<tbody>
<tr>
<td>DEV</td>
<td>dev.api.taxi</td>
<td>geoloc.dev.api.taxi</td>
<td><a href="https://dev.api.taxi/documentation">Documentation</a></td>
</tr>

<tr>
<td>TEST</td>
<td>test.api.taxi</td>
<td>geoloc.test.api.taxi</td>
<td><a href="https://test.api.taxi/documentation">Documentation</a></td>
</tr>

<tr>
<td>PROD</td>
<td>api.taxi</td>
<td>geoloc.api.taxi</td>
<td><a href="https://api.taxi/documentation">Documentation</a></td>
</tr>
</tbody>
</table>



L'état des services peut être suivi en temps réel sur la page suivante : <a href="http://opendatataxi.fr/status/">Etat des services</a>.


Les anciens serveurs de développement (api[-dev].opendatataxi.fr et geoloc.opendatataxi.fr) seront maintenus quelques temps avant d'être décommissionés.
