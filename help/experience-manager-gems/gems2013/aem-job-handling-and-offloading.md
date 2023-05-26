---
title: Présentation de la gestion et du déchargement des tâches dans AEM 5.6.1.
description: Découvrez une présentation technique des fonctionnalités avancées de gestion des tâches. La gestion des tâches correspond à l’infrastructure sous-jacente de fonctionnalités telles que la réplication et le traitement des workflows. Découvrez le module de découverte ainsi que l’API améliorée de traitement des tâches, et les nouvelles fonctionnalités.
uuid: 181e3781-8eca-4a5d-879e-15ae4e1f6649
discoiquuid: ee4cd526-7363-4b8e-ad26-c2c937b70327
targetaudience: target-audience advanced
exl-id: 13888662-d1c5-4fff-b55e-38acede95396
source-git-commit: e401bf0b5ac1e7f06a4576e36887358bed352162
workflow-type: tm+mt
source-wordcount: '207'
ht-degree: 96%

---

# Présentation de la gestion et du déchargement des tâches dans AEM 5.6.1. {#introduction-of-job-handling-and-offloading-in-aem}

La gestion des tâches correspond à l’infrastructure sous-jacente de fonctionnalités telles que la réplication et le traitement des workflows. Cette section présente de manière technique les fonctionnalités avancées de gestion des tâches. Nous discuterons du nouveau module de découverte avec l’API améliorée de traitement des tâches et les nouvelles fonctionnalités. En s’appuyant sur la gestion et la découverte des tâches, la structure de déchargement se concentre sur la distribution des tâches entre les instances non clustérisées. Nous allons examiner de plus près la manière dont le déchargement optimise la gestion des tâches distribuées. Ensuite, nous examinerons comment il est utilisé pour l’implémentation actuelle du déchargement des workflows et comment l’utiliser dans son propre projet.

>[!VIDEO](https://video.tv.adobe.com/v/19580/?quality=9)

*Présenté le 24 juillet 2013*

**Présenté par :**

Carsten Ziegeler, développeur principal, Adobe

Marc Pfaff, développeur en chef, Adobe

Diapositives du présentateur – Partie 1

[Obtenir le fichier](assets/jobhandling.pdf)

Diapositives du présentateur – Partie 2

[Obtenir le fichier](assets/offloading.pdf)

## Liens connexes {#related-links}

* [Génération d’événements et gestion des tâches Apache Sling](https://sling.apache.org/documentation/bundles/apache-sling-eventing-and-job-handling.html)
* [API Discovery et ses implémentations](https://sling.apache.org/documentation/bundles/discovery-api-and-impl.html)
* [Tâches de déchargement](https://docs.adobe.com/docs/en/cq/current/deploying/offloading.html)
