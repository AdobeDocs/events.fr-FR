---
title: Bonnes pratiques relatives à la migration d’Adobe Analytics vers Adobe Customer Journey Analytics
description: Découvrez les étapes essentielles et les bonnes pratiques pour migrer d’Adobe Analytics vers Customer Journey Analytics (CJA), notamment la conception de schémas XDM, le mappage de données et la configuration des vues de données.
solution: Analytics, Customer Journey Analytics
topic: Migration
role: Developer
level: Beginner, Intermediate
doc-type: Event
duration: 3654
last-substantial-update: 2025-07-16T00:00:00Z
jira: KT-18535
source-git-commit: 90eb4a9d2cf445c58fde776092fb047f820fa207
workflow-type: tm+mt
source-wordcount: '298'
ht-degree: 0%

---


# Bonnes pratiques relatives à la migration d’Adobe Analytics vers Adobe Customer Journey Analytics

Découvrez la migration d’Adobe Analytics vers Customer Journey Analytics (CJA). Organisée par Nicolina Picone et Maurizio Corò de l&#39;équipe d&#39;Adobe Ultimate Success, cette session offre un aperçu détaillé de CJA, de ses fonctionnalités et des bonnes pratiques en matière de migration.

## Sujets clés abordés

* différences entre Analytics et CJA
* l’importance d’identifiants d’identité fiables, de l’alignement des structures de données et de la création de vues de données personnalisables
* couvre les stratégies d’importation de données historiques, de gestion de l’attribution des canaux marketing et d’utilisation de la flexibilité de CJA pour un reporting personnalisé

>[!VIDEO](https://video.tv.adobe.com/v/3464911/?learn=on&enablevpops)

## Points clés à retenir

* **Présentation de Customer Journey Analytics (CJA)** CJA est une évolution d’Adobe Analytics, qui se concentre sur le parcours client complet sur plusieurs points de contact (par exemple, mobile, web, CRM, centres d’appels) plutôt que sur des événements à suivi unique. Il permet le traitement et la manipulation des données en temps réel.

* **Préparation à la migration** Les étapes clés de la migration d’Adobe Analytics vers CJA comprennent la garantie d’un identifiant d’identité fort (par exemple, l’ID de personne), l’alignement des variables et des dimensions, et le mappage des données au schéma XDM. Les données historiques peuvent être importées avec des étapes de validation.

* **Vues de données et flexibilité** CJA permet de créer des vues de données personnalisables avec des durées de session ajustables, des filtres de segmentation et des paramètres d’attribution. Cette flexibilité permet des rapports et des analyses personnalisés.

* **Bonnes pratiques relatives à la migration des données historiques** validez les données CJA en les comparant à celles d’Adobe Analytics dans une plage acceptable (par exemple, une différence de 10 %). Commencez par une courte fenêtre de renvoi (par exemple, un mois) et augmentez progressivement.

* **Attribution du canal marketing** CJA offre des fonctionnalités améliorées pour l’attribution du canal marketing, en éliminant des limitations telles que la fonction « Première page de la visite » et en activant des configurations de session plus dynamiques.
