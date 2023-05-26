---
title: Demander à l’expert - Suivi des bonnes pratiques en matière de BAT pour Workfront
description: Découvrez pourquoi vous devez utiliser des modèles de workflow automatisés, comment les créer et comment ajuster les paramètres de BAT pour garantir la confidentialité. Ce webinaire a été enregistré le 4 mars 2020.
activity: use
doc-type: feature video
team: Technical Marketing
kt: 9917
exl-id: 19d73416-80b3-41b3-98ac-6065975ed6bb
source-git-commit: ca06e5a8b1602a7bcfb83a43f529680a5a96bacf
workflow-type: tm+mt
source-wordcount: '1638'
ht-degree: 2%

---

# Demander à l’expert - Suivi des bonnes pratiques en matière de BAT pour Workfront

Découvrez pourquoi vous devez utiliser des modèles de workflow automatisés, comment les créer et comment ajuster les paramètres de BAT pour garantir la confidentialité. Ce webinaire a été enregistré le 4 mars 2020.

>[!VIDEO](https://video.tv.adobe.com/v/341123/?quality=12)

## Q&amp;R

**Question**

Il semble que notre instance génère automatiquement des bons à tirer lors du téléchargement de documents. Existe-t-il un moyen d’activer/désactiver cette fonction ?

**Réponse**

Oui, ce paramètre peut être désactivé dans votre profil personnel. Si vous cliquez sur Mes paramètres > Préférences, une case à cocher apparaît pour &quot;Générer automatiquement des bons à tirer lors du téléchargement des documents&quot;, qui peut être sélectionnée ou désélectionnée.

**Question**

Êtes-vous en mesure de créer un workflow qui comporte des étapes vides afin que vous puissiez remplir les individus après l’avoir joint pour permettre à plusieurs équipes d’utiliser un flux ?

**Réponse**

Oui, les modèles de workflow automatisés peuvent comporter des étapes vierges afin que différents utilisateurs puissent être ajoutés en fonction de l’équipe qui les utilise.

**Question**

Dans notre cas pratique, le concepteur télécharge le document mais le gestionnaire de compte génère le BAT et configure le flux de validation. Lorsqu’une nouvelle version est nécessaire, le concepteur ajoute la version en tant que document uniquement et le processus recommence. Existe-t-il un moyen de laisser le gestionnaire de compte gérer le flux de BAT et le concepteur gérer le contrôle de version sans avoir à créer le flux chaque fois que vous générez le nouveau BAT ?

**Réponse**

Si vous configurez Designer avec un niveau de travail ou un plan d’accès dans Workfront, une licence de vérification lui sera attribuée. Si leur licence de vérification est définie sur Superviseur ou Administrateur, ils pourront créer de nouvelles versions de BAT sans avoir à passer par l’étape manuelle du Gestionnaire de compte pour convertir la nouvelle version et appliquer un workflow. La nouvelle version va simplement adopter le workflow de la version précédente (et peut également être modifiée ou modifiée à l’heure actuelle).

**Question**

Que recommande la fonction &quot;Alertes par e-mail&quot; ? décisions ou toutes les alertes ?

**Réponse**

Je recommande que le Créateur/Propriétaire du BAT soit défini sur &quot;Décisions&quot; pour son alerte par e-mail. Je recommande que tous les autres destinataires du BAT soient définis sur &quot;Désactivé&quot; pour leur alerte par email (même si l’alerte par email est désactivée, ils recevront toujours les notifications Nouveau Bon à tirer, Nouvelle version, Bon à tirer et @Mention Email). Cette configuration permet de s’assurer que les alertes par e-mail sont ciblées et que les e-mails restent au minimum.

**Question**

Pouvez-vous changer le propriétaire du BAT qui est informé lorsque les décisions sont prises ? Nous avons essayé d&#39;utiliser l&#39;outil de vérification, mais nous n&#39;avons pas pu changer le propriétaire du document de la personne qui a téléchargé le document d&#39;origine. Exemple : Un responsable marketing a téléchargé le document d’origine, mais il s’agissait d’un spécialiste du marketing qui, en fin de compte, était responsable de la prise de décisions et de la prise de modifications.

**Réponse**

Pour changer le propriétaire du BAT, vous devez suivre ce chemin : Documents > Sélectionnez le Bon à tirer > Cliquez sur &quot;Détails du bon à tirer&quot; > Dans la fenêtre des détails du bon à tirer, localisez le destinataire que vous souhaitez faire appartenir au propriétaire du BAT > Cliquez sur le bouton Éliminations pour ce destinataire et sélectionnez &quot;Rendre propriétaire&quot;.

**Question**

Existe-t-il un suivi du nombre de tours d’examen ?

**Réponse**

En règle générale, les séries de révisions correspondent au nombre de versions de BAT.

**Question**

Une personne peut-elle être dans plus d&#39;une scène ? En d&#39;autres termes, si nous avons un gestionnaire dans un cycle de révision précoce qui a une révision finale à une étape ultérieure, comment pourrions-nous configurer cela ?

**Réponse**

Bien que vous ne puissiez pas ajouter un destinataire de BAT à plusieurs étapes de révision sur un BAT, une fois l’étape de révision dans laquelle il se trouve activée, il sera activé jusqu’aux étapes restantes pour cette version. Cela leur permettrait de continuer à commenter et répondre aux commentaires, même si d&#39;autres étapes ont commencé. Pour vous assurer que cela fonctionne, assurez-vous que vous n’avez pas de cadenas de scènes lorsque la nouvelle étape démarre.

**Question**

Pouvez-vous modifier des workflows existants ?

**Réponse**

Oui, vous souhaiterez accéder au BAT Workfront, puis sélectionner Workflows dans le menu de gauche. Vous pouvez y modifier des étapes, ajouter des utilisateurs, supprimer des utilisateurs, ajouter des étapes, etc.

**Question**

Le workflow de validation d&#39;un document sur le BAT et non la tâche présente-t-il un avantage spécifique ? Nous l’avons configuré pour être sur la tâche de développement de document/d’art, de sorte que si l’illustration est rejetée à n’importe quel stade du processus de validation, la tâche revient en action pour que le concepteur affecté puisse la réviser. De cette façon, nous n&#39;avons pas à travailler dans deux endroits. MAIS, peut-être que j&#39;ai oublié quelque chose d&#39;important sur cette route.

**Réponse**

Dans le cas de la validation, vous gérez le processus de validation à l&#39;aide du moteur de workflow de BAT. Vous pouvez ainsi utiliser l’outil de révision collaborative des BAT pour recueillir commentaires, commentaires, annotations, décisions et étapes. Vous aurez la possibilité d’utiliser plusieurs déclencheurs de workflow pour acheminer le BAT et vous pourrez utiliser des paramètres propres aux scènes de BAT, tels que le verrouillage, les scènes privées et les décideurs Principal. Vous avez également la possibilité d’affecter des rôles de BAT uniques et des notifications électroniques de BAT uniques. De plus, vous avez la possibilité de vérifier le contenu aussi varié que les BAT statiques, vidéo et interactifs (environ 150 types de fichiers différents).

**Question**

Qui peut mettre la scène sur une scène privée ? Administrateurs uniquement ?

**Réponse**

La création du modèle est de la responsabilité de l’administrateur, mais tout utilisateur capable de créer un BAT peut rendre l’étape privée.

**Question**

La date limite est-elle incluse dans la notification électronique ?

**Réponse**

Oui, si vous appliquez une date limite à un BAT, cela apparaîtra dans la notification par email.

**Question**

Pouvez-vous partager un modèle avec un groupe Bon à tirer ?

**Réponse**

Vous pouvez toutefois noter qu’il ne sera partagé qu’avec les membres du groupe possédant des licences de Bon à tirer. Vous ne pourrez pas partager de modèles avec des utilisateurs Workfront ou des invités qui ne disposent pas de licences de BAT.

**Question**

Comment un bon à tirer est-il renvoyé au propriétaire du BAT s&#39;il est rejeté ?

**Réponse**

Le propriétaire du BAT reste sur le BAT à travers toutes les étapes de BAT. Si le BAT est rejeté, le BAT lui-même n&#39;a pas besoin d&#39;être renvoyé au propriétaire. Au lieu de cela, le propriétaire du BAT sera informé par email de la décision prise, consultera les commentaires et commencera à utiliser une nouvelle version.

**Question**

Comment désactiver/masquer le document &quot;Télécharger&quot; dans le bon à tirer ?

**Réponse**

Lorsque vous ajoutez un nouveau BAT, vous pouvez faire défiler l’écran jusqu’à ce que vous accédiez aux Paramètres du BAT. Vous y verrez une case à cocher &quot;Télécharger le fichier d’origine&quot; que vous pouvez sélectionner ou désélectionner ?

**Question**

Comment ce paramètre de confidentialité dans les Paramètres du compte affecte-t-il les utilisateurs de vérification qui utilisent spécifiquement la comparaison automatisée (côte à côte avec la comparaison automatique) ? Est-ce que le paramètre par défaut défini sur DISabled empêche les réviseurs de comparer deux versions ?

**Réponse**

Pour le paramètre de partage &quot;Les destinataires peuvent afficher toutes les versions&quot; - s’il est défini sur &quot;Désactivé&quot;, si le destinataire n’était pas sur la version 1 mais est sur la version 2, il ne pourra pas comparer les versions 1 et 2. Notez que les utilisateurs Workfront disposant du niveau d’autorisation de BAT de l’administrateur du superviseur pourront voir toutes les versions, quel que soit le paramètre .

**Question**

Plusieurs personnes peuvent-elles télécharger une nouvelle version ? par exemple, un rédacteur charge la version 1, puis nous obtenons le correctif à l’étape 1 . Une modification doit être apportée pour le destinataire. Est-ce que la version de chargement 2 est possible ?

**Réponse**

Les destinataires du BAT peuvent créer de nouvelles versions de BAT s’ils répondent aux critères suivants : 1) Ils sont propriétaires du BAT - ou 2) Ils sont définis avec le rôle d’auteur ou de modérateur du BAT - ou 3) Ils sont configurés avec le Niveau d’autorisation de BAT du superviseur ou de l’administrateur.

