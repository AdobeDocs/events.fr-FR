---
title: Campagnes exécutables - Découvrez comment les exécutables peuvent générer de l’efficacité et de l’impact
description: La session est destinée aux administrateurs Marketo et aux professionnels des opérations de campagne. Elle se concentre sur la compréhension et le déploiement de campagnes exécutables afin d’ajouter de la valeur aux campagnes et programmes, de créer de l’efficacité et de stimuler la croissance.
role: Developer, User
level: Intermediate, Experienced
doc-type: Event
duration: 3778
last-substantial-update: 2024-03-07T00:00:00Z
jira: KT-15098
thumbnail: 3427704.jpeg
exl-id: cfea1a1a-2d29-4cf6-b633-aa2a2523114e
source-git-commit: 5edfadf5b805161f9624068f70a7b4830ab84d72
workflow-type: tm+mt
source-wordcount: '468'
ht-degree: 0%

---

# Campagnes exécutables - Découvrez comment les exécutables peuvent accroître l’efficacité et l’impact

>[!VIDEO](https://video.tv.adobe.com/v/3427704/?learn=on)

**Modéré par** Chris Willis
**Discours** Courtny Edwards-Jones et Jane Musatova

## Vue d’ensemble

Dans cette édition de Deep Dive, championne de l’Adobe, nous discutons de l’utilisation des campagnes exécutables dans Marketo et nous proposons des exemples d’utilisation pour rationaliser les processus et garantir la précision des données. Les campagnes exécutables sont un type de campagne dynamique qui s’exécute de manière synchrone, ce qui permet d’établir des dépendances entre différentes étapes. Ils peuvent être utilisés pour essayer de relancer automatiquement les processus en échec, tels que la normalisation des données ou la qualification des pistes, avant de passer à l’étape suivante. Le document couvre également l’utilisation des campagnes parentes et des exécutables imbriqués, ainsi que les limitations des campagnes exécutables, telles que l’impossibilité d’utiliser des webhooks ou les étapes d’attente.

## Quel est l’objectif de l’utilisation de campagnes exécutables ?

L’utilisation de campagnes exécutables a pour but de rationaliser et d’automatiser des workflows complexes dans Marketo. Les campagnes exécutables vous permettent de définir une séquence d’actions à effectuer avant de passer à l’étape suivante d’une campagne. Cela garantit que chaque action est entièrement exécutée avant de continuer, ce qui réduit le risque d’erreurs ou de processus incomplets. Les campagnes exécutables peuvent être utilisées pour essayer de relancer des processus en échec, normaliser et enrichir les données, qualifier des pistes, capturer des moments intéressants, etc. Ils offrent un moyen plus efficace et plus organisé de gérer et d’automatiser vos opérations marketing.

## Qu’est-ce qu’une campagne exécutable et comment fonctionne-t-elle ?

Une campagne exécutable est un type de campagne dynamique dans Marketo qui permet l’exécution séquentielle de plusieurs flux au sein d’une seule campagne. Il est conçu pour s’assurer que chaque flux est entièrement exécuté avant le début du suivant. Cela diffère d’une campagne de requêtes qui s’exécute de manière asynchrone et qui peut comporter plusieurs flux s’exécutant en parallèle.

Pour créer une campagne exécutable, vous devez cocher la case &quot;Exécutable&quot; lors de la création de la campagne. Une fois créées, vous pouvez ajouter des étapes de flux à la campagne, telles que la modification des valeurs des données, l’envoi d’emails ou la mise à jour des statuts du programme. Cependant, il existe certaines limites aux campagnes exécutables. Vous ne pouvez pas utiliser de déclencheurs, de webhooks ou d’étapes d’attente dans une campagne exécutable.

Les campagnes exécutables sont utiles pour les processus qui ont des dépendances les uns sur les autres, où un flux doit être terminé avant que le suivant puisse commencer. Ils peuvent contribuer à rationaliser les processus opérationnels, à simplifier le traitement des données et à minimiser le risque d’erreurs ou de retards. En utilisant des campagnes exécutables, vous pouvez vous assurer que chaque étape d’un processus est terminée avant de passer à la suivante, ce qui améliore l’efficacité et la précision de vos opérations marketing.