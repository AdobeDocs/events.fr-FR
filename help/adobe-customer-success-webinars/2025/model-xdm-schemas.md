---
title: Bonnes pratiques et informations pour la modélisation des schémas XDM
description: Modélisation des données de Principal dans AEP avec des schémas XDM, la gestion des identités et les bonnes pratiques pour une personnalisation et une segmentation évolutives en temps réel.
topic: Personalization
role: Developer
level: Intermediate
doc-type: Event
duration: 3488
last-substantial-update: 2025-05-08T00:00:00Z
jira: KT-18019
source-git-commit: cfc7b54ae4360779ca2c41f88fc08089bae99165
workflow-type: tm+mt
source-wordcount: '287'
ht-degree: 0%

---


# Bonnes pratiques et informations pour la modélisation des schémas XDM

Au cours de cette session, découvrez les bonnes pratiques et les raccourcis essentiels pour créer des modèles de données d’expérience (XDM) Adobe évolutifs et de haute qualité qui s’alignent sur les normes Adobe Experience Platform. Obtenez des informations sur le mappage efficace de l’expérience client et des données de cas d’utilisation à XDM pour une intégration transparente à Adobe et aux outils externes.

## Points de discussion

* Définition et organisation des composants XDM pour garantir des modèles de données évolutifs et flexibles
* Défis courants liés à la conception, l’évolution et la maintenance de XDM

>[!VIDEO](https://video.tv.adobe.com/v/3458042/?learn=on&enablevpops)

## Principaux points à retenir

**Modélisation des données dans Adobe Experience Platform (AEP)**

Le schéma XDM est la base de la modélisation des données dans AEP. Il permet l’intégration et le partage de données entre différents systèmes. Il définit la structure et la signification des données, telles que les attributs de profil et les actions basées sur un événement.

**Identity Management**

Une gestion des identités appropriée est essentielle pour éviter des problèmes tels que l’effondrement d’un profil. Le hachage de données sensibles telles que les e-mails et l’utilisation d’identifiants uniques peuvent contribuer à maintenir l’intégrité des données. Les mappages d’identités sont recommandés pour la segmentation et la personnalisation en temps réel.

**Bonnes pratiques de conception de schéma**

Simplifiez les schémas et concentrez-vous sur les cas d’utilisation marketing. Évitez de surcharger les schémas avec des attributs inutiles. Utilisez des groupes de champs normalisés et minimisez les personnalisations pour l’évolutivité et la pérennisation.

**Attributs d’événement ou de profil**

Décidez de modéliser les données en tant qu’attributs de profil ou événements en fonction des objectifs marketing. Les attributs de profil sont adaptés au ciblage en temps réel, tandis que les événements fournissent des informations historiques pour la segmentation basée sur le temps.

**Gestion des profils réduits et évolutivité**

Les profils réduits ne peuvent être corrigés que par la prise en charge d’Adobe, mais les règles relatives aux graphiques d’identités peuvent empêcher les réductions futures. Pour restructurer les schémas existants, il est recommandé d’extraire les données nécessaires et de repartir de zéro avec un schéma nettoyé.
