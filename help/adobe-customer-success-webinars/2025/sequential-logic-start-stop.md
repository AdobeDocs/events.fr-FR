---
title: Maîtriser la logique séquentielle dans Adobe Analytics et Customer Journey Analytics - Démarrages et arrêts
description: Principal de la logique séquentielle dans Adobe Analytics avec une segmentation avancée, des contrôles de portée et des champs dérivés pour découvrir les modèles de comportement des clients et clientes et améliorer la précision des données.
solution: Analytics, Customer Journey Analytics
role: Developer
level: Intermediate
doc-type: Event
duration: 3370
last-substantial-update: 2025-05-08T00:00:00Z
jira: KT-18017
source-git-commit: cfc7b54ae4360779ca2c41f88fc08089bae99165
workflow-type: tm+mt
source-wordcount: '768'
ht-degree: 0%

---


# Maîtriser la logique séquentielle dans Adobe Analytics et Customer Journey Analytics : démarrages et arrêts

Au cours de cette session, nous allons découvrir comment configurer des séquences avec l’opérateur THEN dans Adobe Analytics (AA) et Customer Journey Analytics (CJA). Découvrez comment récupérer des sous-ensembles précis d’activités en combinant UNIQUEMENT APRÈS/UNIQUEMENT AVANT LA SÉQUENCE avec les points de contrôle EXCLUDE.

## Points de discussion

* Révision rapide des opérateurs logiques séquentiels autonomes et du framework visuel.
* Décrivez comment l’instruction EXCLUDE affecte les résultats des séquences en utilisant UNIQUEMENT LA SÉQUENCE APRÈS/AVANT.
* Présentez des cas d’utilisation et des démonstrations montrant comment vous pouvez adopter les méthodes de votre entreprise.

>[!VIDEO](https://video.tv.adobe.com/v/3458040/?learn=on&enablevpops)

## Faits saillants


1. Logique séquentielle et segmentation dans Analytics

   * La session s’est concentrée sur les techniques avancées d’application de la logique séquentielle dans les analyses, en soulignant l’importance de comprendre les points de départ et d’arrêt dans les séquences de données pour analyser efficacement les comportements des clients.
   * Les opérateurs séquentiels ont été présentés comme des outils permettant d’identifier des modèles tels que « accès web suivi d’un accès par e-mail » ou « soumission d’une demande suivie de sessions ultérieures ».
   * La nature gourmande de la logique de segment a été mise en évidence, expliquant comment elle renvoie le plus grand jeu de données possible, sauf si elle est contrainte par des conditions supplémentaires.
   * Des techniques de définition de la portée, telles que les séquences « seulement avant » et « seulement après », ont été introduites pour étudier des sous-ensembles de données en fonction de questions commerciales spécifiques.
   * L’utilisation des points de contrôle, des conditions de proximité et des critères d’exclusion a été expliquée afin d’affiner l’analyse des données et de répondre à des questions commerciales complexes.

2. Gestion de plusieurs points ciblés dans l’analyse des données

   * Andy a évoqué les scénarios dans lesquels les clients envoient plusieurs demandes et le besoin d’analyser les comportements après chaque demande plutôt que seulement la première.
   * Des défis tels que le chevauchement des demandes et la définition d&#39;inclure ou d&#39;exclure les points d&#39;intérêt originaux ont été abordés.
   * L’importance de clarifier les hypothèses et d’affiner la logique pour gérer plusieurs occurrences d’une séquence a été soulignée, afin d’assurer une analyse précise des comportements des clients tout au long de leur cycle de vie.

3. Techniques avancées pour arrêter le mappage de données

   * Cette session a présenté des méthodes permettant d’arrêter la correspondance de données à des points de contrôle spécifiques à l’aide de critères d’exclusion, ce qui permet aux analystes d’étudier les données entre les points de départ et d’arrêt définis.
   * Par exemple, l’analyse des comportements entre « accès web suivi d’une interaction avec une application mobile » et l’arrêt à « interaction avec un e-mail ».
   * L&#39;utilisation des conditions « within » et « after » a été expliquée pour appliquer des règles de proximité plus strictes et éviter les résultats inattendus d&#39;une logique gourmande.
   * Andy a montré comment ces techniques peuvent être appliquées pour étudier les comportements des clients par rapport à des événements spécifiques, tels que les soumissions d’applications.

4. Validation et affinement de la logique d’analyse des données

   * Andy a souligné l&#39;importance de valider les hypothèses et de tester la logique pour garantir des résultats précis, car les erreurs dans la création de segments ou les hypothèses de données sont fréquentes.
   * Des exemples de résultats inattendus dus à une logique gourmande ont été partagés, soulignant la nécessité de conditions strictes telles que « dans un événement » ou « dans une session ».
   * Des repères de validation, tels que de petits ensembles de données aux caractéristiques connues, ont été recommandés pour tester et affiner les méthodes d&#39;analyse.

5. Application de la logique séquentielle aux cas d’utilisation réels

   * Andy a fourni des exemples de cas d’utilisation réels, tels que l’analyse du comportement des clients après les soumissions de l’application ou l’identification des actions courantes suite à des achats ou des avis négatifs.
   * La session a montré comment la logique séquentielle peut être appliquée à des modèles d&#39;étude tels que « première session après application » ou « deuxième session après application » sur plusieurs occurrences.
   * On a discuté de l&#39;importance d&#39;étendre l&#39;analyse à des ensembles de données plus vastes tout en maintenant l&#39;exactitude, avec des exemples d&#39;effets en cascade dans les données au niveau de la session.

6. Utilisation de champs dérivés pour une analyse flexible

   * Andy a présenté le concept d’utilisation des champs dérivés dans Adobe Customer Journey Analytics (CJA) pour définir dynamiquement les moments ciblés, ce qui réduit la nécessité de modifier plusieurs filtres pour chaque analyse.
   * Les champs dérivés permettent aux analystes de créer des filtres relatifs à un champ unique, ce qui permet aux ajustements rapides d’étudier différents points ciblés, tels que des applications spécifiques à un produit ou d’autres événements client.

7. Applications pratiques et projets futurs

   * Andy a partagé les plans de la prochaine session du webinaire, qui se concentrera sur les modèles, les aide-mémoire et les applications pratiques des concepts discutés, en passant de la formation aux cas d&#39;utilisation exploitables.
   * La session s&#39;est terminée par un appel aux commentaires via un sondage pour déterminer l&#39;intérêt pour les sujets futurs et assurer l&#39;alignement avec les objectifs des participants.
   * Andy a souligné les micro-engagements de l&#39;équipe d&#39;Ultimate Success, en proposant des sessions de coaching ciblées pour aider les entreprises à appliquer ces concepts à leurs cas d&#39;utilisation spécifiques.

8. Partage de matériel et actions de suivi

   * Andy a confirmé que les documents du webinaire, y compris les enregistrements et les articles de blog, seront partagés avec les participants, fournissant une forme documentée du contenu de la session.
   * Les participants ont été encouragés à contacter leur TAM ou CSM pour obtenir de l’aide supplémentaire et à explorer les licences Ultimate Success pour des sessions de coaching personnalisées.
