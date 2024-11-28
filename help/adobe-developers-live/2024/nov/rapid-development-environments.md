---
title: Environnements de développement rapide Adobe Experience Manager
description: Facilitez le développement et le déploiement rapides dans les environnements cloud avec le nouveau SDK d’Adobe, en réduisant considérablement le temps de déploiement et en prenant en charge les mises à jour rapides, les journaux en direct et les options de configuration avancées, comme expliqué dans DevOps Life 2024.
feature: Developer Tools
topic: Development
role: Developer
level: Beginner, Intermediate
doc-type: Event
duration: 2427
last-substantial-update: 2024-11-27T00:00:00Z
jira: KT-16570
source-git-commit: 07d4174b0d89ba2c417866e76ae72f015b91b03a
workflow-type: tm+mt
source-wordcount: '337'
ht-degree: 0%

---


# Environnements de développement rapide Adobe Experience Manager

Découvrez les bonnes pratiques pour les environnements de développement rapide (RDE) et la console de développement mise à jour. Natalia Angulo Herrera, ingénieur de développement logiciel chez Adobe, et Remo Liechtenstein, ingénieur de développement logiciel chez Adobe, couvrent les défis de migration, la configuration de l’interface de ligne de commande AIO, le déploiement, les tests, la journalisation et la gestion de la configuration pour un workflow Adobe Experience Manager plus fluide.

>[!VIDEO](https://video.tv.adobe.com/v/3440397/?learn=on&enablevpops)


## Discussions communautaires

Poursuivez la conversation dans la communauté Adobe Developers Live [discussion](https://adobe.ly/3UJluDo).

## Principales acquisitions

* **Présentation de DevOps Life 2024** La session est hébergée par Natalia et Remo de l’Adobe, se concentrant sur les environnements de développement rapide.
* **Problème d’énoncé** Le problème des environnements de développement locaux qui fonctionnent bien localement mais échouent lorsqu’ils sont déployés dans le cloud.
* **Solution** Création d’un nouveau SDK dans le cloud pour faciliter le développement et le déploiement rapides, ce qui réduit le temps de 30 minutes à quelques secondes ou quelques minutes.
* **Processus de déploiement** Le nouvel environnement permet des mises à jour et des validations rapides par le biais d’une nouvelle API et d’un nouveau module d’interface de ligne de commande, ce qui accélère le retour et le déploiement.
* **Différences d’infrastructure** L’environnement cloud utilise une instance de création et de publication unique sans haute disponibilité et n’utilise pas MongoDB.
* **Configuration et utilisation** Les développeurs peuvent configurer un environnement de développement rapide par le biais de l’interface de cloud, à l’aide de l’interface de ligne de commande npm et de l’Adobe IO pour l’installation et la configuration.
* **Commandes de base** Les commandes clés incluent io amd —help, io login, io status, io install, io history, io delete et io reset.
* **Journalisation et débogage** Le nouvel environnement prend en charge les journaux en direct et la modification des niveaux de journal sans redéploiement, à l’aide de commandes telles que io am ou d logs.
* **Rubriques avancées** Prise en charge des packages front-end et des pipelines de configuration, ce qui permet un déploiement et une itération rapides.
* **Fonctionnalités à venir** prévoit d’introduire des fonctionnalités d’instantané pour des réinitialisations plus simples de l’environnement et des mises à jour automatiques sans perte de contenu.
* **Questions et réponses et commentaires** La session encourage les participants à rejoindre le canal Discorde pour une interaction en direct et un retour avec l’équipe de développement.