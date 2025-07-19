---
title: Demandez à l’expert - Suivi des bonnes pratiques relatives à Workfront Proof
description: Découvrez pourquoi utiliser des modèles de workflow automatisés, comment les créer et comment ajuster les paramètres d’épreuve pour garantir la confidentialité. Ce webinaire a été enregistré le 4 mars 2020.
doc-type: feature video
team: Technical Marketing
kt: 9917
exl-id: 2b2f6522-2fd9-4d5e-9bc3-903c1d5e4e3b
duration: 4083
source-git-commit: 91f20c3e9ee5ae5b259d5cb3da476974acdc6585
workflow-type: tm+mt
source-wordcount: '1649'
ht-degree: 0%

---

# Demandez à l’expert - Suivi des bonnes pratiques relatives à Workfront Proof

Découvrez pourquoi utiliser des modèles de workflow automatisés, comment les créer et comment ajuster les paramètres d’épreuve pour garantir la confidentialité. Ce webinaire a été enregistré le 4 mars 2020.

>[!VIDEO](https://video.tv.adobe.com/v/341123/?quality=12)

## Questions/Réponses

**Question**

Il semble que notre instance génère automatiquement des épreuves lors du chargement de documents. Existe-t-il un moyen d’activer/désactiver cette fonction ?

**Réponse**

Oui, ce paramètre peut être désactivé dans votre profil personnel. Si vous cliquez sur Mes paramètres > Préférences, une case à cocher permettant de générer automatiquement des épreuves lors du chargement de documents peut être sélectionnée ou désélectionnée.

**Question**

Êtes-vous en mesure de créer un workflow avec des étapes vides afin de pouvoir renseigner les individus après l’avoir joint pour permettre à plusieurs équipes d’utiliser un flux ?

**Réponse**

Oui, les modèles de workflow automatisés peuvent comporter des étapes vides, de sorte que selon l’équipe qui les utilise, différents utilisateurs peuvent être ajoutés.

**Question**

Dans notre cas d’utilisation, le concepteur charge le document, mais le gestionnaire de compte génère le BAT et configure le flux de validation. Lorsqu’une nouvelle version est nécessaire, le concepteur l’ajoute en tant que document uniquement et le processus recommence. Existe-t-il un moyen de laisser le gestionnaire de compte gérer le flux de BAT et le concepteur gérer le contrôle de version sans avoir à créer le flux chaque fois que vous générez la nouvelle BAT ?

**Réponse**

Si vous configurez le Designer avec un niveau d&#39;accès de travail ou de plan dans Workfront, une licence de relecture lui sera attribuée. Si leur licence de relecture est définie sur Superviseur ou Administrateur, ils pourront créer de nouvelles versions de relecture sans avoir à demander au gestionnaire de compte de convertir la nouvelle version et d’appliquer un workflow. La nouvelle version adoptera simplement le workflow de la version précédente (et peut également être modifiée à ce stade).

**Question**

Que recommande la section « Alertes par e-mail » ? décisions ou toutes les alertes ?

**Réponse**

Je recommande que le Créateur/Propriétaire de l’épreuve soit défini sur « Décisions » pour son alerte par e-mail. Je recommande que tous les autres destinataires du BAT soient désactivés pour leur alerte par e-mail (même si l’alerte par e-mail est désactivée, ils recevront toujours les notifications Nouvelle épreuve, Nouvelle version, BAT en retard et E-mail @Mention). Cette configuration garantit que les alertes par e-mail sont ciblées et réduit au minimum le nombre d’e-mails.

**Question**

Êtes-vous en mesure de changer le propriétaire de la preuve qui est avisée lorsque les décisions sont prises? Nous avons essayé d&#39;utiliser l&#39;outil de relecture, mais nous n&#39;avons pas pu changer le propriétaire du document par rapport à la personne qui a chargé le document d&#39;origine. Exemple : un responsable marketing a téléchargé le document d’origine, mais c’était un spécialiste marketing qui était en fin de compte chargé de prendre des décisions et d’apporter des modifications.

**Réponse**

Pour modifier le propriétaire de l’épreuve, vous devez suivre le chemin suivant : Documents > Sélectionner l’épreuve > Cliquer sur « Détails de l’épreuve » > Dans la fenêtre Détails de l’épreuve , localisez le destinataire que vous souhaitez voir devenir propriétaire de l’épreuve > Cliquer sur le bouton Ellipses pour ce destinataire et choisissez « Définir comme propriétaire ».

**Question**

Y a-t-il un suivi du nombre de rondes d&#39;examen?

**Réponse**

En règle générale, les rondes de révisions correspondent au nombre de versions d’épreuve.

**Question**

Une personne peut-elle se trouver à plusieurs étapes ? En d&#39;autres termes, si nous avons un gestionnaire dans un cycle d&#39;examen précoce qui a un examen final à une étape ultérieure, comment cela fonctionnerait-il?

**Réponse**

Bien que vous ne puissiez pas ajouter un destinataire d’épreuve à plusieurs étapes de révision d’une épreuve, une fois que l’étape de révision dans laquelle il se trouve est activée, il sera présent dans l’épreuve tout au long des étapes restantes pour cette version. Cela leur permettrait de continuer à commenter et à répondre aux commentaires même si d&#39;autres étapes ont commencé. Pour que cela fonctionne, veillez à ce que les étapes ne soient pas verrouillées au début de la nouvelle étape.

**Question**

Pouvez-vous modifier des workflows existants ?

**Réponse**

Oui, vous souhaiterez accéder à Workfront Proof, puis sélectionner Workflows dans le menu de gauche. Vous pouvez y modifier des étapes, ajouter des utilisateurs, supprimer des utilisateurs, ajouter des étapes, etc.

**Question**

Y a-t-il un avantage spécifique à ce que le processus d’approbation d’un document figure sur l’épreuve plutôt que sur la tâche ? Nous l’avons configurée pour qu’elle se trouve dans la tâche de développement de document/art. Si l’art est rejeté à n’importe quelle étape du processus d’approbation, la tâche revient en action pour que le concepteur affecté la révise. De cette façon, nous n&#39;avons pas à travailler à deux endroits. Mais peut-être que je passe à côté de quelque chose d&#39;important.

**Réponse**

Dans le cas d&#39;une relecture, vous gérez le processus de validation à l&#39;aide du moteur de workflow de la relecture. Vous pouvez ainsi utiliser l’outil de révision collaborative des épreuves pour recueillir des commentaires, des annotations, des décisions et des étapes. Vous aurez la possibilité d’utiliser plusieurs déclencheurs de workflow pour acheminer l’épreuve et vous pourrez utiliser des paramètres propres aux étapes de l’épreuve, tels que le verrouillage, les étapes privées et les décideurs en matière de Principal. Vous avez également la possibilité d’attribuer des rôles de BAT uniques et des notifications par e-mail de BAT uniques. En outre, vous avez la possibilité de vérifier du contenu aussi varié que des épreuves statiques, vidéo et interactives (environ 150 types de fichiers différents).

**Question**

Qui peut définir la scène sur une scène privée ? Administrateurs uniquement ?

**Réponse**

La création du modèle est la responsabilité de l’administrateur, mais tout utilisateur pouvant créer un BAT peut rendre l’étape privée.

**Question**

L’échéance est-elle incluse dans la notification par e-mail ?

**Réponse**

Oui, si vous appliquez une date limite à un BAT, elle apparaîtra dans l’e-mail de notification.

**Question**

Pouvez-vous partager un modèle avec un groupe de BAT ?

**Réponse**

Vous pouvez toutefois noter qu’elle ne sera partagée qu’avec les membres du groupe qui disposent de licences d’épreuve. Vous ne pourrez pas partager de modèles avec des utilisateurs ou des invités de Workfront qui ne disposent pas de licences d’épreuve.

**Question**

Comment une épreuve est-elle redirigée vers son propriétaire si elle est rejetée ?

**Réponse**

Le propriétaire de l’épreuve reste sur l’épreuve à toutes les étapes des épreuves. Si l’épreuve est rejetée, l’épreuve elle-même n’a pas besoin d’être renvoyée au propriétaire. Au lieu de cela, le propriétaire de l’épreuve sera informé par e-mail de la décision prise, passera en revue les commentaires et commencera à utiliser une nouvelle version.

**Question**

Comment désactiver/masquer le document &#39;Télécharger&#39; dans Proof ?

**Réponse**

Lorsque vous ajoutez une nouvelle épreuve, vous pouvez faire défiler l’écran vers le bas jusqu’à atteindre les Paramètres de l’épreuve. Vous y verrez une case à cocher pour « Télécharger le fichier original » que vous pouvez sélectionner ou désélectionner ?

**Question**

Comment ce paramètre de confidentialité dans les paramètres du compte affecte-t-il les utilisateurs de relecture qui utilisent spécifiquement la comparaison automatisée (côte à côte avec la comparaison automatique) ? — Le paramètre par défaut sur DÉSACTIVÉ empêche-t-il le réviseur de comparer deux versions ?

**Réponse**

Pour le paramètre de partage de « Les destinataires peuvent afficher toutes les versions » : s’il est défini sur « Désactivé », si le destinataire ne se trouvait pas dans la version 1 mais dans la version 2, il ne sera pas en mesure de comparer les versions 1 et 2. Notez que les utilisateurs de Workfront avec le niveau d’autorisation Épreuve Superviseur ou Administrateur pourront voir toutes les versions, quel que soit le paramètre.

**Question**

Est-il possible que plusieurs personnes chargent une nouvelle version ? par exemple, un rédacteur charge la version 1, puis l’épreuve apparaît à l’étape 1 . Ils voient une modification qui doit être apportée, peut-on télécharger la version 2 ?

**Réponse**

Vous pouvez demander aux destinataires de l’épreuve de créer de nouvelles versions d’épreuve s’ils répondent aux critères suivants : 1) Ils sont propriétaires de l’épreuve - ou 2) Ils sont définis avec le rôle d’épreuve Auteur ou Modérateur sur l’épreuve - ou 3) Ils sont configurés avec le niveau d’autorisation de l’épreuve du superviseur ou de l’administrateur.

