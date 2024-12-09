---
title: Optimisation de la diffusion de contenu - Déverrouillage de la puissance des services Edge
description: ATM Edge Delivery Services (EDS) améliore les fonctionnalités d’ATM avec des services composables, des cycles de développement rapides et de hauts scores Lighthouse, en prenant en charge la création basée sur les documents et WYSIWYG, l’architecture sans serveur, la création rapide de sites et des options de personnalisation étendues.
solution: Experience Manager, Experience Manager as a Cloud Service
feature: Edge Delivery Services
role: Admin, Developer, Leader, User
level: Intermediate
doc-type: Event
duration: 3589
last-substantial-update: 2024-12-06T00:00:00Z
jira: KT-16631
source-git-commit: 47ae42d06ed311e60ebce194e0683bb95e8e5b69
workflow-type: tm+mt
source-wordcount: '410'
ht-degree: 0%

---


# Optimisation de la diffusion de contenu : déverrouillage de la puissance des services Edge

Au cours de cette session, nous vous proposons un aperçu des Edge Delivery Services (EDS) et de leur architecture. Nous allons découvrir comment EDS s’intègre à la création basée sur les documents et à la création basée sur les AEM via l’éditeur universel. Une démonstration en direct présentera le SDK en action, suivie de ressources pour une exploration plus approfondie et d’une session de questions-réponses.

>[!VIDEO](https://video.tv.adobe.com/v/3440938/?learn=on&enablevpops)

## Principales acquisitions

### Présentation d’EDS

* EDS est un ensemble de services composables conçus pour améliorer les capacités d&#39;ATM. &#x200B;
* Il vise à offrir des expériences exceptionnelles qui favorisent l’engagement et les conversions avec des cycles de développement rapides et un score de phare de 100 %. &#x200B;

### Options de création

* **Création basée sur des documents** utilise des outils familiers tels que Microsoft Word ou Google Docs pour la création de contenu, ce qui permet la création rapide de contenu sans formation approfondie. &#x200B;
* **Éditeur universel** Fournit une interface WYSIWYG similaire aux sites d’ATM traditionnels, ce qui permet une création de contenu plus détaillée et visuelle. &#x200B;

### Architecture

* EDS s’intègre dans la structure du Cloud Service Amazon. &#x200B;
* Il prend en charge l’implémentation sans serveur et peut fonctionner sans instance d’auteur ou d’éditeur traditionnelle. &#x200B;
* Deux niveaux de mise en cache peuvent être implémentés : au niveau de l’infrastructure client et au niveau EDS. &#x200B;

### Gestion de contenu

* La création basée sur les documents nécessite un compte GitHub, Google Drive ou Microsoft SharePoint, un module externe sidekick et un outil de synchronisation de code. &#x200B;
* EDS avec création IAM nécessite un compte GitHub, une licence de service cloud IAM et un outil de synchronisation de code.

### Développement et déploiement

* Le processus de création d’un site avec EDS est rapide et prend souvent moins d’une journée. &#x200B;
* Le développement local peut être réalisé à l’aide de la commande aem up pour créer une version locale du site web.
* Les modifications peuvent être validées dans les branches de fonctionnalités pour les tests avant de fusionner dans la branche principale. &#x200B;

### Personnalisation et extension

* Les composants personnalisés peuvent être créés à l’aide de CSS et JavaScript simples. &#x200B;
* L’architecture permet des intégrations tierces et des sources de création personnalisées.

### Bonnes pratiques

* Il est recommandé d’utiliser vanilla JavaScript et CSS pour gérer les scores élevés de Lighthouse.
* Toute introduction de bibliothèques comme React doit être soigneusement étudiée et testée afin d’éviter une dégradation des performances.

### Assistance et documentation

* Une documentation complète est disponible pour guider les utilisateurs tout au long du processus de configuration et de personnalisation. &#x200B;
* Les utilisateurs sont encouragés à contacter pour Adobe la prise en charge de tout problème non résolu. &#x200B;