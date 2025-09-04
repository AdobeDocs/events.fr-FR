---
title: Architecture d’Analysis - Comment aborder votre modèle de données Customer Journey Analytics
description: Découvrez comment structurer les modèles de données CJA avec les hiérarchies d’événements, l’attribution et les KPI afin de déverrouiller des informations plus précises sur le parcours client.
feature: Attribution
role: User
level: Beginner, Intermediate, Experienced
doc-type: Event
duration: 0
last-substantial-update: 2025-09-04T00:00:00Z
jira: KT-18813
source-git-commit: 124b52203b98a80dd9202dab1b0dbe575475a52b
workflow-type: tm+mt
source-wordcount: '325'
ht-degree: 0%

---


# Architecture d’Analysis : approche de votre modèle de données Customer Journey Analytics

L’un des aspects essentiels de la création d’un modèle de données CJA est la compréhension de la relation hiérarchique entre les différents points de contact et interactions. C’est la base d’analyses et d’informations pertinentes.

Les principales considérations sont les suivantes :

* Identification et mappage des points d’interaction client sur tous les canaux
* Établissement de hiérarchies et de relations d’événements claires
* Définir des modèles d’attribution cohérents
* Création de mesures et d’indicateurs clés de performance normalisés

En structurant correctement ces éléments, les entreprises peuvent mieux suivre et analyser l’ensemble du parcours client, ce qui permet d’obtenir des informations plus exploitables et d’améliorer les capacités de prise de décision.

>[!VIDEO](https://video.tv.adobe.com/v/3471111/?learn=on&enablevpops)

## Déverrouiller la modélisation des données pour une analyse puissante

Découvrez comment une architecture de données efficace dans Adobe Experience Platform (AEP) et Customer Journey Analytics (CJA) génère des informations et des rapports exploitables.

* **La conception des schémas est importante** le choix entre des schémas, des tableaux et des tableaux d’objets plats a un impact direct sur les fonctionnalités d’analyse et la flexibilité des rapports.
* **Processus de transformation** les données ingérées dans AEP doivent être soigneusement structurées pour garantir une transformation et une utilisation transparentes dans CJA.
* **Hiérarchie des conteneurs** il est essentiel de comprendre les niveaux d’événement, de session et de personne pour une analyse à plusieurs niveaux et des rapports précis.
* **Stratégies pratiques** planification initiale, gouvernance des schémas et exploitation des fonctionnalités de Platform sont essentielles pour des mises en œuvre évolutives et pérennes.

La maîtrise de ces concepts permet aux équipes d’optimiser leurs workflows d’analyse et de déverrouiller des informations commerciales plus précises.

## Types de schémas et cas d’utilisation

* **Schémas plats** Idéal pour les relations de données simples et individuelles. Idéal pour le suivi d’événement de base et les mesures/dimensions simples.
* **Tableaux** utile pour les listes d’éléments associés (par exemple, les catégories de produits, les balises de contenu). Chaque élément de tableau devient une dimension individuelle à analyser.
* **Tableaux d’objets** conçus pour des cas d’utilisation complexes tels que les achats de produits, où chaque objet conserve ses propres propriétés et relations. Permet une analyse détaillée au niveau de l’objet.
* **Choisir judicieusement** sélectionnez le schéma le plus simple qui répond à vos besoins, mais utilisez des tableaux et des objets pour les scénarios avancés nécessitant la conservation des relations.