**Question**

Comment gérer plusieurs épreuves (par exemple, A, B et C) avec le workflow automatisé. Recommencez-vous ?

**Réponse**

Vous pouvez appliquer un modèle de workflow automatisé à plusieurs BAT au moment de la création de la version initiale des BAT. Pour ce faire, suivez le chemin suivant : Documents > Ajouter > Épreuve. Sur la page Nouvelle épreuve , sélectionnez plusieurs fichiers à charger, appliquez le modèle de workflow automatisé et créez les épreuves.

**Question**

Une épreuve peut-elle être exportée avec des commentaires dans un PDF ?

**Réponse**

Vous pouvez exporter le résumé d’impression d’une épreuve vers un fichier PDF. Il contiendra tous les commentaires, annotations, réponses et décisions.

**Question**

Où puis-je voir les paramètres du BAT ?

**Réponse**

Pour afficher les paramètres d’une épreuve existante, vous devez suivre le chemin suivant : Onglet Documents > Sélectionnez l’épreuve > Cliquez sur « Détails de l’épreuve » > Depuis la fenêtre Détails de l’épreuve qui s’ouvre, vous souhaitez développer la zone « Paramètres ».

**Question**

Pouvez-vous taguer quelqu&#39;un sur la scène privée ?

**Réponse**

Si vous êtes un destinataire de BAT dans l’étape privée, vous pourrez baliser n’importe qui dans cette étape privée. Si vous n’êtes pas à l’étape privée, vous ne pourrez pas baliser une personne à partir de l’étape privée.

**Question**

Une fois que vous avez activé une étape, êtes-vous en mesure de la désactiver ?

**Réponse**

Vous ne pourrez pas désactiver une étape active, mais vous pouvez « Verrouiller » l’étape, ce qui empêchera les personnes appartenant à l’étape de faire des commentaires et de prendre des décisions.

**Question**

Que se passe-t-il en arrière-plan lorsqu’un ou plusieurs réviseurs dans une étape indiquent que des modifications sont requises ? Qui est averti du chargement d’une nouvelle version ?

**Réponse**

Cela dépendra du paramètre « Alerte par e-mail » du créateur du BAT et/ou des destinataires du BAT sur le BAT. Je recommande que les créateurs/propriétaires d’épreuve reçoivent l’alerte par e-mail de « Décisions » afin qu’ils soient avertis par e-mail chaque fois qu’une décision est prise sur l’épreuve.
