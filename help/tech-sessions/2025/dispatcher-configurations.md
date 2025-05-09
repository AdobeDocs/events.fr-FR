---
title: Configurations de Dispatcher dans Adobe Experience Manager as a Cloud Service
description: Découvrez les bonnes pratiques d’AEM Dispatcher en matière de mise en cache, de sécurité et de performances afin d’optimiser l’évolutivité et l’efficacité d’AEM as a Cloud Service.
solution: Experience Manager as a Cloud Service
version: Experience Manager as a Cloud Service
feature: Dispatcher
role: Developer, Leader, User
level: Beginner, Intermediate, Experienced
doc-type: Event
duration: 4200
last-substantial-update: 2025-05-07T00:00:00Z
jira: KT-17903
source-git-commit: cfc7b54ae4360779ca2c41f88fc08089bae99165
workflow-type: tm+mt
source-wordcount: '339'
ht-degree: 0%

---


# Sessions techniques : configurations Dispatcher dans Adobe Experience Manager as a Cloud Service

**Adobe Experience Manager (AEM) as a Cloud Service** offre évolutivité, flexibilité et performances améliorées pour les plateformes d’expérience digitale modernes. Le **Dispatcher AEM** est au cœur de cette architecture. Il s’agit d’un composant essentiel responsable de la mise en cache, de la sécurité et de la gestion des requêtes. Lorsqu’il est correctement configuré, le Dispatcher accélère la diffusion du contenu, protège les systèmes principaux et améliore les performances globales du site.

Cette présentation met en évidence les paramètres Dispatcher clés, notamment les stratégies de mise en cache, les mécanismes de contrôle d’accès et le filtrage des demandes. Il présente également les bonnes pratiques pour maintenir un déploiement d’AEM sécurisé et hautement performant dans le cloud. Que vous soyez développeur, architecte ou décideur d’entreprise, une bonne compréhension des configurations Dispatcher est essentielle pour libérer tout le potentiel d’AEM as a Cloud Service.

>[!VIDEO](https://video.tv.adobe.com/v/3457891/?learn=on&enablevpops)

## Points clés

* **Dispatcher SDK pour la validation** AEM Dispatcher SDK est un outil puissant d’analyse statique des configurations. Il permet une validation rapide des configurations, vérifie l’immuabilité et identifie les erreurs, ce qui représente un gain de temps significatif par rapport aux déploiements complets des pipelines.

* **Environnement de développement rapide (RDE)** le RDE fournit un environnement d’exécution interactif pour tester et déboguer des configurations au-delà de l’analyse statique. Il permet une validation et un débogage plus rapides, ce qui réduit le temps nécessaire au déploiement et aux tests.

* **Mise en réseau avancée avec proxy Mod** Des configurations de mise en réseau avancées, telles que des adresses IP de sortie dédiées et VPN, peuvent être configurées à l’aide de Cloud Manager. Le module proxy mod permet de décharger des transactions d’AEM vers des services externes, d’optimiser les performances et de réduire la charge sur la JVM .

* **Bonnes pratiques relatives aux configurations Dispatcher** Les principales recommandations incluent l’utilisation de chemins relatifs, d’en-têtes x-vhost uniques et d’en-têtes client appropriés, ainsi que l’utilisation d’en-têtes de contrôle du cache pour gérer efficacement la mise en cache. Ces pratiques permettent d’éviter les échecs de pipeline et d’améliorer l’efficacité du débogage.

* **Pipeline de couche web pour le déploiement** Le pipeline de couche web est un utilitaire pour le déploiement de configurations Dispatcher isolées. Elle comprend des tests supplémentaires tels que l’invalidation du cache, qui permettent de s’assurer que les mises à jour du contenu sont répercutées rapidement et précisément dans les environnements de production.