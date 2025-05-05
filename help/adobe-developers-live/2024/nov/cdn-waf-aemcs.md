---
title: Configuration du réseau de diffusion de contenu et de WAF dans Adobe Experience Manager as a Cloud Service
description: Améliorez les performances et la sécurité des applications Adobe Experience Manager as a Cloud Service grâce à des règles CDN personnalisables, à la protection WAF et au pipeline de configuration, comme le partagent les experts en Adobe.
feature: Security
topic: Performance, Security
role: Developer
level: Beginner, Intermediate
doc-type: Event
duration: 2211
last-substantial-update: 2024-11-26T00:00:00Z
jira: KT-16574
exl-id: a9f38e79-c707-443d-8b2f-e534ce4dd43d
source-git-commit: 946d7cd484e8c5d4358d4099b3518705cab8d4a3
workflow-type: tm+mt
source-wordcount: '366'
ht-degree: 0%

---

# Configuration du réseau de diffusion de contenu et de WAF dans Adobe Experience Manager as a Cloud Service

Déverrouillez tout le potentiel du réseau de diffusion de contenu géré par Adobe avec des règles de réseau de diffusion de contenu personnalisables, la protection WAF et le pipeline de configuration. Marius Petria, ingénieur informaticien Adobe, Quentin Vecchio, ingénieur du développement logiciel à l&#39;Adobe, et Florian Froese, ingénieur du développement logiciel à l&#39;Adobe, partagent des stratégies pour améliorer les performances et la sécurité des applications Adobe Experience Manager as a Cloud Service.

>[!VIDEO](https://video.tv.adobe.com/v/3440604/?learn=on&enablevpops&captions=fre_fr)

## Discussions communautaires

Poursuivez la conversation dans la communauté Adobe Developers Live [discussion](https://adobe.ly/3O0TyYa).

## Points clés

* **Introduction de nouvelles fonctionnalités de configuration** La présentation introduit de nouvelles fonctionnalités de configuration pour le CDN dans un service cloud, en mettant l’accent sur la possibilité de configurer le CDN pour divers cas d’utilisation.
* **Options de configuration du réseau de diffusion de contenu** Les nouvelles options permettent d’interagir avec les requêtes et réponses HTTP, telles que l’ajout/la suppression d’en-têtes, la réécriture des chemins de requête, le blocage du trafic, la redirection des clients et le proxy vers différentes origines.
* **Améliorations de la sécurité** Les nouvelles fonctionnalités incluent des règles de filtrage du trafic pour bloquer ou consigner le trafic en fonction des modèles de demande, ainsi que l’introduction de M WAF pour une protection avancée contre les attaques Web telles que l’injection SQL et XSS.
* **Configuration déclarative** La configuration est effectuée à l’aide de fichiers YAML et déployée via un pipeline de configuration dans Cloud Manager, ce qui en fait un processus rapide et simple.
* **Transformations de requêtes et de réponses** Les nouvelles fonctionnalités permettent des transformations de requêtes pour normaliser les URL et supprimer les paramètres de requête inutiles, ainsi que des transformations de réponses pour définir des en-têtes avant d’envoyer des réponses aux clients.
* **Filtres de trafic et Limitation de débit** Les filtres de trafic peuvent bloquer des adresses IP ou des pays spécifiques et mettre en oeuvre une limitation de débit pour se protéger des attaques DDoS. La limitation de débit peut être configurée en fonction de différents critères tels que l’adresse IP du client, l’agent utilisateur et le chemin de requête.
* L’Adobe **Outils de surveillance et d’analyse** fournit des outils tels que les tableaux de bord Elasticsearch/Kibana et Splunk pour analyser le trafic et l’utilisation, ce qui permet d’identifier et d’atténuer les menaces potentielles pour la sécurité.
* **Démo pratique** La présentation comprend une démonstration montrant comment déployer des configurations CDN à l’aide de Cloud Manager et comment gérer les erreurs et valider les configurations localement à l’aide d’AEM.
