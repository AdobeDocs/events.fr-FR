---
title: Rationalisation des opérations de développement avec Cloud Manager
description: Optimisez les workflows de déploiement avec la nouvelle fonctionnalité "Bring Your Own Git" d’Adobe dans AMP Cloud Manager, ce qui permet l’intégration directe de référentiels Git externes, la prise en charge d’une stratégie de décalage à gauche pour les contrôles qualité du code anticipés et l’amélioration de l’efficacité et de l’adaptabilité.
solution: Experience Manager, Experience Manager Cloud Manager
feature: Git Repositories, CI-CD Pipeline
topic: Integrations
role: Developer
level: Beginner, Intermediate
doc-type: Event
duration: 1034
last-substantial-update: 2024-11-27T00:00:00Z
jira: KT-16547
source-git-commit: a5b6c2c3150fcc98686fe74d68f186bfe4e1befa
workflow-type: tm+mt
source-wordcount: '326'
ht-degree: 0%

---


# Rationalisation des opérations de développement avec Cloud Manager

Des pratiques d’opérations de développement efficaces sont essentielles pour fournir des expériences à grande échelle. Adrian Tanase, ingénieur en développement logiciel chez Adobe, explore comment Adobe Experience Manager Cloud Manager peut rationaliser les workflows de déploiement, améliorer l’automatisation et prendre en charge l’intégration et la diffusion continues (CI/CD).

>[!VIDEO](https://video.tv.adobe.com/v/3439904/?learn=on&enablevpops)

## Discussions communautaires

Poursuivez la conversation dans la communauté Adobe Developers Live [discussion](https://adobe.ly/3Ywf7Vm).

## Principales acquisitions

* **Introduction d’une nouvelle fonctionnalité** Adriana Clayton d’Adobe a introduit une nouvelle fonctionnalité dans AMP Cloud Manager appelée &quot;Apportez votre propre Git&quot;.
* **Objectif de la fonctionnalité** La fonctionnalité est conçue pour optimiser les workflows de déploiement, ce qui les rend plus rapides, plus efficaces et plus adaptables aux fournisseurs préférés.
* **Défis résolus** La fonctionnalité résout la complexité de la synchronisation de référentiels Git externes avec des référentiels Git Adobe, ce qui ajoute des étapes supplémentaires et du temps au processus de déploiement.
* **Solution fournie** &quot;Apportez votre propre Git&quot; permet la connexion directe de référentiels Git externes privés et publics aux pipelines Cloud Manager, ce qui permet la perception immédiate des modifications du code et l’exécution d’actions avant la fusion du code.
* **Stratégie de gauche de Maj** L’intégration prend en charge une stratégie de gauche de décalage, ce qui permet d’exécuter les contrôles de qualité du code plus tôt dans le processus de développement, ce qui permet aux développeurs de recevoir des commentaires opportuns.
* **Démo et validation** Une démonstration a été fournie pour montrer comment intégrer des référentiels et les valider à l’aide de Cloud Manager, y compris les étapes pour les référentiels GitHub et Bitbucket.
* **Impact sur les clients** Depuis sa disponibilité générale, plus de 130 clients ont intégré leurs référentiels, ce qui empêche plus de 2 500 demandes d’extraction avec des problèmes de qualité du code d’atteindre la production.
* **Améliorations futures** prévoit d’étendre la fonctionnalité afin d’inclure des rapports directement dans GitLab et Bitbucket, et d’étendre &quot;Bring Your Own Git&quot; aux services de diffusion Edge pour une plus grande flexibilité.
* **Encouragement pour les commentaires** Les clients sont encouragés à fournir des commentaires et à participer à la phase d’adoption précoce pour les référentiels non GitHub.
