---
title: 'Efficacité d’AEM Sites : optimisation des performances, configuration et dépannage'
description: Le webinaire sur l’efficacité des sites AMP a porté sur l’optimisation des performances, la configuration du Dispatcher, les bonnes pratiques de gestion des droits et les stratégies permettant de résoudre les problèmes de performances.
solution: Experience Manager
version: Cloud Service
role: Admin, Developer, Leader, User
level: Intermediate
doc-type: Event
duration: 3452
last-substantial-update: 2024-10-30T00:00:00Z
jira: KT-16353
exl-id: 55f7c1d8-7c2c-4392-894a-2aa9b3cc0e4a
source-git-commit: 32060a6a0d2cc24b8dc09c8f5e9f9d9c679e6d3e
workflow-type: tm+mt
source-wordcount: '231'
ht-degree: 0%

---

# Efficacité d’AEM Sites : optimisation des performances, configuration et dépannage

Dans ce webinaire, nous aborderons les principes de base de la résolution des problèmes liés aux sites Adobe Experience Manager (AEM). Que vous rencontriez des problèmes de performances ou que vous ayez à gérer des configurations complexes, cette session vous apportera des compétences pratiques pour gérer et optimiser votre environnement AEM. Nous privilégierons les démonstrations en direct aux diapositives, offrant ainsi une expérience pratique pour relever les défis du monde réel&#x200B;

>[!VIDEO](https://video.tv.adobe.com/v/3435114/?learn=on)

## Points clés

Le webinaire portait sur l’efficacité du site AMP, notamment l’optimisation des performances, la configuration et le dépannage.

### Configuration de Dispatcher

* Importance du Dispatcher dans la diffusion de sites web performants.
* Aspects clés de la configuration du Dispatcher : configuration de l’hôte virtuel, mappage de domaine avec structure de cache et rapports et redirections réguliers.

### Rights Management

* Bonnes pratiques : appliquez des droits aux groupes, évitez les instructions de refus et évitez la suringénierie.
* Utilisation de l’outil Netcentric ACL pour gérer les droits par le biais d’un fichier Yaml, ce qui facilite le déploiement et la traçabilité.

### Problèmes de performances

* Importance de l’identification des deltas dans les opérations de synchronisation pour éviter les vidages complets du cache.
* Évitez les opérations de page volumineuses pendant les heures de bureau.
* Simplifiez les workflows aux étapes nécessaires.
* Soyez prudent avec les processus système tiers sur les systèmes de création, en particulier avec les outils tels qu’ImageMagick.
* Évitez les requêtes synchronisées avec des systèmes tiers qui ne peuvent pas gérer la charge.
* Gérez les composants personnalisés lourds pour éviter une dégradation des performances.
* Surveillez les sessions de longue durée pour empêcher les exceptions de segments introuvables.
