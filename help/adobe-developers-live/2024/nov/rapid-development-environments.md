---
title: Environnements de développement rapide Adobe Experience Manager
description: Facilitez le développement et le déploiement rapides dans les environnements cloud avec Adobe New SDK, ce qui réduit considérablement le temps de déploiement et prend en charge les mises à jour rapides, les journaux en direct et les options de configuration avancées, comme expliqué dans la section DevOps Life 2024.
solution: Experience Manager as a Cloud Service, Experience Manager
feature: Developer Tools
topic: Development
role: Developer
level: Beginner, Intermediate
doc-type: Event
duration: 2427
last-substantial-update: 2024-11-27T00:00:00Z
jira: KT-16570
exl-id: 330d8be1-14a0-488a-aae0-ee90e1f7621e
source-git-commit: 91f20c3e9ee5ae5b259d5cb3da476974acdc6585
workflow-type: tm+mt
source-wordcount: '337'
ht-degree: 0%

---

# Environnements de développement rapide Adobe Experience Manager

Découvrez les bonnes pratiques relatives aux environnements de développement rapide (RDE) et à la Developer Console mise à jour. Natalia Angulo Herrera, ingénieure de développement logiciel chez Adobe, et Remo Liechti, ingénieure de développement logiciel chez Adobe, abordent les défis de la migration, la configuration, le déploiement, les tests, la journalisation et la gestion de la configuration de l’interface de ligne de commande AIO pour un workflow Adobe Experience Manager plus fluide.

>[!VIDEO](https://video.tv.adobe.com/v/3440397/?learn=on&enablevpops)


## Discussion Communautaire

Poursuivez la conversation dans la communauté Adobe Developers Live [discussion](https://adobe.ly/3UJluDo).

## Principaux points à retenir

* **Présentation de DevOps Life 2024** La session est organisée par Natalia et Remo d’Adobe, et se concentre sur les environnements de développement rapide.
* **Énoncé du problème** Défi des environnements de développement locaux qui fonctionnent bien localement, mais qui échouent lorsqu’ils sont déployés sur le cloud.
* **Solution** Création d’un nouveau SDK dans le cloud pour faciliter un développement et un déploiement rapides, en réduisant le temps de 30 minutes à quelques secondes ou quelques minutes.
* **Processus de déploiement** Le nouvel environnement permet des mises à jour et des validations rapides par le biais d’une nouvelle API et d’un nouveau plug-in de ligne de commande, ce qui accélère les retours et le déploiement.
* **Différences d’infrastructure** L’environnement cloud utilise une instance de création et de publication unique sans haute disponibilité et n’utilise pas MongoDB.
* **Installation et utilisation** Les développeurs peuvent configurer un environnement de développement rapide via l’interface cloud, à l’aide de npm et de l’interface de ligne de commande Adobe IO pour l’installation et la configuration.
* **Commandes de base** Les commandes clés incluent io amd —help, io login, io status, io install, io history, io delete et io reset.
* **Journalisation et débogage** Le nouvel environnement prend en charge les journaux dynamiques et la modification des niveaux de journal sans redéploiement, à l’aide de commandes telles que les journaux io am ou d.
* **Rubriques avancées** Prise en charge des packages front-end et des pipelines de configuration, permettant un déploiement et une itération rapides.
* **Fonctionnalités à venir** prévoit d’introduire la fonctionnalité d’instantané pour faciliter les réinitialisations d’environnement et les mises à jour automatiques sans perte de contenu.
* **Questions/réponses et commentaires** La session encourage les participants à rejoindre le canal Discord pour des interactions en direct et des commentaires avec l’équipe de développement.
