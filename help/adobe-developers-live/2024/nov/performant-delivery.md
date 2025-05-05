---
title: Bonnes pratiques de diffusion performante
description: Optimisez la diffusion multimédia et les performances avec Dynamic Media en exploitant la diffusion en continu adaptative, les profils vidéo personnalisés, les bonnes pratiques d’optimisation pour les moteurs de recherche, l’optimisation des images, la gestion de contenu en bloc, les paramètres prédéfinis de la visionneuse, l’invalidation du cache et l’imagerie dynamique.
feature: Dynamic Media, Video, SEO Optimization, Smart Imaging, Viewer Presets, Best Practices
topic: Content Management
solution: Experience Manager, Experience Manager Assets
role: Developer
level: Beginner, Intermediate
doc-type: Event
duration: 1596
last-substantial-update: 2024-11-26T00:00:00Z
jira: KT-16572
exl-id: a1920020-b9ce-43be-8f9e-e52aac68da7b
source-git-commit: 946d7cd484e8c5d4358d4099b3518705cab8d4a3
workflow-type: tm+mt
source-wordcount: '368'
ht-degree: 0%

---

# Bonnes pratiques de diffusion performante

Rejoignez Riya Midha, responsable produit senior chez Adobe, pour découvrir les bonnes pratiques de configuration d’Adobe Experience Manager Assets Dynamic Media. Découvrez comment optimiser la diffusion de ressources, améliorer la diffusion vidéo en continu, configurer des visionneuses et mesurer et améliorer les performances.

>[!VIDEO](https://video.tv.adobe.com/v/3440419/?learn=on&enablevpops&captions=fre_fr)

## Discussions communautaires

Poursuivez la conversation dans la communauté Adobe Developers Live [discussion](https://adobe.ly/3YGedpb).

## Principales acquisitions

* **Fonctionnalités Dynamic Media** Dynamic Media permet une diffusion rapide et flexible de médias personnalisés de haute qualité sur plusieurs appareils, en gérant plus de 9 000 milliards de diffusions multimédia par an et des volumes de pointe quotidiens pouvant atteindre 69 milliards de ressources.
* **Diffusion en continu adaptative** L’utilisation de la diffusion en continu adaptative pour la diffusion vidéo réduit considérablement la mise en mémoire tampon. Un test a montré une réduction du nombre de tampons de 50 à 5 sur une vidéo de 60 secondes avec une bande passante limitée de 5 Mbit/s.
* **Profils vidéo** La création de profils vidéo personnalisés avec divers codages de qualité garantit des performances vidéo optimales dans des conditions réseau variées.
* **Bonnes pratiques relatives à l’optimisation pour les moteurs de recherche**
   * Utilisez des ensembles de règles pour créer des URL descriptives afin d’optimiser l’optimisation du référencement.
   * Ajoutez des attributs de texte de remplacement et de titre aux images.
   * Utilisez l’imagerie dynamique et les formats d’image les plus récents, tels que WebP, pour de meilleurs classements de recherche.
* **Optimisation d’image**
   * Utilisez les paramètres de mise à l’échelle pour ajuster la résolution de l’image en fonction de la taille de l’écran.
   * Évitez d’utiliser une qualité de 100 % pour les images ; utilisez plutôt une plage de 80 à 90 % pour réduire la taille du fichier sans perte de qualité perceptible.
   * Appliquez des paramètres d’accentuation pour améliorer la clarté du texte dans les images.
* **Gestion de contenu en bloc**
   * Segmenter le contenu destiné à la diffusion Dynamic Media d’un autre contenu.
   * Utilisez la synchronisation sélective pour optimiser les temps de traitement et améliorer le temps de mise sur le marché.
* **Paramètres prédéfinis de la visionneuse** Personnalisez l’aspect et le comportement de la visionneuse à l’aide des paramètres prédéfinis de la visionneuse sans modification du code. Par exemple, la modification des boutons de lecture/pause, l’activation de la lecture automatique et de la boucle, ainsi que l’ajout de superpositions d’images.
* **Invalidation du cache** Utilisez l’invalidation du cache pour refléter immédiatement les modifications apportées aux ressources déjà publiées, en contournant le délai d’activation de 10 heures par défaut.
* **Surveillance et débogage** Utilisez des outils tels que l’appli de bureau AEM et la page Query Debugger pour effectuer le suivi des tâches de traitement et identifier les ressources non traitées.
* **Imagerie dynamique** L’imagerie dynamique est activée par défaut sur tous les domaines, ce qui réduit la taille des fichiers image et améliore les temps de chargement.
