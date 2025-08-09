---
title: Maîtriser Dynamic Media avec l’API ouverte
description: Comprenez les principales différences entre Dynamic Media traditionnel et le modèle d’API ouverte et apprenez à réussir la transition et l’implémentation de Dynamic Media Ultimate avec l’API ouverte.
solution: Experience Manager as a Cloud Service, Experience Manager Assets
feature-set: Experience Manager Assets
feature: SDK/API
topic: Development, Content Management
role: Admin, Developer, User
level: Beginner, Intermediate
doc-type: Event
duration: 2757
last-substantial-update: 2025-08-08T00:00:00Z
jira: KT-18702
source-git-commit: ef1eacd73c5a4fb9cdfee730d40606ec65bab2a7
workflow-type: tm+mt
source-wordcount: '249'
ht-degree: 3%

---


# Maîtriser Dynamic Media avec l’API ouverte

Ce webinaire est destiné aux professionnels qui connaissent bien Dynamic Media traditionnel et qui cherchent à comprendre et à implémenter [Dynamic Media Ultimate](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dm-prime-ultimate) avec l’API Open.  Nous allons explorer le fonctionnement de haut niveau de Dynamic Media Ultimate avec l’API ouverte et le comparer à Dynamic Media traditionnel. Notre objectif est de fournir une compréhension complète des différences entre ces deux approches, ce qui permet aux participants qui connaissent Dynamic Media de s’adapter facilement au modèle d’API ouverte.

>[!VIDEO](https://video.tv.adobe.com/v/3470620/?learn=on&enablevpops)

## Comparaison des fonctionnalités clés

| Fonctionnalité | Dynamic Media | Dynamic Media avec OpenAPI |
|-----------------------------|------------------------|----------------------------|
| *Disponibilité* | On-premise, AMS, Cloud | Cloud uniquement |
| *Modificateurs* | Ensemble riche disponible | Limité mais en croissance |
| *Contrôle d’accès* | Ouvert à tous les utilisateurs | Restreint par les rôles |
| *TTL CDN* | ~10 heures | ~10 minutes |
| *Application des approbations* | Publication automatique | Approbation requise |
| *Optimisation pour les moteurs de recherche* | Oui | Oui |

## Scénarios d’intégration

Ces scénarios d’intégration démontrent la flexibilité et l’évolutivité de Dynamic Media avec OpenAPI pour répondre aux divers besoins des entreprises.

* **Intégration d’AEM Sites** Dynamic Media avec OpenAPI prend en charge une intégration transparente à AEM Sites, ce qui permet d’extraire des ressources directement à partir du niveau de diffusion sans duplication.
* **CMS tiers** Permet l’intégration à des plateformes telles que Salesforce et Drupal à l’aide d’API ou de micro applications front-end.
* **Accès piloté par les API** fournit des API pour la recherche, la récupération et la diffusion de rendus optimisés des ressources.
* **Optimisation du niveau de diffusion** Assets est diffusé via Fastly, ce qui accélère et rend la diffusion plus efficace.