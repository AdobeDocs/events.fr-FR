---
title: Demander à l’expert - Bonnes pratiques pour optimiser le BAT Workfront
description: Découvrez comment configurer des paramètres, activer des rapports performants et éviter les pièges courants dans le Bon à tirer. Ce webinaire a été enregistré le 26 février 2020.
activity: use
doc-type: feature video
team: Technical Marketing
kt: 9916
source-git-commit: edd0bdb28a9b3d065a64a95af6a216b747577c77
workflow-type: tm+mt
source-wordcount: '5566'
ht-degree: 2%

---

# Demander à l’expert - Bonnes pratiques pour optimiser le BAT Workfront

Découvrez comment configurer les paramètres pour la réussite, accéder aux vues (et autres astuces) afin d’activer les rapports de qualité et comprendre comment éviter les pièges courants dans le Bon à tirer. Ce webinaire a été enregistré le 26 février 2020.

>[!VIDEO](https://video.tv.adobe.com/v/341122/?quality=12)

## Q&amp;R

**Question**

Actuellement, pour donner à un destinataire la possibilité de partager un BAT qui a été partagé avec lui, vous devez cocher manuellement la case &quot;abonnement&quot; sous les paramètres du BAT. Est-il prévu de faire cocher cette case automatiquement par défaut ?

**Réponse**

Cela peut être activé/désactivé par défaut pour les utilisateurs individuels par un administrateur en suivant ce chemin : Connexion via le protocole PHQ > Paramètres du compte > Utilisateurs > Cliquez sur dans le nom de l’utilisateur > Paramètres de bon à tirer par défaut.

**Question**

Si vous ne sélectionnez pas &quot;Nouveau BAT&quot; et que vous téléchargez un document, l’utilisateur est défini sur &quot;Générer automatiquement le BAT&quot;. Pouvez-vous modifier ces paramètres une fois les fichiers déjà chargés ?

**Réponse**

Oui. Vous pouvez ajuster tous les paramètres du BAT en sélectionnant le BAT dans l&#39;onglet Documents , puis en cliquant sur Détails du BAT.

**Question**

Cette présentation s’applique-t-elle à l’outil autonome ?

**Réponse**

Recommendations sur les rôles de BAT, les alertes par e-mail, les options de décision, les e-mails de transfert et le regroupement/partage/paramètres des modèles de workflow sont tous pertinents pour un BAT autonome.

**Question**

À quoi utiliseriez-vous un modèle de Bon à tirer ?

**Réponse**

Si le processus d’examen du contenu de votre entreprise est souvent répété ou si le contenu est souvent examiné par les mêmes personnes, vous pouvez créer des modèles de workflow qui contiennent les réviseurs avec les rôles de BAT et les paramètres de notification que vous spécifiez.

**Question**

Qu’est-ce qu’un modèle de workflow de BAT ?

**Réponse**

Un modèle de workflow de bon à tirer est un modèle avec un workflow de routage de BAT prédéterminé qui peut être appliqué aux bons à tirer. Ils vous permettent à la fois de normaliser et d&#39;automatiser les processus de validation du BAT.

**Question**

Comment créer un modèle de BAT ?

**Réponse**

En tant qu’administrateur, vous souhaitez suivre ce chemin : Connexion au QSP > Workflows > Nouveau > Nouveau modèle.

**Question**

Cette fonctionnalité de partage de modèles permet-elle le partage avec des groupes et des équipes ou uniquement avec des utilisateurs individuels ?

**Réponse**

Actuellement, vous ne pouvez pas partager de modèles de workflow avec des groupes Workfront, des équipes, des rôles de tâche ou des entreprises. Vous pouvez toutefois les partager avec des individus et les partager avec des groupes de BAT. Pour créer un groupe de BAT, procédez comme suit : Connexion au QSP > Groupes > Nouveau groupe.

**Question**

Lors de l’envoi d’un BAT, sous Organisation, est-il possible de nettoyer les dossiers que voit chaque utilisateur afin qu’il ne voit que les dossiers qui lui sont applicables ? Au lieu de tous les dossiers qui ont été créés dans le compte des entreprises ?

**Réponse**

Cette question est liée à Workfront Proof Standalone. Dans le BAT Workfront autonome, vous pouvez utiliser des dossiers privés afin de masquer des dossiers d’utilisateurs spécifiques. Cela permet une liste plus rationalisée de dossiers parmi lesquels choisir. Notez que vous pouvez également utiliser une logique de type anticipé pour localiser le dossier auquel vous souhaitez ajouter un BAT.

**Question**

Les réviseurs et les approbateurs ont-ils la possibilité de modifier ces paramètres de notification ?

**Réponse**

Les administrateurs de Workfront peuvent modifier les paramètres d’alerte par défaut pour les utilisateurs et les contacts. Les créateurs de BAT peuvent alors modifier le paramètre de notification lors de la création d&#39;un BAT, ainsi que sur leurs BAT existants.

Les destinataires sur BAT peuvent toujours modifier leur alerte par email pour des BAT spécifiques au niveau de l’outil Visionneuse de BAT en sélectionnant l’icône Paramètres dans le menu de gauche.

**Question**

Les alertes par e-mail remplacent-elles les notifications globales ?

**Réponse**

Les alertes par email de BAT sont totalement indépendantes des paramètres de notification globale.

**Question**

Si les réviseurs sont définis sur &quot;désactivé&quot;, comment sauront-ils s’il existe un nouveau BAT à vérifier s’ils ont rejeté un précédent ?

**Réponse**

Les alertes par e-mail sont indépendantes du nouvel e-mail de BAT, du nouvel e-mail de version, de l’e-mail à risque, de l’e-mail en retard et de l’e-mail @Mentions. Si vous choisissez &quot;Désactivé&quot; comme alerte email, vous ne pourrez que désactiver les notifications sur les activités telles que les commentaires, les réponses et les décisions sur le BAT (à l’exception des @Mention emails provenant des commentaires).

**Question**

Le paramètre de désactivation des emails est-il défini à l’échelle de l’entreprise ? ou est-ce par Portfolio ?

**Réponse**

Le paramètre situé dans Configuration > Email > Révision et approbation qui permet/désactive l’envoi des emails lorsque les destinataires du BAT font des commentaires est de type Enterprise Wide (il s’agit d’un paramètre global).

**Question**

J’ai un utilisateur &quot;invité&quot; qui a été ajouté au BAT et ne peut pas passer en revue le BAT. Et l’utilisateur n’a pas accès à Workfront.

**Réponse**

Si l’invité peut accéder au BAT, mais pas faire de commentaires/décisions, vérifiez son rôle de BAT sur le BAT. Dans ce cas, ils ont peut-être été ajoutés au BAT avec le rôle de BAT &quot;Lecture seule&quot;. S’ils sont configurés en tant que réviseur ou réviseur et approbateur sur le BAT et qu’ils ne peuvent toujours pas faire de commentaires/annotations/décisions, veuillez envoyer un ticket d’assistance.

**Question**

Les utilisateurs invités ont-ils besoin d’une licence ?

**Réponse**

Les utilisateurs invités n’ont pas besoin d’une licence .

**Question**

Je ne vois pas la boîte de décision du BAT ?

**Réponse**

Si vous ne voyez pas la boîte de décision du BAT sur un BAT, vous pouvez être configuré sur le BAT avec un rôle de BAT Lecture seule ou Réviseur, ou l’étape dans laquelle vous vous trouvez sur le BAT n’a pas encore commencé.

**Question**

Pouvez-vous clarifier le paramètre dans WF>Configuration (si vous avez la possibilité d’envoyer un email pour chaque commentaire), ces paramètres sont envoyés même si l’email dans PHQ est désactivé ? et qui reçoit les emails??

**Réponse**

L’option Configuration de Workfront > Email > Notification de révision et d’approbation est indépendante des options Alertes par email au niveau du BAT. Si cela est activé, tout le monde sur chaque BAT recevra un email chaque fois qu&#39;une personne sur les bons à tirer qu&#39;elle est en train de faire un commentaire.

**Question**

Auparavant, vous aviez recommandé &quot;désactivé&quot; pour les alertes par e-mail en dehors du propriétaire du BAT. Les destinataires recevront-ils toujours une notification par email leur indiquant qu&#39;un BAT leur a été affecté dans ce cas ?

**Réponse**

Oui. Les alertes par email (qui peuvent être définies sur Toutes les activités, Désactivées, Décisions, etc.) sont indépendantes des emails de notification de BAT (Nouveau BAT, Nouvelle version, BAT à risque, BAT tardif, @Mentions).

**Question**

Que se passe-t-il si vous avez une instance où quelqu&#39;un est ajouté à un BAT et qu&#39;il a l&#39;impression qu&#39;il ne devrait pas y être ? La suppression de &quot;Non pertinent&quot; ne leur donnerait-elle pas la possibilité de choisir ?

**Réponse**

Il s’agit d’une bonne utilisation de l’option Décision non pertinente . Cependant, si quelqu&#39;un ne doit pas être sur le BAT, je recommande qu&#39;il @Mention le propriétaire du BAT dans un commentaire sur le BAT et demande à être retiré. Si une personne qui doit prendre une décision sur le BAT prend une décision &quot;Non pertinent&quot; alors qu’elle doit prendre une décision Approuvé ou Modifications requises, cela peut modifier le fonctionnement du workflow appliqué à ce BAT.

**Question**

Où puis-je trouver la case à cocher &quot;Exiger une connexion&quot; pour les utilisateurs invités ?

**Réponse**

Elle se trouve dans les paramètres du BAT de la page de création du BAT lors de la création d’un BAT. Si le BAT a déjà été créé, vous pouvez accéder à ce paramètre en sélectionnant le BAT dans l&#39;onglet Documents et en cliquant sur Détails du BAT > Paramètres. Notez que vous ne pouvez partager les bons de connexion requis qu’avec les personnes qui disposent d’une licence de vérification.

**Question**

Quelqu&#39;un peut-il se retirer d&#39;un bon à tirer s&#39;il a été ajouté par quelqu&#39;un d&#39;autre ?

**Réponse**

Si la personne dispose de droits d’édition sur le BAT auquel elle a été ajoutée, elle peut se retirer. Les personnes disposant de droits de modification seront des utilisateurs Workfront disposant d’une licence de vérification de niveau administrateur ou superviseur, ainsi que des personnes ajoutées au BAT avec des rôles de BAT Auteur ou Modérateur. Toute autre personne devra être supprimée par une personne disposant de droits de modification.

**Question**

Pourquoi utiliser l’approbation de document plutôt que l’approbation de BAT ou vice versa ?

**Réponse**

L’approbation de document peut être utilisée pour un document qui ne nécessite pas de commentaires et d’annotations conformes au document en cours d’approbation. Par exemple, il suffit que vous regardiez ce document et que vous l&#39;approuviez ou le rejetiez. Le BAT autorise les commentaires et les annotations dans le document dans l’outil Visionneuse de BAT. Par exemple, vous devez examiner ce BAT, ajouter des commentaires, ajouter des annotations et prendre une décision. À l’avenir, le projet vise à unifier les deux fonctionnalités, car elles sont très similaires.

**Question**

Nous sommes un service marketing et nous faisons une validation interne du BAT, puis nous devons envoyer l&#39;envoi externe au demandeur. Nous ne donnons pas accès aux Demandeurs à nos projets. Nous ne voulons pas non plus qu&#39;ils voient tous nos commentaires dans la preuve interne. Maintenant, nous faisons un nouveau bon à tirer, nous le téléchargeons et nous leur envoyons un email. Nous voulons les faire utiliser le QG des BAT, mais nous ne savons pas comment y parvenir sans lui donner accès à notre projet. Des suggestions ?

**Réponse**

Je vous recommande d’utiliser des modèles de workflow automatisés qui vous permettront d’utiliser des &quot;phases privées&quot;. Les phases privées vous permettent de masquer les commentaires, les annotations et les décisions des réviseurs invités dans d’autres étapes. Cela permet à votre révision de BAT interne d’être complètement masquée du demandeur externe.

**Question**

Une fois qu’un BAT a été créé par quelqu’un d’autre, quel est le meilleur moyen de vous ajouter en tant que validant et approbateur ?

**Réponse**

Si vous êtes un utilisateur Workfront disposant de l’autorisation BAT de l’administrateur ou du superviseur, vous pouvez vous ajouter en tant que réviseur et approbateur à tout BAT auquel vous avez accès. Sinon, vous souhaiterez que le propriétaire du BAT (ou une autre personne disposant de droits d’édition sur le BAT) vous ajoute.

**Question**

Nous avons essayé de baliser les utilisateurs dans un bon à tirer, mais ils ne reçoivent pas de notification par email. Existe-t-il un élément dans les paramètres du compte pour s’assurer qu’un courrier électronique est envoyé ?

**Réponse**

Je vous recommande de vérifier Filtres d&#39;email / Dossier de spam pour voir si les notifications y sont allées, puis d&#39;effectuer les réglages nécessaires dans l&#39;application de messagerie pour placer sur la liste autorisée ces emails. Vous pouvez également contacter notre équipe d’assistance pour obtenir de l’aide à ce sujet.

**Question**

Vous ne pouvez @ quelqu&#39;un que s&#39;il a une licence de preuve, n&#39;est-ce pas ? Comme dans, cette personne n&#39;a jamais été dans le BAT et vous voulez les marquer (@).

**Réponse**

Si vous êtes un utilisateur invité ou Workfront disposant d’une licence de vérification de votre gestionnaire, vous pouvez @Mention toute personne qui se trouve sur le BAT (qu’elle dispose ou non d’une licence). Si vous êtes un utilisateur Workfront disposant d’une licence de vérification du superviseur ou que vous êtes le propriétaire du BAT, vous pouvez @Mention n’importe qui dans votre liste de contacts dans la plateforme de vérification.

**Question**

Problème le plus important ici : adresse électronique %2B (adresses électroniques en double). Pourquoi et comment cela se produit-il et comment peut-on y remédier ?

**Réponse**

Cela peut se produire si quelqu’un ajoute manuellement une personne à un BAT en utilisant la mauvaise adresse électronique. Si vous rencontrez ce problème, un administrateur peut supprimer une adresse email incorrecte du compte BAT en suivant le chemin suivant : PHQ Login > Contacts > Sélectionner l&#39;email / l&#39;instance d&#39;invité incorrecte > Supprimer. Si vous rencontrez des problèmes lors de l’ajout d’utilisateurs avec des adresses électroniques en double, contactez notre équipe d’assistance pour obtenir de l’aide.

**Question**

Une fois qu’une décision a été prise, vous devez remettre le BAT en production. Quel type d&#39;accès devez-vous donner à l&#39;équipe de production afin qu&#39;elle puisse utiliser l&#39;action du commentaire si le BAT est verrouillé ?

**Réponse**

Si un BAT est verrouillé, vous devez déverrouiller le BAT pour que les personnes puissent envoyer des commentaires d’action ou des réponses aux commentaires. Les personnes disposant des autorisations suivantes peuvent déverrouiller le BAT : Propriétaire du BAT, utilisateurs Workfront disposant d’un niveau de licence de vérification de l’administrateur ou du responsable.

**Question**

Quelle est la meilleure solution pour que les équipes connaissent les bons à tirer qui se trouvent déjà dans une file d’attente pour personnes ?

**Réponse**

Vous pouvez créer un rapport Approbations de BAT dans Workfront. Vous pouvez ensuite appliquer des filtres qui affichent uniquement les bons à tirer pour des utilisateurs spécifiques qui nécessitent encore une décision.

**Question**

Existe-t-il un moyen de télécharger les bons à tirer avec les validations associées dans un dossier ?

**Réponse**

Vous pouvez accéder et télécharger un rapport de synthèse d’impression pour vos BAT qui contiendra tous les commentaires, réponses, balises, actions et décisions dans toutes les versions.

**Question**

Lorsque les utilisateurs qui demandent l’accès à la fonction de reporting de BATHQ, cela leur donnera également accès à la section située à gauche (c.-à-d. workflows, contacts, paramètres du compte, etc.) ?

**Réponse**

Cela dépendra de leur niveau de licence de BAT. S’ils sont configurés avec la licence de responsable ou de responsable, ils pourront accéder aux contacts, mais pas aux paramètres du compte et aux workflows. S’ils sont configurés avec la licence d’administrateur, ils auront accès aux Paramètres du compte et aux workflows.

**Question**

Dans mon entreprise, le chef de projet envoie une demande d’approbation aux parties prenantes pour révision/commentaire. Vous avez mentionné que nous ne devrions pas ajouter de noms aux champs de validation, comment le Premier Ministre partage-t-il le BAT créatif aux parties prenantes ?

**Réponse**

Le champ Approbation est destiné aux validations de document, ce qui est pratique si vous avez besoin d’une simple approbation de document. Si vous souhaitez une approbation de BAT (avec commentaires, annotations et décision sur un BAT), vous souhaitez ajouter les parties prenantes au BAT avec le rôle de validant et d’approbateur.

**Question**

Comment ajouter des personnes comme nouveaux rôles sur un BAT déjà créé ?

**Réponse**

Pour ajouter des destinataires du BAT et sélectionner leur rôle de BAT sur un BAT existant, vous devez suivre le chemin suivant : Sélectionnez le BAT dans l&#39;onglet Documents > puis cliquez sur Détails du BAT. Lorsque la fenêtre des détails du BAT s&#39;ouvre, cliquez sur le bouton Éligibilité en haut à droite de l&#39;étape et sélectionnez &quot;Partager&quot;. Vous pourrez ensuite ajouter les destinataires et sélectionner leur rôle de BAT et leur alerte par email.

**Question**

Si nous accordons l’accès à Bon à tirer HQ aux responsables/créateurs de BAT, sommes-nous capables de bloquer les zones d’administration telles que les workflows, les groupes, etc. ?

**Réponse**

Oui, ceci est déterminé par l’autorisation de BAT de l’utilisateur. Les utilisateurs disposant de l’autorisation de BAT d’un responsable ou d’un superviseur n’auront pas accès aux paramètres du compte et aux modèles de workflow. Les utilisateurs disposant de l’autorisation BAT de l’administrateur auront accès aux paramètres du compte et aux modèles de workflow. Tous les utilisateurs disposant d’un accès pourront accéder à la zone Groupes .

**Question**

Comment les utilisateurs peuvent-ils voir tous les bons à tirer auxquels ils sont affectés sans être responsables des BAT ?

**Réponse**

Si un utilisateur souhaite voir tous les bons à tirer sur lesquels il doit encore prendre une décision, il pourra utiliser la zone Accueil ou Mes mises à jour dans Workfront (en fonction de son niveau d’accès). Vous pouvez également créer un rapport d’approbation de BAT et appliquer des filtres pour afficher uniquement les bons à tirer indiquant que l’utilisateur connecté est un réviseur et un approbateur activé.

**Question**

Bonjour, pouvez-vous passer en revue les workflows de vérification automatisée, dans les situations où il y a 3 séries de plans et de commentaires et comment vous adapter lorsque les commentaires sont fournis en retard, et comment cela peut être le mieux lié aux tâches dans WF pour chaque série (commentaires de conception et de chef de projet) ?

**Réponse**

Bien que vous puissiez adopter de nombreuses approches différentes pour utiliser les tâches avec la fonction Révision et approbation. Une approche que j’aime adopter est d’avoir une tâche pour &quot;Routage des BAT&quot; et j’utilise le workflow de BAT pour gérer les notifications aux destinataires (au lieu de leur affecter une tâche). Vous pouvez ensuite créer une tâche pour &quot;Routage des BAT 2e&quot; et &quot;Routage des BAT 3e&quot; qui peut vous aider à suivre le nombre de tours qui ont été parcourues. Vous pourrez également suivre l&#39;avancement des BAT à l&#39;aide du Tableau de bord des BAT (Connexion PHQ > Tableau de bord > Bons à tirer à gérer). Cette vue indique le nombre de bons à tirer tardifs (ainsi que les bons à tirer à risque) que vous gérez.

**Question**

Lorsqu’un BAT est supprimé, est-ce qu’une copie de ce BAT est toujours sur vos serveurs ?

**Réponse**

Oui. Si vous supprimez un BAT qui se trouve dans la zone Corbeille du compte BAT associé, il peut être restauré à partir de cet emplacement si nécessaire et y restera jusqu’à ce que la corbeille soit vidée.

**Question**

Existe-t-il un moyen de déclencher une nouvelle décision si un autre utilisateur rejette ou approuve les modifications ? ie. Le service de vérification voit quelque chose, le chef de projet devra prendre une nouvelle décision... même s&#39;il l&#39;a déjà examiné et l&#39;a approuvé. (en essayant de ne pas obliger le gestionnaire de proj à attendre le délai de relecture pour faire sa révision) ?

**Réponse**

Bien qu’il ne soit pas possible d’automatiser cette opération, vous pouvez définir le gestionnaire de projet avec l’alerte par courrier électronique des décisions. Ainsi, lorsque le service de relecture prendra sa décision, le chef de projet sera informé de la décision qui a été prise et pourra ensuite revenir dans le BAT, examiner les commentaires effectués par le service de relecture, puis modifier sa décision si nécessaire.

**Question**

Pourquoi lorsque je coche &quot;Demander l’approbation&quot; lorsque j’envoie une mise à jour dans la section Détails du bon à tirer, je ne vois que le statut SOC et non SOCD. Devrions-nous éviter d’utiliser cette case à cocher ? La bonne pratique pour envoyer une mise à jour sur un BAT.

**Réponse**

Lors de l’utilisation de la fonction &quot;Demander l’approbation&quot;, vous travaillez avec la fonctionnalité Approbation du document qui sera indépendante de la vérification et de la barre de progression de SOCD. Si vous devez mettre à jour le rôle de BAT d’un destinataire de BAT, vous devez suivre ce chemin : Dans l&#39;onglet Documents, sélectionnez le BAT, puis cliquez sur Détails du BAT. Lorsque la fenêtre des détails du BAT s&#39;ouvre, la liste des destinataires et l&#39;option du rôle du BAT (ainsi que l&#39;option Alerte email) peuvent être ajustées en ligne. Cela vous permet (par exemple) de remplacer le rôle de BAT de Réviseur par Réviseur et Approbateur.

**Question**

Est-il possible de s’assurer que les approbateurs finaux n’ont pas accès aux versions précédentes (et aux commentaires) si le même document de BAT figure ? Un nouveau document de BAT doit-il être créé ou existe-t-il un moyen de conserver toutes les versions et tous les commentaires dans un seul et de désigner l’accès aux versions ?

**Réponse**

Dans les Paramètres du compte au sein du BAT, vous pouvez contrôler le partage/l’accès à la visibilité de vos BAT. Pour mettre à jour ce paramètre afin que les destinataires du BAT ne voient que les versions de BAT que vous désignez (au lieu de voir toutes les versions du BAT), vous devez suivre ce chemin : PHQ Login > Paramètres du compte > Partage > Les destinataires peuvent afficher toutes les versions = Désactivé.

**Question**

Pouvez-vous ajouter l’écran du tableau de bord du BAT en tant que page externe au tableau de bord du flux de travail ? Les non-administrateurs verront-ils le tableau de bord ?

**Réponse**

Vous pouvez ajouter le tableau de bord du BAT en tant que page externe dans un tableau de bord. Notez que cela ne serait visible que par les utilisateurs disposant d’une licence de vérification.

**Question**

Les fonctions Tableau de bord et Création de rapports dans ProofHQ ne sont disponibles que pour les administrateurs qui ont accès au Bon à tirer, cependant. Les planificateurs généraux n’ont-ils pas accès en tant qu’administrateur ?

**Réponse**

C&#39;est exact. Bien que vous puissiez soumettre un cas d’assistance avec Workfront pour demander à tous les utilisateurs de votre licence de vérification d’accès au système de BAT.

**Question**

Bonjour, une question sur la flexibilité de la propriété des BAT : Si un nouveau téléchargement de version de Bon à tirer est requis en l’absence du propriétaire d’origine, est-il recommandé pour eux d’ajouter un collègue au workflow en tant qu’auteur et ils décideront &quot;Non pertinent&quot; ? (La délégation de la propriété ne semble fonctionner que pour une seule version).

**Réponse**

Ce cas pratique et ce workflow fonctionneraient parfaitement. Une autre chose que vous pouvez considérer, c&#39;est que les utilisateurs qui peuvent avoir besoin de télécharger de nouvelles versions sur des bons à tirer qui ne sont pas le propriétaire soient configurés avec le niveau d&#39;autorisation de BAT du superviseur ou de l&#39;administrateur. Ce niveau d’autorisation leur permet de charger de nouvelles versions sur des bons à tirer dont ils ne sont pas propriétaires sans avoir à les ajouter au BAT en tant qu’auteur ou modérateur (ce qui nécessiterait tous deux une décision).

**Question**

Si je comprends bien, vous ne pouvez pas ajouter le même utilisateur aux étapes suivantes d’un workflow automatisé, ce qui nous pose problème. Est-ce quelque chose que vous pouvez modifier pour permettre à un même utilisateur d’être en plusieurs étapes ?

**Réponse**

Bien que vous ne puissiez pas ajouter un destinataire de BAT à plusieurs étapes de révision sur un BAT, une fois l’étape de révision dans laquelle il se trouve activée, il sera activé jusqu’aux étapes restantes pour cette version. Cela leur permettrait de continuer à commenter et répondre aux commentaires, même si d&#39;autres étapes ont commencé. La clé pour vous assurer que cela fonctionne est de vous assurer que vous n’avez pas de verrouillage des scènes lorsque de nouvelles scènes démarrent.

**Question**

Pouvez-vous expliquer le routage des BAT entre les étapes ? Comment fermer l’un d’eux et passer à l’étape suivante ?

**Réponse**

Il existe quelques options disponibles dans les modèles de workflow automatisés qui permettront au de passer d’une étape à l’autre. Les options que vous pouvez utiliser sont &quot;Lors de la création du BAT&quot;, &quot;Lorsque toutes les décisions sont approuvées dans une étape parent&quot;, &quot;Lorsque toutes les décisions sont approuvées ou approuvées avec des modifications dans une étape parent&quot;, &quot;Lorsque toutes les décisions sont prises dans une étape parent&quot;, ainsi que certaines autres options.

**Question**

Pouvez-vous supprimer un BAT d’un document généré automatiquement, mais vous ne vouliez pas qu’il soit un BAT ?

**Réponse**

Si le paramètre &quot;Générer automatiquement les bons à tirer lors du téléchargement des documents&quot; est activé, vous ne pourrez pas supprimer un bon à tirer d’un document. Vous souhaiterez le télécharger à nouveau via le bouton Ajouter > Documents .

**Question**

Un utilisateur peut-il indiquer à l’étape 3 du flux du BAT qu’il ajoute une autre personne en tant que Révision et approbateur ?

**Réponse**

Si cet utilisateur dispose des droits d’édition sur le BAT, il peut le faire. Les personnes disposant de droits de modification seront : Propriétaire du BAT, destinataires du BAT ajoutés au BAT avec le rôle de BAT de l’auteur ou du modérateur, utilisateurs de la licence du BAT avec le niveau d’autorisation du superviseur Niveau d’autorisation du BAT.

**Question**

Si un utilisateur est désigné comme auteur, peut-il télécharger une nouvelle version du BAT ? Ce serait quelqu&#39;un d&#39;autre que l&#39;émetteur du BAT.

**Réponse**

Les destinataires du BAT avec le rôle de BAT Auteur et Modérateur peuvent ajouter de nouvelles versions aux BAT sur lesquels ils se trouvent avec ce rôle de BAT.

**Question**

Les utilisateurs externes reçoivent un email par BAT pour révision. Cela peut être difficile pour eux de suivre l’état de tous les bons à tirer qu’ils ont en jeu. Existe-t-il des tableaux de bord ou des options de liste d’état d’email ou des fonctionnalités à venir permettant aux utilisateurs externes de suivre leur état sur plusieurs bons à tirer ?

**Réponse**

Je vous recommande d’ajouter ces utilisateurs externes à Workfront avec une licence de réviseur gratuite. Cela leur donnera accès à une page Mes mises à jour qui contiendra la liste de tous les bons à tirer restants pour prendre une décision.

**Question**

Pouvez-vous expliquer plus en détail les notifications Decisions ? Est-ce que je n’obtiendrai des notifications qu’avec les commentaires du BAT des réviseurs et des approbations ou est-ce que je recevrai également les commentaires des réviseurs et quand les recevoir ?

**Réponse**

Les notifications d’alerte par courrier électronique de décision ne sont envoyées que lorsque des décisions sont prises sur le BAT. Ils ne seront pas envoyés lorsque des commentaires seront faits. Cependant, si vous recevez une alerte par e-mail de décision qui indique qu’un destinataire sur le BAT a pris la décision de Modifications requises, vous savez que c’est le bon moment pour examiner les commentaires qu’il a ajoutés (qui seront dans le BAT).

**Question**

En ce qui concerne le transfert des emails, vous connectez-vous en tant que propriétaire de l&#39;email ? Et cela se produirait-il avec des environnements verrouillés ? Cela se produirait-il avec un environnement d&#39;authentification unique ?

**Réponse**

Cela vous connecterait au BAT en tant que personne qui vous a transféré l&#39;email. L’utilisation de la connexion requise sur les bons à tirer et de l’authentification unique vous empêchera d’accéder au BAT en tant que personne qui vous a transféré l’email.

**Question**

Où puis-je accéder au tableau de bord et aux rapports dans la vérification ?

**Réponse**

Si vous disposez d’une icône de case à cocher à droite de votre barre de recherche dans Workfront, cela signifie que vous disposez d’un compte Workfront et BAT intégré. Lorsque vous cochez cette case, vous accédez au bon à tirer Workfront et l’écran d’accueil s’affiche dans le tableau de bord. Les rapports peuvent être créés à l’aide de l’option Vues du panneau de gauche.

**Question**

Dans la section &quot;Rôle&quot;, il y a 2 coches en bas qui indiquent être sur le point d’ajouter quelqu’un à l’aide d’un @mention, etc. Dans les paramètres de BAT, vous pouvez définir des rôles par défaut pour chaque personne, mais il n’existe pas d’option pour que ces coches soient automatiquement cochées. Vous devez donc le faire chaque fois que vous créez un BAT. Comment pouvez-vous en faire une valeur par défaut pour un utilisateur ?

**Réponse**

Il n’existe actuellement aucun moyen de faire de ce paramètre un paramètre par défaut pour les destinataires du BAT. Cependant, vous pouvez enregistrer ces paramètres comme paramètres par défaut pour les destinataires dans les modèles de workflow automatisés.

**Question**

Comment changer de propriétaire de BAT ?

**Réponse**

Pour changer de propriétaire d’un BAT, vous devez suivre le chemin suivant : Dans l&#39;onglet Documents, sélectionnez le BAT et cliquez sur &quot;Détails du BAT&quot;. L’onglet Détails du BAT s’ouvre. Si la personne que vous souhaitez rendre propriétaire du BAT ne figure pas encore sur le BAT, vous souhaiterez l’ajouter en tant que destinataire en cliquant sur le bouton Élipses et en sélectionnant Partager. Une fois la personne ajoutée au BAT (ou si elle est déjà sur le BAT), vous allez sélectionner le bouton Élipements correspondant pour sélectionner &quot;Rendre propriétaire&quot;. Ils seront désormais propriétaires du BAT.

**Question**

En termes de nouvelles versions de BAT... la seule façon pour moi de le faire est de faire glisser le fichier au-dessus du fichier existant. Est-ce la bonne manière de le faire ?

**Réponse**

Je vous recommande de créer de nouvelles versions de la manière suivante : sélectionnez le BAT dans l&#39;onglet Documents , puis cliquez sur le bouton Plus , choisissez Nouvelle version > Bon à tirer . Vous accédez alors à la page Nouvelle version qui transfère le workflow et vous permet d’effectuer les ajustements nécessaires avant de router la nouvelle version.

**Question**

Pouvez-vous désactiver les commentaires sur les bons à tirer pour les partager avec un client afin qu’il ne voie pas tous les commentaires internes de l’équipe ? Pour qu&#39;il n&#39;y ait pas à regénérer une nouvelle preuve.

**Réponse**

Je vous recommande d’utiliser des modèles de workflow automatisés qui vous permettront d’utiliser des &quot;phases privées&quot;. Les phases privées vous permettent de masquer les commentaires, les annotations et les décisions des réviseurs invités dans d’autres étapes. Cela permet à votre révision de BAT interne d’être complètement masquée du demandeur externe.

**Question**

L’étape Bon à tirer de Workfront n’est-elle ajoutée que lors de l’utilisation de workflows automatisés et une personne qui n’a pas été ajoutée au workflow ouvre-t-elle le BAT ?

**Réponse**

L&#39;étape &quot;Bon à tirer Workfront&quot; sera ajoutée aux bons à tirer si un non-destinataire clique dans le BAT. Elle sera également appliquée si quelqu’un convertit un BAT de workflow de base en BAT Workfront automatisé.

**Question**

Avons-nous la possibilité de configurer un workflow de BAT dans lequel plusieurs décisions peuvent être prises ?

Nous essayons de fournir des rapports à notre équipe juridique interne sur le moment où un service juridique externe a terminé les révisions sur les bons à tirer (combien de jours en moyenne leur faut-il pour terminer leur examen, qui l&#39;a terminé, etc.)

Nous avons commencé par ajouter une nouvelle décision au workflow de BAT appelé &quot;Fin de la révision des OC&quot;, et nous avons pensé que nous pourrions assembler un rapport pour en effectuer le suivi.

Le problème est qu’il semble qu’une seule décision peut être prise sur le workflow.

**Réponse**

Plusieurs décisions peuvent être prises sur un BAT, mais il n’y aura qu’un seul statut global sur un BAT qui viendra du scénario le plus mauvais de la décision sur le BAT, ou de la décision prise par un décideur Principal.

En raison de vos exigences de création de rapports, je vous recommande de faire en sorte que tous les membres du BAT utilisent les mêmes options de décision (Approuvé, Approuvé avec des modifications, Modifications requises), puis utilisent les Rapports dans le tableau de bord du BAT (Connexion PHQ > Rapports) et appliquent l’option de filtrage par destinataires (inclure les destinataires du service juridique extérieur dans le filtre), afin de pouvoir voir le temps de rotation moyen sur leurs BAT.

**Question**

Une fois qu’une nouvelle version est glissée et déposée sur un BAT existant, pourquoi TOUS les rôles changent-ils ou disparaissent-ils spécifiquement ?

**Réponse**

Lorsque vous faites glisser un document comme nouvelle version, vous avez raison de dire que le workflow est supprimé de la nouvelle version. Si vous souhaitez conserver le workflow de la version précédente à la version suivante, sélectionnez le BAT dans l&#39;onglet Documents, puis cliquez sur le bouton Plus, choisissez Nouvelle version > Bon à tirer. Vous accédez alors à la page Nouvelle version qui transfère le workflow et vous permet d’effectuer les ajustements nécessaires avant de router la nouvelle version.

**Question**

Scénario - Transfert de BAT : Un client externe qui examine un BAT peut vouloir circuler en interne dans son organisation avant d’approuver notre BAT. Les autres révisions ne seront pas nécessairement dans le système, donc il ne semble pas @ dans les commentaires fonctionneraient. Comment doivent-ils partager au mieux : transférer l&#39;email et indiquer au destinataire que les commentaires n&#39;apparaîtront pas comme leur nom ?

**Réponse**

Vous souhaitez utiliser la fonctionnalité BAT - Abonnements . Cela peut être activé dans les paramètres du BAT et permettre aux destinataires du BAT de transférer un lien public générique vers le BAT, puis de permettre aux personnes de s&#39;abonner au BAT (essentiellement en s&#39;ajoutant elles-mêmes).

**Question**

Quelle est la bonne pratique pour utiliser des dossiers dans des documents ?

**Réponse**

Cela dépendra de la nature du projet, mais vous pouvez considérer un dossier BAT Principal qui contient tous les bons à tirer/versions activement routés et un dossier BAT approuvé contenant tous les bons à tirer finalisés et approuvés. Une fois qu&#39;un BAT est entièrement validé, vous le déplacez du dossier BAT Principal vers le dossier Bons à tirer approuvés.

**Question**

Si j&#39;ai 3 personnes sur un groupe de critiques, puis-je définir que j&#39;ai besoin d&#39;une approbation de 2 d&#39;entre elles sur 3 ?

**Réponse**

Oui. Vous souhaiterez ajouter les deux personnes pour lesquelles vous avez besoin d’une décision en tant que réviseurs et approbateurs et la troisième personne en tant que réviseur.

**Question**

Nous souhaitons envoyer un BAT à un client externe (utilisateur non Workfront) pour révision et commentaire. Nous voulons leur envoyer un bon à tirer (en d&#39;autres termes, sans commentaires internes). Quelles sont les bonnes étapes de réalisation pour s&#39;assurer que le client externe reçoit le BAT (juste le BAT, pas d&#39;accès au projet lui-même) et comment les clients externes &quot;nous renvoient&quot;-ils leur BAT marqué ? Actuellement, nous n’utilisons pas de modèles de BAT/workflows automatisés.

**Réponse**

Il est recommandé d’utiliser des modèles de workflow automatisés/automatisés pour cela, car cela vous permettra d’utiliser la fonctionnalité &quot;Etape privée&quot;. Lors de l’utilisation de la fonctionnalité d’évaluation privée, les commentaires/décisions et les destinataires de certaines étapes de révision peuvent rester masqués aux personnes d’autres étapes. Par exemple, vous pouvez avoir une étape interne en tant qu’étape privée et une étape client. Les clients ne verront rien à voir avec l’étape interne, tandis que vous pourrez voir l’activité dans l’étape client.

**Question**

Est-il possible de garder des utilisateurs spécifiques (ou proofreader) à une étape précoce sans qu’ils ne soient bouclés ultérieurement ?

**Réponse**

Une fois que quelqu&#39;un est ajouté à une version d&#39;un BAT dans une étape, il reste sur cette version du BAT jusqu&#39;aux étapes restantes. Vous avez la possibilité de verrouiller leur scène lorsque la prochaine étape commence (ou manuellement), ce qui les empêchera d’effectuer d’autres commentaires.

**Question**

Où pouvons-nous voir une liste de toutes les personnes qui ont examiné et/ou approuvé un BAT, un jour et à quelle heure ? À des fins d’audit, etc. Y a-t-il aussi un endroit où nous pouvons voir toutes les révisions et approbations pour toutes les versions d&#39;un BAT ?

**Réponse**

Pour afficher une liste d’activités, telle que le moment où des commentaires et des décisions ont été pris, vous souhaiterez cliquer sur dans l’ historique des activités dans les détails du BAT. Pour y accéder, suivez ce chemin : Sélectionnez le Bon à tirer dans l&#39;onglet Documents > Cliquez sur Détails du bon à tirer > Développez la section Activité . Si vous souhaitez afficher ces informations au niveau de la version, suivez ce chemin : Sélectionnez le Bon à tirer dans l’onglet Documents > Cliquez sur l’onglet Détails > Une section Versions s’affiche en bas de l’écran. Vous pouvez y accéder aux détails du BAT au niveau de la version.

**Question**

Pouvez-vous parler un peu des scènes privées dans l&#39;examen.

**Réponse**

Lorsqu’une étape est rendue privée, les commentaires et les décisions ne sont pas visibles par les personnes qui ne sont pas ajoutées à cette étape ou qui ne sont pas superviseurs, administrateurs ou administrateurs de facturation dans le compte. En outre, les réviseurs qui sont ajoutés à une étape privée ne peuvent voir que l’étape à laquelle ils sont ajoutés sur le BAT et les commentaires effectués à cette étape.
