---
title: Optimiser la diffusion de contenu - Tirer parti de la puissance des services Edge
description: La session sur Edge Delivery Services (EDS) a porté sur son architecture, son intégration à la création basée sur des documents et sur AEM, la création rapide de sites, les options de personnalisation et les bonnes pratiques pour maintenir des performances élevées.
solution: Experience Manager, Experience Manager as a Cloud Service
feature: Edge Delivery Services
role: Admin, Developer, Leader, User
level: Intermediate
doc-type: Event
duration: 3589
last-substantial-update: 2024-12-06T00:00:00Z
jira: KT-16631
exl-id: 2057e491-9ec3-4bfe-b85a-6b74d70822bf
source-git-commit: 32060a6a0d2cc24b8dc09c8f5e9f9d9c679e6d3e
workflow-type: tm+mt
source-wordcount: '406'
ht-degree: 0%

---

# Optimiser la diffusion de contenu : tirer parti de la puissance des services Edge

Au cours de cette session, nous vous donnerons un aperçu de Edge Delivery Services (EDS) et de son architecture. Nous allons examiner comment EDS s’intègre à la création basée sur des documents et à la création basée sur AEM via l’éditeur universel. Une démonstration en direct présentera EDS en action, suivie de ressources pour une exploration plus approfondie et d’une session de questions/réponses.

>[!VIDEO](https://video.tv.adobe.com/v/3440938/?learn=on&enablevpops)

## Principaux points à retenir

### Présentation d’EDS

* EDS est un ensemble de services composables conçus pour améliorer les capacités d’ATM. &#x200B;
* Il vise à offrir des expériences exceptionnelles qui stimulent l’engagement et les conversions avec des cycles de développement rapides et un score phare de 100 %. &#x200B;

### Options de création

* **Création basée sur les documents** Utilise des outils familiers tels que Microsoft Word ou Google Docs pour la création de contenu, ce qui permet de créer rapidement du contenu sans formation approfondie. &#x200B;
* **Éditeur universel** fournit une interface WYSIWYG similaire aux sites ATM traditionnels, ce qui permet de créer du contenu plus détaillé et visuel. &#x200B;

### Architecture

* EDS s’intègre au framework Amazon Cloud Service. &#x200B;
* Il prend en charge l’implémentation sans serveur et peut fonctionner sans instance d’auteur ou d’éditeur traditionnelle. &#x200B;
* Deux niveaux de mise en cache peuvent être implémentés : au niveau de l’infrastructure client et au niveau du service de développement. &#x200B;

### Gestion de contenu

* La création basée sur des documents nécessite un compte GitHub, Google Drive ou Microsoft SharePoint, un plug-in Sidekick et un outil de synchronisation de code. &#x200B;
* EDS avec création IAM nécessite un compte GitHub, une licence IAM as a Cloud Service et un outil de synchronisation de code.

### Développement et déploiement

* Le processus de création d’un site avec EDS est rapide et prend souvent moins d’une journée. &#x200B;
* Le développement local peut être effectué à l’aide de la commande aem up pour créer une version locale du site web.
* Les modifications peuvent être validées dans les branches de fonctionnalités à des fins de test avant de fusionner dans la branche principale. &#x200B;

### Personnalisation et extensibilité

* Les composants personnalisés peuvent être créés à l’aide de CSS et JavaScript simples. &#x200B;
* L’architecture permet des intégrations tierces et des sources de création personnalisées.

### Bonnes pratiques

* Il est recommandé d’utiliser le JavaScript vanille et le CSS pour conserver des scores lighthouse élevés.
* Toute introduction de bibliothèques telles que React doit être soigneusement étudiée et testée afin d’éviter une dégradation des performances.

### Assistance et documentation

* Une documentation complète est disponible pour guider les utilisateurs et utilisatrices tout au long du processus de configuration et de personnalisation. &#x200B;
* Nous recommandons aux utilisateurs de contacter l’assistance Adobe pour tout problème non résolu. &#x200B;
