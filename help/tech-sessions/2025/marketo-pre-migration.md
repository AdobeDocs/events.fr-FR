---
title: Migration de Marketo vers Adobe Admin Console - (pré-migration)
description: Adobe effectue une migration de Marketo Engage vers Admin Console pour une meilleure gestion des utilisateurs. Découvrez les types de migration automatique et automatique, les conditions préalables, les modifications après la migration, les bonnes pratiques, les pièges courants et l’assistance. Accédez à l’enregistrement de la session sur le site web Adobe Experience League.
role: Admin, Developer, Leader, User
level: Beginner, Intermediate, Experienced
doc-type: Event
duration: 2280
last-substantial-update: 2025-03-14T00:00:00Z
jira: KT-17483
exl-id: 9c3da83f-9e02-4a2e-9784-10213facf056
source-git-commit: 848fa8fee05b315361781059eabb3b19904c78c2
workflow-type: tm+mt
source-wordcount: '417'
ht-degree: 0%

---

# Migration de Marketo vers Adobe Admin Console - Pré-migration

Rejoignez-nous pour une migration transparente de Marketo avec des experts Adobe !

Anticipez votre migration Marketo avec l’équipe Expérience client et identité d’Adobe dans ce webinaire informatif. Nous vous guiderons à travers les étapes clés, les bonnes pratiques et les défis courants pour assurer une transition en douceur vers Adobe Admin Console.

Ce que vous apprendrez,

* Une feuille de route détaillée pour votre processus de pré-migration
* Bonnes pratiques pour simplifier votre transition et éviter les pièges
* Réponses d’experts aux problèmes de migration courants

Que vous débutiez votre migration ou que vous prépariez les étapes finales, cette session vous fournira les connaissances et les outils nécessaires pour naviguer en toute confiance dans le processus. Ne manquez pas cette occasion d’aller de l’avant et de rendre votre migration Marketo transparente !

>[!VIDEO](https://video.tv.adobe.com/v/3449712/?learn=on&enablevpops)

## Principaux points à retenir

### Objectif de la migration et présentation

Adobe effectue une migration de Marketo Engage vers Admin Console afin de consolider tous les produits dans un hub pour une meilleure gestion des utilisateurs et un meilleur accès.  Admin Console servira de hub central pour la gestion des produits Adobe, des rôles utilisateur, des autorisations et de l’accès à l’assistance. Les URL d’accès à Marketo Engage seront remplacées par la plateforme Adobe Experience Cloud.

### Types de migration

* **Migration automatique** pour les organisations comptant moins de 75 utilisateurs et ne disposant pas de configuration SSL. Adobe gère la migration.
* **Migration automatique** Pour les organisations disposant d’une configuration SSL. Les administrateurs gèrent le processus de migration à l’aide de la console de migration.

### Conditions préalables à la migration

* Les administrateurs système doivent remplir l’e-mail de consentement.
* SSL doit être configuré dans Admin Console (et non dans l’instance Marketo).

### Changements après la migration

* Les utilisateurs se connectent à l’aide d’Adobe ID ou d’un Federated ID (SSL).
* Les rôles d’administrateur et les autorisations déterminent les niveaux d’accès dans Admin Console.

### Bonnes pratiques

* vérifier les e-mails des utilisateurs et résoudre les comptes verrouillés avant la migration ;
* Assurez-vous que les rôles d’administrateur appropriés sont attribués.
* Désactivez les bloqueurs d’annonces publicitaires ou utilisez le mode navigation privée pour éviter les problèmes de connexion.

### Pièges courants

* Des autorisations d’administrateur incorrectes peuvent limiter l’accès.
* Les extensions de navigateur et les bloqueurs d’annonces publicitaires peuvent interférer avec l’accès.
* La liste blanche d’adresses IP n’est pas encore prise en charge dans Admin Console, mais elle est en cours de développement.

### Impact sur les fonctionnalités

* Les e-mails automatisés, les utilisateurs d’API et les codes munchkin ne seront pas affectés par la migration.
* La migration a principalement une incidence sur l’authentification et la gestion des utilisateurs.

### Support technique

* Les utilisateurs rencontrant des problèmes doivent ouvrir un dossier d’assistance auprès de l’assistance clientèle d’Adobe.
* Incluez l’ID d’organisation IMS dans les cas d’assistance pour une résolution plus rapide.