**Question**

Comment gérer plusieurs bons à tirer (par exemple, A, B et C) avec le workflow automatisé. Tu recommences ?

**Réponse**

Vous pouvez appliquer un modèle de workflow automatisé à plusieurs BAT au moment de la création de la version initiale des BAT. Pour ce faire, suivez ce chemin : Documents > Ajouter nouveau > Bon à tirer. Sur la page Nouveau bon à tirer , sélectionnez plusieurs fichiers à charger, appliquez le modèle de workflow automatisé et créez les bons à tirer.

**Question**

Un BAT peut-il être exporté avec des commentaires dans un PDF ?

**Réponse**

Vous pouvez exporter un résumé d’impression sur un BAT vers un fichier de PDF. Il contiendra tous les commentaires, les annotations, les réponses et les décisions.

**Question**

Où puis-je voir les paramètres du BAT ?

**Réponse**

Pour afficher les paramètres du BAT sur un BAT existant, vous devez suivre ce chemin : Onglet Documents > Sélectionnez le Bon à tirer > Cliquez sur &quot;Détails du bon à tirer&quot; > Depuis la fenêtre Détails du bon à tirer qui s’ouvre, vous souhaiterez développer la zone &quot;Paramètres&quot;.

**Question**

Pouvez-vous marquer n&#39;importe qui sur la scène privée ?

**Réponse**

Si vous êtes un destinataire de BAT dans la scène privée, vous pourrez baliser n’importe qui dans cette scène privée. Si vous n’êtes pas dans la scène privée, vous ne pourrez pas marquer quelqu’un dans la scène privée.

**Question**

Une fois une étape activée, pouvez-vous la désactiver ?

**Réponse**

Vous ne pourrez toutefois pas désactiver une étape principale, mais vous pouvez &quot;verrouiller&quot; la scène qui empêchera les personnes de l’étape de faire des commentaires et de prendre des décisions.

**Question**

Que se passe-t-il en arrière-plan lorsque 1 ou plusieurs réviseurs d’une scène demandent des modifications ? Qui reçoit une notification pour télécharger une nouvelle version ?

**Réponse**

Cela dépendra du créateur du BAT et/ou du paramètre &quot;Alerte email&quot; des destinataires du BAT. Je recommande que les créateurs/propriétaires de BAT soient définis avec l’alerte par e-mail des &quot;décisions&quot; afin qu’ils soient avertis par e-mail chaque fois qu’une décision est prise sur le BAT.
