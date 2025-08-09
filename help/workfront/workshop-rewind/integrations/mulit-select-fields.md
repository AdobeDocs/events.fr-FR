---
title: Naviguer facilement dans l’API Workfront et les modifications de fusion pour les champs à sélection multiple
description: Découvrez les modifications à venir de l’API Adobe Workfront et de Fusion , notamment les mises à jour des champs à sélection multiple, le contrôle de version des abonnements aux événements et les stratégies pour empêcher les modifications avec rupture.
feature: Workfront API, Workfront Fusion, Workfront Integrations and Apps
topic: Integrations
role: Admin, Developer, Leader, User
level: Beginner, Intermediate, Experienced
doc-type: Event
duration: 3172
last-substantial-update: 2025-08-08T00:00:00Z
jira: KT-18631
source-git-commit: 6225f36c5d26ecca5ebc2aca24a2d592a3279570
workflow-type: tm+mt
source-wordcount: '340'
ht-degree: 0%

---


# Naviguer facilement dans l’API Workfront et les modifications de fusion pour les champs à sélection multiple

Cet atelier a été enregistré le 25 juin 2025 et comprenait Andy Hess, qui partageait les modifications à venir de l’API Workfront et de Fusion.

>[!VIDEO](https://video.tv.adobe.com/v/3469978/?learn=on&enablevpops)

## Ressources

Outre l’enregistrement à la demande, nous avons inclus la présentation et des ressources supplémentaires :
* [Diaporama PDF](https://workfront-experience.s3.us-west-2.amazonaws.com/Training/Guides/Customer+Success+at+Scale/Navigating+the+API+and+Fusion+Changes+for+Multi-Select+Fields+with+Ease+062425.pdf)
* Un événement organisé en partenariat avec l’équipe de développement logiciel d’Adobe a eu lieu début mai sur les modifications apportées aux abonnements aux événements si vous souhaitez en savoir plus sur ce domaine spécifique, [[suivi des événements] Préserver vos scénarios Fusion lors de la mise à niveau de la version V2 des abonnements aux événements](https://experienceleaguecommunities.adobe.com/t5/workfront-discussions/event-follow-up-preserving-your-fusion-scenarios-during-the/m-p/754182#M4041)

## Principaux points à retenir et ressources

* Les modifications apportées aux champs à sélection multiple de l’API Workfront seront publiées dans la version 21 (octobre 2025) afin d’assurer un format de tableau JSON cohérent au lieu de réponses mixtes de type chaîne/tableau
* Le contrôle de version de l’abonnement aux événements est en cours d’introduction. La version 2 renverra toujours les champs à sélection multiple sous forme de tableaux, tandis que la version 1 conserve le comportement incohérent actuel
* Les nouveaux abonnements aux événements sont automatiquement mis à niveau par défaut vers la version 2. Tous les abonnements seront automatiquement mis à niveau vers la version 2 à la mi-janvier 2026
* Une nouvelle version du connecteur Workfront sera publiée plus tard cette année avec un processus de mise à niveau manuelle pour préserver le mappage des modules et empêcher les modifications avec rupture
* L’assistant Fusion AI est actuellement disponible, mais nécessite un contrat d’IA signé et une configuration de licence appropriée. Contactez votre gestionnaire de compte si vous avez des questions ou si vous souhaitez en savoir plus. [Plus d’informations sur l’utilisation de l’IA dans Fusion](https://experienceleague.adobe.com/en/docs/workfront-fusion/using/manage-scenarios/fusion-ai-assistant)
* [Modèles Workfront Fusion actuellement disponibles](https://experienceleague.adobe.com/en/docs/workfront-fusion/using/create-and-manage-templates/currently-available-fusion-templates)
* [Appeler pour les modèles Fusion](https://experienceleaguecommunities.adobe.com/t5/workfront-discussions/call-for-fusion-template-ideas/m-p/732085#M3686)- si vous avez des suggestions de nouveaux modèles Fusion, ajoutez-les ici ! C’est de là que l’équipe tire ses idées  

Si vous avez des questions complémentaires, veuillez répondre à cette [publication de la communauté Experience League](https://experienceleaguecommunities.adobe.com/t5/workfront-discussions/event-follow-up-navigating-the-workfront-api-and-fusion-changes/td-p/761253) ! 

Nous espérons vous voir lors des futurs ateliers sur le succès client !  Veillez à consulter les [Événements Workfront](https://experienceleague.adobe.com/events/?filters=Workfront) sur Experience League pour obtenir la liste complète et vous inscrire.