---
title: Configuration du réseau CDN et de WAF dans Adobe Experience Manager as a Cloud Service
description: Améliorez les performances et la sécurité des applications Adobe Experience Manager as a Cloud Service avec des règles de réseau CDN personnalisables, la protection WAF et le pipeline de configuration, tels qu’ils sont partagés par les experts Adobe.
solution: Experience Manager as a Cloud Service
feature: Security
topic: Performance, Security
role: Developer
level: Beginner, Intermediate
doc-type: Event
duration: 2211
last-substantial-update: 2024-11-26T00:00:00Z
jira: KT-16574
exl-id: a9f38e79-c707-443d-8b2f-e534ce4dd43d
source-git-commit: 91f20c3e9ee5ae5b259d5cb3da476974acdc6585
workflow-type: tm+mt
source-wordcount: '366'
ht-degree: 0%

---

# Configuration du réseau CDN et de WAF dans Adobe Experience Manager as a Cloud Service

Libérez tout le potentiel du réseau CDN géré par Adobe avec des règles CDN personnalisables, la protection WAF et le pipeline de configuration. Marius Petria, informaticien principal chez Adobe, Quentin Vecchio, ingénieur en développement logiciel chez Adobe et Florian Froese, ingénieur en développement logiciel chez Adobe, partagent des stratégies pour améliorer les performances et la sécurité des applications Adobe Experience Manager as a Cloud Service.

>[!VIDEO](https://video.tv.adobe.com/v/3440401/?learn=on&enablevpops)

## Discussion Communautaire

Poursuivez la conversation dans la communauté Adobe Developers Live [discussion](https://adobe.ly/3O0TyYa).

## Points clés

* **Introduction de nouvelles fonctionnalités de configuration** La présentation introduit de nouvelles fonctionnalités de configuration pour le réseau CDN dans un service cloud, en se concentrant sur la capacité à configurer le réseau CDN pour divers cas d’utilisation.
* **Options de configuration du réseau CDN** Les nouvelles options permettent une interaction avec les requêtes et les réponses HTTP, comme l’ajout ou la suppression d’en-têtes, la réécriture des chemins de requête, le blocage du trafic, la redirection des clients et la création d’un proxy vers différentes origines.
* **Améliorations de la sécurité** Les nouvelles fonctionnalités incluent des règles de filtrage du trafic pour bloquer ou consigner le trafic en fonction des modèles de requête, et l’introduction de WAF M pour une protection avancée contre les attaques web telles que l’injection SQL et XSS.
* **Configuration déclarative** La configuration est effectuée à l’aide de fichiers YAML et déployée via un pipeline de configuration dans Cloud Manager, ce qui en fait un processus rapide et simple.
* **Transformations de requête et de réponse** les nouvelles fonctionnalités permettent des transformations de requête pour normaliser les URL et supprimer les paramètres de requête inutiles, ainsi que des transformations de réponse pour définir des en-têtes avant d’envoyer des réponses aux clients.
* **Filtres de trafic et limitation de débit** les filtres de trafic peuvent bloquer des adresses IP ou des pays spécifiques et implémenter la limitation de débit pour se protéger contre les attaques DDoS. La limitation de débit peut être configurée en fonction de divers critères tels que l’adresse IP du client, l’agent utilisateur et le chemin d’accès de la requête.
* **Outils de surveillance et d’analyse** Adobe fournit des outils tels que les tableaux de bord Elasticsearch/Kibana et Splunk pour analyser le trafic et l’utilisation, ce qui permet d’identifier et d’atténuer les menaces de sécurité potentielles.
* **Démonstration pratique** la présentation comprend une démonstration montrant comment déployer des configurations de réseau CDN à l’aide de Cloud Manager et comment gérer les erreurs et valider les configurations localement à l’aide d’AEM.
