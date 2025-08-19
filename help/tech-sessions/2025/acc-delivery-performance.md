---
title: Performances de diffusion de Adobe Campaign Classic - Dépannage
description: Cette session a couvert les principales stratégies permettant d’améliorer les performances des diffusions par e-mail et SMS à l’aide d’Adobe Campaign. Elle a permis de relever des défis courants tels que les retards de diffusion, le faible débit et la lenteur des transactions, en offrant des solutions tels que l’optimisation des lots, la journalisation SQL et la surveillance des performances du serveur. Les bonnes pratiques en matière de délivrabilité incluent l'authentification correcte des e-mails (SPF, DKIM, DMARC), la surveillance des listes noires et les vérifications de spam. Pour de meilleures performances, les experts recommandent de nettoyer les workflows, de limiter les règles et d’éviter les conteneurs partagés. Conseils de diffusion SMS axés sur la configuration correcte du compte externe et l’analyse des journaux. La session a également mis l’accent sur la validation du suivi, la maintenance de la base de données à l’aide de rapports de surcharge et l’application de règles de pression/fatigue pour stimuler l’engagement. Un enregistrement de session sera partagé par e-mail et publié sur le site d’Adobe Experience Platform.
solution: Campaign Classic v7
product: Adobe Campaign
feature: SMS, Deliverability, Troubleshooting
role: User
level: Beginner, Intermediate, Experienced
doc-type: Event
duration: 2257
last-substantial-update: 2025-04-25T00:00:00Z
jira: KT-17869
exl-id: a7e1e198-b63b-4a2a-9ffc-7f72bf4c61c1
source-git-commit: 3b54c46988da18248024d115997704d9881f5e68
workflow-type: tm+mt
source-wordcount: '442'
ht-degree: 0%

---

# Sessions techniques : Performances de diffusion Adobe Campaign Classic - Dépannage

Au cours de cette session, nous allons explorer les défis courants rencontrés lors de la fourniture de performances optimales avec Adobe Campaign Classic (ACC) et fournir des stratégies exploitables pour le dépannage et la résolution des problèmes. Les participants apprendront à identifier les goulets d&#39;étranglement en termes de performances, à corriger les incohérences en matière de préparation/configuration de la diffusion et à mettre en œuvre les bonnes pratiques pour assurer une communication fluide. De l’optimisation des diffusions à la résolution des difficultés techniques, ce webinaire dotera les participants des connaissances et des outils nécessaires pour améliorer l’efficacité de leurs campagnes ACC, obtenir de meilleurs résultats et offrir des expériences client de haute qualité.

>[!VIDEO](https://video.tv.adobe.com/v/3457826/?learn=on&enablevpops)

## Principaux points à retenir

**Défis et solutions en matière de prestation**

* Les problèmes courants incluent les retards de diffusion, les échecs de préparation, les diffusions bloquées, les faibles taux de réussite, le faible débit, le faible engagement et la lenteur des diffusions transactionnelles.
* Les solutions impliquent l’optimisation du traitement par lots des diffusions, la surveillance des performances du serveur, l’activation de la journalisation des requêtes SQL, la révision des journaux d’audit et la configuration appropriée des affinités MTA et IP.

**Bonnes pratiques en matière de délivrabilité**

* Vérifiez que l’authentification des e-mails est correcte (SPF, DKIM, DMARC).
* Surveillez les statuts des listes noires et évitez le déclenchement de spam.
* Utilisez les contrôles de spam pour évaluer les scores de spam avant d&#39;envoyer des e-mails.

**Optimisation des performances de diffusion**

* Utiliser des workflows de ciblage propres et limiter les champs de personnalisation.
* Implémentez des règles de limitation, de traitement par lots et de topologie pour les exclusions et le filtrage.
* Évitez de partager des conteneurs sur plusieurs canaux pour éviter les goulots d’étranglement.

**Résolution des problèmes de diffusion SMS**

* Vérifiez que les comptes externes sont configurés de manière unique et que les processus SMS sont en cours d’exécution.
* Recherchez des erreurs dans les journaux SMS et vérifiez les expressions régulières dans les paramètres SMP.
* Contactez le fournisseur de services pour tout problème de configuration incorrecte.

**Lenteur De Diffusion Transactionnelle**

* Surveillance des temps de traitement internes et totaux.
* Assurez-vous que la taille de diffusion est dans les limites (60 Go pour le lot, 30 Go pour l’événement).
* Vérifiez les règles de typologie et les paramètres de personnalisation.

**Suivi et engagement**

* Validez les workflows de tracking et les journaux du serveur.
* Testez les formules de suivi personnalisées dans les environnements inférieurs avant la production.
* Assurez-vous que les serveurs de suivi sont opérationnels.

**Maintenance de la base de données**

* Utilisez les rapports de gonflement pour identifier les tableaux présentant un gonflement élevé et justifier un vide de base de données.

**Recommandations générales**

* Utilisez les règles de pression et de fatigue pour limiter les e-mails inutiles.
* Segmentez les diffusions volumineuses en lots plus petits afin d’optimiser les performances.
