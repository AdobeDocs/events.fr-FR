---
title: Demandez aux experts - Extensions utiles dans les balises (Launch) pour aider à surcharger le SDK Web
description: Pensez-vous à migrer votre mise en oeuvre vers le nouveau SDK Web Adobe ?  Nous allons parcourir certaines de nos extensions préférées dans la bibliothèque de balises d’Adobe qui vous aideront à passer votre collecte de données au niveau suivant.
solution: Data Collection,Experience Platform
kt: 10528
thumbnail: https://video.tv.adobe.com/v/346610?format=jpeg
event-start-time: 2022-08-23 09:00-7
event-guests: Rudi Shumpert,Jeff Chasin,Eric Matisoff
exl-id: 5ef987f4-37f5-473f-b9f2-1598b7e655ba
duration: 3833
source-git-commit: 9a297cda953d4414131657f9ac84580aea0eabeb
workflow-type: tm+mt
source-wordcount: '675'
ht-degree: 0%

---

# Demandez aux experts : Extensions utiles dans les balises (Launch) pour aider à surcharger le SDK Web

Pensez-vous à migrer votre mise en oeuvre vers le nouveau SDK Web Adobe ?  Nous allons parcourir certaines de nos extensions préférées dans la bibliothèque de balises d’Adobe qui vous aideront à passer votre collecte de données au niveau suivant.

>[!VIDEO](https://video.tv.adobe.com/v/346610/?quality=12&learn=on)

## Questions et commentaires du programme

### Extension de l’assistant d’éléments de données à partir d’Evolyse

<br> 
**Question :** Du point de vue de la sécurité des données, Evolytics est-il sécurisé à utiliser, puisqu’il s’agit d’une extension tierce ?

**Réponse :** Oui. Vous pouvez consulter le code d’extension si vous le souhaitez. De plus, il n’enregistre aucune date, il effectue simplement une transformation.

<br> 

**Question :** Cette capture correspond-elle également à l’Adobe ECID ?

**Réponse :** L’ECID d’Adobe n’est pas capturé dans cette extension. Cette extension est destinée à créer des identifiants anonymes supplémentaires (entre autres).

**Réponse :** L’Adobe ECID peut être capturé de différentes manières. Nous le partagerons via les notes ExL et le Twitter car nous ne pouvons pas partager les liens du chat ici.

<br> 

**Question :** La fonctionnalité de hachage propose-t-elle diverses techniques de hachage comme SHA-256 et fournit-elle des clés publiques et privées ?

**Réponse :** Oui ! SHA-256 est la valeur par défaut.

<br> 

### Questions et commentaires généraux :

<br> 

**Question :** Sur quoi cliquons-nous pour télécharger les fichiers source pour les extensions ? Est-ce dans le &quot;menu à 3 points&quot; ?

**Réponse :** Oui ! Les 3 points, puis Télécharger la source (depuis la vue Catalogue)

<br> 

**Commentaire :** Une des choses que je creuse vraiment avec les extensions c&#39;est leur gain de temps. Beaucoup d&#39;entre eux vous font des choses *can* utilisez du code personnalisé, mais avec une extension , vous n’avez pas besoin d’écrire ce code.

**Répondre :** Tout de suite. Et il est reproductible sans avoir à recréer la roue à chaque fois.

<br> 

**Question :** Comment les modules externes d’analyse seront-ils pris en charge ou remplacés par des mises en oeuvre de SDK Web ?

**Réponse :** De nombreux modules externes d’analyse sont en fait inutiles ces jours-ci grâce à une flexibilité supplémentaire de Workspace et des balises d’Adobe. Toutefois, ceux qui ne le sont pas sont activement migrés pour être utilisés par le SDK Web.

<br> 

**Question :** Développement du suivi d’Activity Map à l’aide du SDK Web ?

**Réponse :** Je suis heureux d’annoncer que Activity Map est activement utilisé pour la prise en charge dans le SDK Web.

<br> 

**Question :** Pourrions-nous avoir accès au réseau Adobe Edge pour gérer les événements avant de les transférer vers les destinations finales ? Je comprends que nous pouvons aussi le faire dans Launch, mais dans le futur serait-il possible de le faire aussi sur le serveur ?

**Réponse :** Oui ! Cela est possible grâce à notre fonctionnalité de transfert d’événements, que les clients peuvent acheter via n’importe quel de nos produits Real-Time CDP (Real-Time CDP Connections, Prime ou Ultimate).

**Réponse :** Les connexions RTCDP (transfert d’événements) permettent d’avoir plus de contrôle avant de l’envoyer vers des destinations non adobe.

**Réponse :** Consultez quelques-unes de nos autres vidéos ExL Live pour en savoir plus à ce sujet (comme [celui-ci](exl-live-episode-06-23-22.md)).

<br> 

**Commentaire :** Appel rapide pour l’une de mes extensions préférées : il existe une extension de table de mappage où vous pouvez lire un tableau pour un élément de données qui &quot;si cette valeur est alors défini comme cela&quot;.

**Répondre :** La flexibilité qu&#39;ils offrent est impressionnante. Notez également que les entreprises peuvent également créer leurs propres extensions privées si elles le souhaitent.

<br> 

**Question :** Vous avez montré les données individuelles de la gestion de la relation client comme la ville et la météo, où stockons-nous la réponse individuelle ?

**Réponse :** Les réponses sont stockées dans chaque événement unique qui déclenche une règle dans une propriété Event Forwarding et sont utilisées uniquement dans cet événement spécifique.

<br> 

Poursuivez la discussion sur ce sujet dans la section [Discussions de la communauté Experience League](https://experienceleaguecommunities.adobe.com/t5/adobe-experience-platform/experience-league-live-post-session-discussion-useful-extensions/m-p/542620#M240).
<br> 

## Sessions LIVE Experience League supplémentaires de cette série de collecte de données

* [Demandez aux experts - Principes de base du SDK Web](exl-live-episode-05-26-22.md)
* [Demandez aux experts - Connexions RTCDP](exl-live-episode-06-23-22.md)
* [Demandez aux experts - Enchères de données et préparation des données](exl-live-episode-07-21-22.md)
