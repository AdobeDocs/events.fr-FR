---
title: Sessions techniques - Gestion du sous-domaine Adobe Campaign et du SSL dans le Panneau de Contrôle
description: Découvrez comment déléguer et configurer des sous-domaines dans le Panneau de Contrôle d'Adobe Campaign, configurer des certificats SSL et surveiller la configuration pour assurer la délivrabilité sécurisée des e-mails.
solution: Campaign
feature: Subdomains and Certificates
role: Admin, Developer, Leader, User
level: Beginner, Intermediate, Experienced
doc-type: Event
duration: 3409
last-substantial-update: 2025-09-05T00:00:00Z
jira: KT-18866
source-git-commit: 18ce421793d97372198151afc92b24f3bed053a8
workflow-type: tm+mt
source-wordcount: '344'
ht-degree: 0%

---


# Sessions techniques : gestion des sous-domaines Adobe Campaign et SSL dans le Panneau de Contrôle

Au cours de cette session, nous explorons les concepts de délégation et de configuration de sous-domaines dans Adobe Campaign, y compris l’installation de certificats SSL pour sécuriser les sous-domaines.

Découvrez ce qu’est un sous-domaine, ses objectifs et les méthodes de délégation qui permettent à Adobe de l’utiliser efficacement. La session aborde également les principes de sécurisation d’un sous-domaine par le biais de certificats SSL et les bonnes pratiques pour maintenir un environnement sécurisé.

Nous fournissons des conseils détaillés sur la configuration des sous-domaines à l’aide du Panneau de Contrôle en libre-service, en mettant en évidence les obstacles potentiels et la manière de les surmonter. Les participants acquièrent des connaissances pratiques pour assurer une configuration fluide et une gestion sécurisée de leurs sous-domaines.

Que vous soyez administrateur, développeur ou propriétaire de plateforme, cette session vous dote des compétences nécessaires pour configurer et sécuriser des sous-domaines en toute confiance dans Adobe Campaign.

>[!VIDEO](https://video.tv.adobe.com/v/3471391/?learn=on&enablevpops)

## Maîtriser la gestion des sous-domaines dans Adobe Campaign

Découvrez les principes de base de la délégation, de la configuration et de la sécurité des sous-domaines pour les communications électroniques Adobe Campaign :

* **Délégation de sous-domaine** Choisissez entre la délégation complète ou CNAME pour contrôler la manière dont Adobe gère la délivrabilité de vos DNS et e-mails.
* **Configuration DNS et SSL** Une configuration appropriée des certificats MX, SPF, DKIM, DMARC et SSL est essentielle pour un envoi d’e-mails sécurisé et fiable.
* **Panneau de Contrôle** utilisez l’outil en libre-service d’Adobe pour rationaliser la configuration des sous-domaines, surveiller les enregistrements et gérer les certificats SSL.
* **Pièges courants** Évitez les retards et les erreurs en comprenant les délais d’audit, les exigences en matière d’enregistrement et les étapes de dépannage.

La maîtrise de ces processus garantit la sécurité de vos campagnes, leur délivrabilité et le maintien de la réputation de votre marque.

## Méthodes de délégation ** complète ou CNAME

* **Délégation complète** Adobe gère tous les enregistrements DNS pour le sous-domaine, assurant une délivrabilité et une sécurité optimales. Recommandé pour la plupart des utilisateurs.
* **Délégation CNAME** Le client et Adobe partagent les mêmes responsabilités DNS. Le client crée des enregistrements CNAME pointant vers des ressources gérées par Adobe.
* **Principales différences :
* **Complète** Adobe dispose d’une autorité complète ; moins de maintenance client.
* **CNAME** Responsabilité partagée ; étapes manuelles supplémentaires pour le client.
* **Conseil** ne déléguez jamais votre domaine racine (uniquement les sous-domaines) pour éviter de perdre le contrôle sur votre domaine principal.
