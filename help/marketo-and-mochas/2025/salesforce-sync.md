---
title: Marketo et mochas - Synchronisation de Salesforce
description: Effectuez le Principal de la synchronisation Marketo-Salesforce avec des conseils d’experts sur les autorisations, la visibilité des champs, la collaboration entre administrateurs et administratrices et les bonnes pratiques pour garantir une intégration fluide et optimisée.
feature: Salesforce Integration
topic: Integrations
role: Admin, Developer, Leader, User
level: Beginner, Intermediate, Experienced
doc-type: Event
duration: 3547
last-substantial-update: 2025-08-07T00:00:00Z
jira: KT-18706
source-git-commit: bc5752512fb1bc50cefe0180c308574e821888a2
workflow-type: tm+mt
source-wordcount: '714'
ht-degree: 0%

---


# Marketo et mochas : synchronisation Salesforce

Marketo comporte très peu d’intégrations natives, mais Salesforce est la plus puissante de toutes. Avec environ 90 % de la clientèle Marketo qui utilise également Salesforce, Adobe s’engage à conseiller ses clients sur la manière de théoriser, de diagnostiquer et d’optimiser la synchronisation entre les deux. La synchronisation de Marketo avec SFDC repose en grande partie sur les autorisations dans SFDC accordées à l’utilisateur de synchronisation Marketo. Cela peut s’avérer difficile pour les clients, car plusieurs administrateurs ou différentes équipes créent des silos de communication autour des mises à jour du système.

Ce webinaire aborde les points suivants en ce qui concerne la synchronisation de SFDC &lt;-> Marketo :

· Expliquer le fonctionnement de la synchronisation à l’œil d’oiseau
· Masquage des champs et des objets de l’utilisateur de synchronisation Marketo dans SFDC
· Comment communiquer avec l’administrateur SFDC
· Comment travailler efficacement avec l’assistance Marketo
· Éléments à éviter lors de la synchronisation de Marketo avec SFDC

>[!VIDEO](https://video.tv.adobe.com/v/3470624/?learn=on&enablevpops)

## Bonnes pratiques relatives à l’utilisation de la synchronisation Salesforce

Pour utiliser efficacement la synchronisation Salesforce avec Marketo, suivez ces bonnes pratiques, expliquées étape par étape en termes simples :

1. **Comprendre le processus de synchronisation**

   La synchronisation connecte Marketo et Salesforce, ce qui permet aux données de circuler entre les deux systèmes. Considérez l’« utilisateur de synchronisation Marketo » comme un pont entre les deux plateformes. Cet utilisateur dispose des autorisations nécessaires pour lire et écrire certaines données :

   * **Accès en écriture** Leads et contacts (Marketo peut les mettre à jour dans Salesforce).
   * **Accès en lecture** Comptes, opportunités, objets personnalisés et activités (Marketo peut les afficher, mais ne peut pas les modifier).

   Lorsque les données changent dans Salesforce ou Marketo, la synchronisation met à jour l’autre système toutes les cinq minutes. Cependant, vous pouvez hiérarchiser les mises à jour urgentes à l’aide d’étapes de flux telles que « Synchroniser avec SFDC ».

1. **Nettoyer les champs**

   Ne synchronisez que les champs activement utilisés. Par exemple :

   * Si d’anciens champs comme « Notes relatives à la COVID-19 » ne sont plus pertinents, supprimez-les de la synchronisation. Cela réduit l’encombrement et accélère le processus.
   * Évitez de synchroniser les champs de formule (par exemple, « âge du prospect en jours »), car ils ne mettent pas à jour la date et l’heure, ce qui peut entraîner des problèmes.

1. **Prévenir les retards**

   Une liste d’attente se produit lorsque trop de données sont en attente de synchronisation. Pour éviter cela :

   * Limiter les mises à jour inutiles : par exemple, si le score d’un compte change légèrement (de 60 à 61, par exemple), il peut déclencher des mises à jour pour tous les contacts associés. Au lieu de cela, regroupez les scores par plages (par exemple, 0-25, 26-50) pour réduire les mises à jour.
   * Campagnes par lots : utilisez des campagnes par lots au lieu de déclencher des campagnes pour traiter les données plus efficacement.

1. **Gérer les erreurs**

   Des erreurs peuvent se produire lorsque Marketo tente de mettre à jour un champ dans Salesforce mais n’a pas l’autorisation. Pour résoudre les problèmes :

   * Connectez-vous à Salesforce en tant qu’utilisateur de synchronisation Marketo et essayez d’effectuer la même action. Cela permet d’identifier les problèmes d’autorisation ou les données non valides.
   * Configurez des campagnes récurrentes dans Marketo pour corriger les erreurs courantes, telles que la normalisation des valeurs de pays/état (par exemple, « CA » vers « Californie »).

1. **Utiliser des filtres de synchronisation personnalisés**

   Les filtres personnalisés vous permettent de contrôler les enregistrements synchronisés entre Salesforce et Marketo. Par exemple, créez un champ appelé « Ne pas synchroniser avec Marketo ». Si ce champ est marqué comme « true » pour un enregistrement, il ne se synchronise pas avec Marketo. Cela s’avère utile pour exclure les adresses e-mail non valides ou les contacts obsolètes.

1. **Limiter la création de la tâche**

   Salesforce elm. Concentrez-vous sur les activités significatives comme le « formulaire rempli » ou le « lien cliqué dans l’e-mail ».

1. **Collaborer avec votre administrateur Salesforce**

   Comme la synchronisation implique les deux systèmes, travaillez en étroite collaboration avec votre administrateur Salesforce pour :

   * Gérez les autorisations de l’utilisateur de synchronisation Marketo.
   * Nettoyez les champs inutiles dans Salesforce.
   * Résolvez ensemble les problèmes de synchronisation.

1. **Surveillance des performances de synchronisation**

   Vérifiez régulièrement le statut de la synchronisation dans la section d’administration de Marketo :

   Recherchez les pics dans les tableaux de bord « Tendance de la liste d’attente de synchronisation » ou « Débit de synchronisation ». Elles indiquent des retards ou des mises à jour excessives.
Si vous constatez des problèmes, identifiez les champs ou les enregistrements à l’origine du problème.

1. **Utilisez Les Objets Personnalisés Avec Sagesse**

   Les objets personnalisés sont des structures de données spéciales qui peuvent stocker des informations supplémentaires (par exemple, des détails de produit). Synchronisez uniquement les objets personnalisés nécessaires à vos campagnes pour éviter de surcharger votre base de données.

1. **Planifiez l’évolutivité**

   Lors de la configuration de la synchronisation, pensez à long terme :

   * Conservez un dictionnaire de données pour suivre les champs synchronisés et pourquoi.
   * Évitez de synchroniser des champs ou des enregistrements inutiles pour maintenir l’efficacité du système.

En suivant ces étapes, vous pouvez garantir une intégration fluide et efficace entre Marketo et Salesforce, ce qui réduit le nombre d’erreurs et optimise la valeur de vos données.
