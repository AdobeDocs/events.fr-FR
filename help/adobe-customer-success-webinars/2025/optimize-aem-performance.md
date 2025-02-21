---
title: Optimisation des performances d’AEM - Stratégies et techniques de mise en cache
description: La session a couvert les stratégies et techniques de mise en cache, les mécanismes et les niveaux de mise en cache, la gestion dynamique du contenu, les problèmes de mise en cache de débogage et la synchronisation de l’invalidation du cache entre le Dispatcher et le réseau CDN.
topic: Performance
role: Admin, Developer, Leader, User
level: Intermediate
doc-type: Event
duration: 3764
last-substantial-update: 2025-02-21T00:00:00Z
jira: KT-17373
source-git-commit: e7bf8b79ad4920b303fc3afbdfb4adee60614c88
workflow-type: tm+mt
source-wordcount: '277'
ht-degree: 0%

---


# Optimisation des performances d’AEM : stratégies et techniques de mise en cache

Au cours de cette session, nous allons explorer divers mécanismes de mise en cache, tels que la mise en cache de pages, de ressources et de Dispatcher, ainsi que la manière d’implémenter la mise en cache au niveau du réseau CDN pour optimiser la diffusion du contenu et réduire les temps de chargement. La discussion portera sur les bonnes pratiques pour chaque couche de mise en cache, la résolution des problèmes courants et la manière d’exploiter les fonctionnalités du réseau CDN pour une efficacité maximale.

## Points clés de la discussion

* Présentation de la mise en cache
* Types de mise en cache, Bonnes pratiques de mise en cache, invalidation et actualisation du cache
* Techniques de débogage

>[!VIDEO](https://video.tv.adobe.com/v/3444452/?learn=on&enablevpops)

## Principaux points à retenir

* **Stratégies et techniques de mise en cache** La session a porté sur diverses stratégies et techniques de mise en cache visant à optimiser les performances, notamment la mise en cache au niveau de différents niveaux tels que le navigateur, le réseau CDN et le Dispatcher.

* **Mécanismes et niveaux de mise en cache** La discussion a porté sur différents mécanismes et niveaux de mise en cache, notamment la mise en cache du navigateur, la mise en cache CDN et la mise en cache du Dispatcher, ainsi que sur la manière dont ils peuvent être configurés et gérés.

* **Gestion de contenu dynamique** Les techniques de gestion du contenu dynamique sur une page ont été abordées, y compris l’utilisation de Sling Dynamic Include (SDI) et des inclusions côté Edge (ESI) pour s’assurer que le contenu dynamique n’est pas mis en cache lorsque le contenu statique l’est.

* **Problèmes de mise en cache de débogage** diverses techniques pour déboguer les problèmes de mise en cache à différents niveaux (navigateur, réseau CDN, dispatcher) ont été expliquées, y compris l’utilisation des en-têtes, des journaux et des configurations spécifiques pour identifier et résoudre les problèmes de mise en cache.

* **Synchronisation de l’invalidation du cache** La session a abordé le défi de synchroniser l’invalidation du cache entre le Dispatcher et le réseau CDN, en recommandant l’utilisation de valeurs d’âge maximal plus courtes et d’API de purge du réseau CDN pour s’assurer que les deux caches sont invalidés simultanément lors de l’activation de la page.