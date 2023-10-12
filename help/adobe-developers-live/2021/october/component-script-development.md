---
title: Bonnes pratiques pour le développement et le déploiement des scripts de composant dans Experience Manager as a Cloud Service
description: Cette session décrit les bonnes pratiques les plus récentes que les développeurs Adobe Experience Manager peuvent appliquer afin d’avoir des déploiements d’applications plus prévisibles. Introduit en tant que fonctionnalité Apache Sling en 2019 et utilisé dans AEMaaCS depuis 2020, les scripts précompilés offrent aux développeurs deux améliorations majeures par rapport à la méthode classique de déploiement des composants Adobe Experience Manager - 1. les scripts peuvent être versionnés et comporter des chaînes de dépendances explicites, comme toute API Java 2. la compilation du script peut désormais être effectuée pendant le processus de création de l’application, ce qui permet de détecter rapidement les erreurs potentielles (dépendances manquantes, utilisation incorrecte de l’API, etc.) Nous nous concentrerons sur la manière dont les développeurs peuvent configurer leurs projets pour fournir leurs scripts sous la forme de lots précompilés et utiliser les analyseurs de fonctionnalités Sling Adobe Experience Manager locaux pour vérifier que les exigences de l’API sont satisfaites, les aidant à détecter rapidement toute erreur potentielle.
solution: Experience Manager
feature: Developer Tools
topic: Development
role: Developer, Architect
level: Beginner, Intermediate, Experienced
version: Cloud Service
kt: 9177
type: Event
exl-id: 71fa0d10-cea5-416e-a6e5-2c729c7793a6
source-git-commit: 1792dc318643aec2c12613f621361d72a7a918b1
workflow-type: tm+mt
source-wordcount: '341'
ht-degree: 10%

---

# Bonnes pratiques pour le développement et le déploiement des scripts de composant dans Experience Manager as a Cloud Service

Cette session décrit les bonnes pratiques les plus récentes que les développeurs Adobe Experience Manager peuvent appliquer afin d’avoir des déploiements d’applications plus prévisibles. Introduit en tant que fonctionnalité Apache Sling en 2019 et utilisé dans AEMaaCS depuis 2020, les scripts précompilés offrent aux développeurs deux améliorations majeures par rapport à la méthode classique de déploiement des composants Adobe Experience Manager : 1. les scripts peuvent être versionnés et comporter des chaînes de dépendances explicites, comme toute API Java 2. la compilation du script peut désormais être effectuée pendant le processus de création de l’application, ce qui permet de détecter rapidement les erreurs potentielles (dépendances manquantes, utilisation incorrecte de l’API, etc.) Nous nous concentrerons sur la manière dont les développeurs peuvent configurer leurs projets pour fournir leurs scripts sous la forme de lots précompilés et utiliser les analyseurs de fonctionnalités Sling Adobe Experience Manager locaux pour vérifier que les exigences de l’API sont satisfaites, les aidant à détecter rapidement toute erreur potentielle.

Poursuivez la conversation dans **[Communautés d’Experience League](https://adobe.ly/3zJrS0f)**.

>[!VIDEO](https://video.tv.adobe.com/v/337851/?quality=12&learn=on&hidetitle=true)

## Ressources supplémentaires

- [Documentation Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform.html?lang=fr)
- [Présentation d’Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/landing/home.html?lang=fr)
- [Tutoriels Adobe Experience Platform](https://experienceleague.adobe.com/docs/platform-learn/tutorials/overview.html?lang=fr)
