---
title: Efficacité d’AEM Sites - Optimisation des performances, configuration et dépannage
description: 'Principes de base de la résolution des problèmes liés aux sites Adobe Experience Manager (AEM). Que vous rencontriez des problèmes de performances ou que vous ayez affaire à des configurations complexes, cette session vous apportera des compétences pratiques pour gérer et optimiser votre environnement AEM. Nous donnerons la priorité aux démonstrations en direct plutôt qu’aux diapositives, offrant ainsi une expérience pratique pour relever les défis du monde réel. ​Points de discussion clés : - Configuration de l’hôte virtuel et mappage des domaines - Problèmes de performances - Autorisation, identification, autorisations utilisateur'
solution: Experience Manager
version: Cloud Service
role: Admin, Developer, Leader, User
level: Intermediate
doc-type: Event
duration: 3452
last-substantial-update: 2024-10-30T00:00:00Z
jira: KT-16353
source-git-commit: 3f245f71cd4db5097b5a9e712114112451d899e4
workflow-type: tm+mt
source-wordcount: '268'
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