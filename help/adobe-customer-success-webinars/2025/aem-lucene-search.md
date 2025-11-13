---
title: Conseils essentiels et bonnes pratiques pour la recherche AEM Lucene
description: Stimulez l’engagement numérique avec les outils de recherche AEM avancés tels que les filtres, les facettes, la suggestion automatique, la NGram et la vérification orthographique. Apprenez de démonstrations du monde réel.
solution: Experience Manager
feature: Search
role: Admin, Developer
level: Intermediate, Experienced
doc-type: Event
duration: 3630
last-substantial-update: 2025-11-13T00:00:00Z
jira: KT-19550
source-git-commit: 84c9a126769fa94b0197d12ca594137e13edc510
workflow-type: tm+mt
source-wordcount: '418'
ht-degree: 0%

---


# Conseils essentiels et bonnes pratiques pour la recherche AEM Lucene

Découvrez comment améliorer votre présence numérique et l’engagement des clients grâce à des fonctionnalités de recherche de pointe, notamment des filtres, des facettes, des suggestions automatiques, la NGram et la vérification orthographique. Découvrez des démonstrations réelles et obtenez des informations sur l’optimisation de vos fonctionnalités de recherche avec AEM et Lucene. Ce webinaire vous donne l’occasion d’améliorer votre expérience de recherche et de garder une longueur d’avance sur le paysage numérique.

>[!VIDEO](https://video.tv.adobe.com/v/3476410/?learn=on&enablevpops)

## Déverrouiller une recherche puissante dans Adobe Experience Manager

Adobe Experience Manager (AEM) tire parti de la recherche Lucene pour offrir des résultats rapides et pertinents sur le contenu, les ressources et les métadonnées. Cette session explique le fonctionnement des index Lucene, comment les configurer et les bonnes pratiques pour optimiser les performances de recherche.

* **La recherche Lucene est omniprésente** elle optimise la recherche dans l’auteur, l’éditeur et les portails AEM, en gérant les suggestions automatiques, les filtres, les facettes et la pagination.
* **Les définitions d’index optimisent les performances** la personnalisation des définitions d’index Oak est essentielle pour une recherche efficace et ciblée.
* **Les bonnes pratiques sont importantes** copiez les définitions d’index existantes, limitez les propriétés indexées et utilisez les indicateurs appropriés pour effectuer des recherches de texte intégral et de propriétés.
* **Les fonctionnalités avancées améliorent l’expérience utilisateur** les facettes, la suggestion automatique, la vérification orthographique, l’amplification et la correction peuvent être activées pour des expériences de recherche plus riches.

La compréhension de ces principes permet de garantir des fonctionnalités de recherche stables et à forte valeur ajoutée dans AEM, en prenant en charge les objectifs techniques et commerciaux.

## Blocs de création de l’index Lucene

Les définitions d’index AEM Lucene sont la base des performances et de la précision des recherches. Les principaux composants sont les suivants :

* **Type** Spécifie le type d’index (Lucene, propriété, etc.).
* **Restriction de type de nœud** cible des types de contenu spécifiques (par exemple, dam:Asset, cq:Page).
* **Restriction de chemin d’accès** Limite l’indexation aux chemins de référentiel définis pour plus d’efficacité.
* **Règles d’agrégat** contrôle la profondeur et la portée du contenu indexé, en s’assurant que les propriétés pertinentes sont consultables.
* **Règles d’index** configuration principale ; définit des indicateurs tels que nodeScopeIndex (recherche en texte intégral large) et analyze (tokenisation/normalisation).

La configuration soigneuse de ces éléments garantit que les requêtes de recherche sont rapides, pertinentes et efficaces en termes de ressources.

## Optimisation des performances de recherche

L’optimisation efficace des recherches dans AEM Lucene implique une configuration stratégique et le respect des bonnes pratiques :

* **Commencez avec des index existants** copiez et modifiez toujours des définitions prêtes à l’emploi, et ne créez jamais à partir de zéro.
* **Limiter les propriétés indexées** incluez uniquement les propriétés nécessaires pour que les index restent nettoyés et performants.
* **Utilisation judicieuse des indicateurs :
   * **nodeScopeIndex** true pour une recherche en texte intégral large
   * **analyze** true pour la segmentation en unités lexicales au niveau de la propriété
   * **assessmentPathRestriction** true pour les requêtes basées sur les chemins d’accès
* **Indexation de propriété** La restriction de propriété recherche les meilleures performances ; utilisez le texte intégral uniquement lorsque cela est nécessaire.
* **Tri et facettes** Activez propertyIndex et l’ordre de tri ; définissez la facette** true pour le filtrage basé sur le nombre.

L’application de ces stratégies accélère les requêtes, réduit l’utilisation des ressources et donne des résultats plus pertinents.

