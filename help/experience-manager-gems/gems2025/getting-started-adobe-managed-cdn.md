---
title: AEM GEMs - Prise en main du réseau CDN géré par l’Adobe
description: Découvrez comment configurer le réseau CDN géré par l’Adobe dans AEM Cloud Service pour améliorer les performances et la sécurité avec les nouvelles fonctionnalités de configuration du réseau CDN.
role: Developer, User
level: Intermediate
doc-type: Event
duration: 3438
last-substantial-update: 2025-01-30T00:00:00Z
jira: KT-17227
source-git-commit: 1cfa9cdb0e973e6d088b1faeaa63539b0a7fba36
workflow-type: tm+mt
source-wordcount: '437'
ht-degree: 0%

---


# AEM GEMs - Prise en main du réseau CDN géré par l’Adobe

Découvrez le réseau CDN géré par Adobe dans AEM Cloud Service et comment le configurer. Rejoignez-nous pour explorer les nouvelles fonctionnalités de configuration du réseau CDN qui peuvent être utilisées pour améliorer les performances et la sécurité de vos applications AEM as a Cloud Service. Au cours de cette session, vous découvrirez :

* Qu’est-ce que le réseau CDN d’Adobe ?
* Topologies pertinentes pour AEMaaCS et les Edge Delivery Services
* Cas d’utilisation standard pouvant être mis en œuvre avec des règles CDN
* Utilisation des RDE pour tester et déployer rapidement des configurations de réseau CDN

>[!VIDEO](https://video.tv.adobe.com/v/3443168/?learn=on&enablevpops)

*Enregistrement le 22 janvier 2025*

Vous avez une question, peut-être un commentaire?  Rejoignez la discussion dans les [communautés Experience League ](https://adobe.ly/4haufPK) !

## Principaux points à retenir

### Fonctionnalités clés du réseau CDN géré par Adobe

* **Domaines et certificats personnalisés** Essentiel pour héberger des domaines et certificats personnalisés et établir des connexions sécurisées.
* **Mise en cache** La diffusion des réponses HTTP à partir du cache est beaucoup plus rapide (moins de 10 millisecondes) que la récupération à partir de l’origine (des centaines de millisecondes).
* L’Adobe **réseau CDN prêt à l’emploi et personnalisé** fournit un réseau CDN géré prêt à l’emploi, mais les utilisateurs peuvent également apporter leur propre réseau CDN.

### Options de configuration

* **Transformations de requête** modifiez les en-têtes, les chemins de réécriture, bloquez le trafic et les requêtes de redirection.
* **Filtres de trafic** Bloquez ou autorisez le trafic selon des règles spécifiques.
* **Authentification** Prise en charge de la clé Edge, de la clé Push et de l’authentification de base.
* **Sélecteurs d’origine** requêtes proxy vers différentes origines en fonction de règles définies.
* **Transformations de réponse** modifiez les en-têtes et le statut des réponses.

### Déploiement et personnalisation

* **Pipeline de configuration** Déployez les fichiers YAML pour configurer les règles CDN.
* **Protection du trafic** utilisez des règles de filtrage du trafic pour bloquer, consigner et alerter le trafic en fonction de modèles.
* **Limitation de débit** Protect contre les attaques DDoS en limitant le nombre de requêtes par adresse IP.

### Outils et analyses

* **Pile Kibana Elasticsearch** Analysez l&#39;utilisation et le trafic avec les tableaux de bord fournis.
* **Transfert de journal** Transférez les journaux vers une instance Splunk pour analyse.

### Faits saillants de la démonstration

* **Configurations de déploiement** Démonstration des règles de filtrage du trafic et des redirections.
* **Authentification et sélection d’origine** explique comment configurer l’authentification de base et le trafic proxy vers différentes origines.

### Bonnes pratiques

* **Réponses rapides** assurez des réponses rapides à partir des origines pour éviter les vulnérabilités.
* **Bonne mise en cache** utilisez la mise en cache pour gérer efficacement le trafic.
* **Utilisez des tableaux de bord** Analysez le trafic et l’utilisation pour définir des limites de débit appropriées.
* **Combiner les stratégies** Utilisez différentes stratégies de limitation de débit pour une meilleure protection.
* **Définir des alertes** Recevez des notifications lorsque le site est attaqué.
* **Test des règles** Commencez par consigner les actions avant le blocage pour vous assurer que les règles fonctionnent comme prévu.

### Contact et commentaires

* **Commentaires et cas d’utilisation** Contactez l’équipe pour des cas d’utilisation et des commentaires avancés.
* **Sessions futures** Participez aux sondages pour suggérer des sujets pour les sessions futures.