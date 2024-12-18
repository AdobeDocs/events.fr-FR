---
title: Efficacité d’AEM Sites - Optimisation des performances, configuration et dépannage
description: Cette session aborde les principales compétences de dépannage de Adobe Experience Manager (AEM) Sites, en se concentrant sur des solutions pratiques pratiques pour les problèmes de performances, les configurations complexes et les autorisations d’utilisateur.
solution: Experience Manager
version: Cloud Service
role: Admin, Developer, Leader, User
level: Intermediate
doc-type: Event
duration: 3452
last-substantial-update: 2024-10-30T00:00:00Z
jira: KT-16353
exl-id: 55f7c1d8-7c2c-4392-894a-2aa9b3cc0e4a
source-git-commit: ef652eb09c33f11d69ec66f70013cd3e53537a95
workflow-type: tm+mt
source-wordcount: '235'
ht-degree: 0%

---

# Efficacité d’AEM Sites : optimisation des performances, configuration et dépannage

Dans ce webinaire, nous allons découvrir les principes de base de la résolution des problèmes liés aux sites Adobe Experience Manager (AEM). Que vous rencontriez des problèmes de performances ou que vous ayez affaire à des configurations complexes, cette session vous apportera des compétences pratiques pour gérer et optimiser votre environnement AEM. Nous donnerons la priorité aux démonstrations en direct plutôt qu’aux diapositives, offrant ainsi une expérience pratique pour relever les défis du monde réel. &#x200B;

>[!VIDEO](https://video.tv.adobe.com/v/3435114/?learn=on)

## Points clés

Le webinaire était axé sur l’efficacité du site AMP, notamment l’optimisation des performances, la configuration et la résolution des problèmes.

### Configuration Dispatcher

* Importance du dispatcher dans la diffusion de sites web performants.
* Principaux aspects de la configuration du Dispatcher : configuration de l’hôte virtuel, mappage de domaine avec structure du cache, rapports et redirections réguliers.

### Rights Management

* Bonnes pratiques : appliquez des droits aux groupes, évitez les instructions de refus et évitez les surmanipulations.
* Utilisation de l’outil ACL Netcentral pour gérer les droits via un fichier Yaml, ce qui facilite le déploiement et la traçabilité.

### Problèmes de performances

* Importance d’identifier les deltas dans les opérations de synchronisation pour éviter les purges complètes du cache.
* Évitez les opérations de page volumineuses pendant les heures de bureau.
* Simplifiez les workflows selon les étapes nécessaires.
* Soyez prudent avec les processus système tiers sur les systèmes de création, en particulier avec les outils tels que ImageMagick.
* Évitez les requêtes synchronisées sur des systèmes tiers qui ne peuvent pas gérer la charge.
* Gérez des composants personnalisés volumineux pour éviter une dégradation des performances.
* Surveillez les sessions longues pour éviter les exceptions de segment introuvables.
