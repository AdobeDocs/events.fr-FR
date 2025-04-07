---
title: Adobe Pass - nouvelle API REST v2
description: Cette session se concentre sur l’introduction de la nouvelle API REST v2 d’Adobe et sur le guidage des utilisateurs tout au long de son processus de migration.
role: Developer
level: Beginner, Intermediate, Experienced
doc-type: Technical Video
duration: 3230
last-substantial-update: 2025-04-07T00:00:00Z
jira: KT-17685
hidefromtoc: true
source-git-commit: 1082d67d49901e151115255b585799a5f57bda4a
workflow-type: tm+mt
source-wordcount: '243'
ht-degree: 0%

---


# Adobe Pass - nouvelle API REST v2

Cette session se concentre sur l’introduction de la nouvelle API REST v2 d’Adobe et sur le guidage des utilisateurs tout au long de son processus de migration.

>[!VIDEO](https://video.tv.adobe.com/v/3457461/?learn=on&enablevpops)

## Principaux points forts

* **Présentation et avantages**

   * L’API REST v2 est conçue pour une authentification moderne, flexible et évolutive, répondant aux événements à forte demande et aux scénarios multi-appareils.
   * Les principales améliorations comprennent un chiffrement amélioré, la cohérence de session, le SSO entre appareils et des informations d’erreur étendues pour un débogage plus rapide.

* **Étapes de migration**

   * Les utilisateurs doivent créer des applications enregistrées avec des portées API REST v2.
   * Les configurations existantes telles que l’identification d’appareil et les mappages MVPD peuvent être réutilisées.
   * La migration implique des phases telles que l’enregistrement, la configuration, l’authentification, la préautorisation et l’autorisation.

* **améliorations fonctionnelles**

   * L’API RESTful unifiée remplace les SDK Access Neighbour, ce qui simplifie l’implémentation entre les plateformes.
   * Prise en charge de plusieurs profils d’authentification au cours d’une même session et transitions transparentes entre appareils.
   * Les flux de pré-autorisation et d’autorisation restent obligatoires pour l’accès au contenu.

* **Planning**

   * L’API REST v1 cessera de recevoir des mises à jour en décembre 2025 et sera complètement retirée d’ici la fin de 2026.
   * Les utilisateurs sont encouragés à terminer la migration bien avant ces dates limites.

* **Ressources et assistance**

   * La documentation, les livres de cookie et les questions fréquentes sont disponibles sur Adobe Experience League.
   * Adobe propose des environnements sandbox, des tickets Zendesk et des réunions de migration pour l’assistance.

* **Faits Saillants Des Questions/Réponses**

   * L’API REST v2 nécessite une réauthentification, car elle n’est pas rétrocompatible avec la v1.
   * La préautorisation est nécessaire à l’interface utilisateur, tandis que l’autorisation est nécessaire pour les jetons de média.
   * La connexion unique est prise en charge via un nouveau jeton de service Adobe.

