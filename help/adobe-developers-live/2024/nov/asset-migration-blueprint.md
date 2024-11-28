---
title: Plan directeur de la migration Assets
description: Découvrez comment migrer un DAM hérité vers Adobe Experience Manager Assets avec des insights d’Achim Koch, qui couvrent l’analyse des parties prenantes, la planification des ressources, la transformation des données et les bonnes pratiques comme l’utilisation de fichiers CSV pour la gestion des données.
feature: Migration
topic: Migration
solution: Experience Manager, Experience Manager Assets
role: Developer
level: Beginner, Intermediate
doc-type: Event
duration: 1690
last-substantial-update: 2024-11-26T00:00:00Z
jira: KT-16576
exl-id: f588055b-05c7-44df-be67-799a0e3ee1ed
source-git-commit: 946d7cd484e8c5d4358d4099b3518705cab8d4a3
workflow-type: tm+mt
source-wordcount: '338'
ht-degree: 0%

---

# Plan directeur de la migration Assets

Rejoignez Achim Koch, architecte technique principal chez Adobe, pour découvrir comment migrer un DAM hérité vers Adobe Experience Manager Assets. Obtenez des informations sur l’analyse des parties prenantes, la planification des ressources, la transformation des données et les bonnes pratiques, telles que l’utilisation de fichiers CSV pour la gestion des données. Créez une feuille de route pour vos propres projets de migration Adobe Experience Manager.

>[!VIDEO](https://video.tv.adobe.com/v/3440403/?learn=on&enablevpops)

## Discussions communautaires

Poursuivez la conversation dans la communauté Adobe Developers Live [discussion](https://adobe.ly/4hKHpnF).

## Principales acquisitions

* **Aucun outil prêt à l’emploi pour la migration** Il n’existe aucun outil unique pouvant migrer de divers systèmes hérités vers Adobe Experience Manager (AEM) en raison de la diversité des produits et des solutions personnalisées.

* **Cinq étapes de migration**

   * Planification du projet
   * Planification de l’implémentation
   * Implémentation AEM
   * Implémentation du script de migration
   * Exécution de la migration

* **Participation des parties prenantes** Il est essentiel d’identifier et d’impliquer les parties prenantes telles que les sponsors, les utilisateurs professionnels, les administrateurs système informatique et la prise en charge du système hérité.

* **Planification des ressources et de la chronologie** Assurez-vous que les ressources sont disponibles et planifiez les jours fériés, les heures de pointe et les fenêtres non limitées.

* **Planification technique** Cela inclut l’analyse des exigences, la transformation des données et la planification de l’infrastructure.

* **Processus itératif** La migration implique plusieurs itérations d’exécution de script, d’analyse, de retour et d’adaptation.

* **Utilisation des fichiers CSV** Les fichiers CSV sont recommandés pour faciliter leur utilisation et leur lisibilité pendant le processus de migration.

* **Node.js de langage de script** est recommandé pour sa prise en charge du format CSV, AWS et HTTP et pour être une bonne occasion d’apprendre JavaScript.

* **Qualité et répétabilité** Assurez une migration de données de haute qualité, conservez les données d’origine et les fichiers CSV à titre de référence et rendez le processus répétable.

* **Gel de contenu** Déclarez un gel de contenu pendant la migration pour empêcher l’ajout de nouvelles données après la prise de l’instantané.

* **Outils et conseils** Utilisez des outils tels que VS Code avec l’extension Rainbow CSV et tenez compte du marqueur d’ordre des octets (BOM) pour les fichiers texte UTF-8.

* **Validation de l’entreprise** Réservez du temps pour tester et obtenir l’approbation officielle de l’entreprise après la migration afin de lever le gel du contenu.
