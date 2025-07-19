---
title: Demandez à l’expert - Bonnes pratiques pour optimiser Workfront Proof
description: Découvrez comment configurer des paramètres, activer des rapports performants et éviter les pièges courants dans Proof. Ce webinaire a été enregistré le 26 février 2020.
doc-type: feature video
team: Technical Marketing
kt: 9916
exl-id: 7d3e437d-4a6e-44b8-9eff-eabb8284c391
duration: 5182
source-git-commit: 91f20c3e9ee5ae5b259d5cb3da476974acdc6585
workflow-type: tm+mt
source-wordcount: '5572'
ht-degree: 0%

---

# Demandez à l’expert - Bonnes pratiques pour optimiser Workfront Proof

Découvrez comment configurer les paramètres de réussite, accéder aux vues (et d’autres astuces) pour activer des rapports de qualité et comprendre comment éviter les pièges courants dans Proof. Ce webinaire a été enregistré le 26 février 2020.

>[!VIDEO](https://video.tv.adobe.com/v/341122/?quality=12)

## Questions/Réponses

**Question**

Actuellement, pour permettre à un destinataire de partager un BAT qu&#39;il a partagé avec lui, vous devez cocher manuellement la case « abonnement » sous Paramètres du BAT. Envisage-t-on de faire en sorte que cette case soit cochée automatiquement par défaut ?

**Réponse**

Cette option peut être activée/désactivée par défaut pour des utilisateurs individuels par un administrateur en suivant ce chemin : PHQ Login > Account Settings > Users > Click in the User&#39;s Name > Default Proof Settings.

**Question**

Si vous ne sélectionnez pas « Nouvelle épreuve » et que vous téléchargez un document, l’utilisateur est défini sur « Générer automatiquement l’épreuve ». Pouvez-vous modifier ces paramètres une fois les fichiers chargés ?

**Réponse**

Oui. Vous pouvez ajuster tous les paramètres d’une épreuve en la sélectionnant dans l’onglet Documents , puis en cliquant sur Détails de l’épreuve.

**Question**

Cette présentation s’applique-t-elle à l’outil autonome ?

**Réponse**

Les recommandations sur les rôles de BAT, les alertes par e-mail, les options de décision, le transfert d’e-mails et le regroupement/partage/paramètres de modèle de workflow sont toutes pertinentes pour le BAT autonome.

**Question**

À quoi serviriez-vous un modèle de BAT ?

**Réponse**

Si le processus de révision du contenu de votre entreprise est souvent répété ou si le contenu est souvent révisé par les mêmes personnes, vous pouvez créer des modèles de workflow contenant ces réviseurs et réviseuses avec les rôles de BAT et les paramètres de notification que vous spécifiez.

**Question**

Qu’est-ce qu’un modèle de workflow d’épreuve ?

**Réponse**

Un modèle de workflow d’épreuve est un modèle avec un workflow de routage d’épreuve prédéterminé qui peut être appliqué aux épreuves. Ils vous permettent de normaliser et d’automatiser les processus de validation des épreuves.

**Question**

Comment créer un modèle de BAT ?

**Réponse**

En tant qu’administrateur, vous souhaiterez suivre ce chemin : PHQ Login > Workflows > Nouveau > Nouveau modèle.

**Question**

Cette fonctionnalité de partage de modèles permet-elle le partage avec des groupes et des équipes ou uniquement avec des utilisateurs individuels ?

**Réponse**

Actuellement, vous ne pouvez pas partager des modèles de workflow avec des groupes, des équipes, des fonctions ou des entreprises Workfront. Vous pouvez toutefois les partager avec des individus ainsi qu’avec des groupes de BAT. Pour créer un groupe de BAT, procédez comme suit : PHQ Login > Groups > New Group.

**Question**

Lors de l’envoi d’une épreuve (sous Organisation), existe-t-il un moyen de nettoyer les dossiers que chaque utilisateur voit afin qu’il ne voit que les dossiers qui lui sont applicables ? Au lieu de tous les dossiers qui ont été créés dans le compte d’entreprises ?

**Réponse**

Cette question concerne l’instance autonome de Workfront Proof. Dans Workfront Proof autonome, vous pouvez utiliser des dossiers privés afin de masquer les dossiers à des utilisateurs spécifiques. Cela permet de choisir parmi une liste de dossiers plus rationalisée. Notez que vous pouvez également utiliser la logique de saisie semi-automatique pour localiser le dossier auquel vous souhaitez ajouter une épreuve.

**Question**

Les réviseurs et approbateurs ont-ils la possibilité de modifier ces paramètres de notification ?

**Réponse**

Les administrateurs de Workfront ont la possibilité de modifier les paramètres par défaut des alertes par e-mail pour les utilisateurs et les contacts. Les créateurs d’épreuves peuvent ensuite modifier le paramètre de notification lors de la création d’une épreuve ainsi que sur leurs épreuves existantes.

Les destinataires des BAT peuvent toujours modifier leur alerte par e-mail pour des BAT spécifiques au niveau du BAT dans l’outil Visionneuse de BAT en sélectionnant l’Icône Paramètres dans le menu de gauche.

**Question**

Les alertes par e-mail remplacent-elles les notifications globales ?

**Réponse**

Les alertes par e-mail concernant les épreuves sont totalement indépendantes des paramètres de notification globaux.

**Question**

Si les réviseurs sont définis sur « désactivé », comment sauront-ils s’il existe une nouvelle épreuve qu’ils peuvent réviser s’ils ont rejeté une précédente ?

**Réponse**

Les alertes par e-mail ne dépendent pas de l&#39;e-mail Nouvelle épreuve, de l&#39;e-mail Nouvelle version, de l&#39;e-mail À risque, de l&#39;e-mail Tardif et de l&#39;e-mail @Mentions. Si vous choisissez « Désactivé » comme alerte par e-mail, vous désactivez simplement les notifications sur l’activité telles que les commentaires, les réponses et les décisions sur le BAT (à l’exception des e-mails de @Mention provenant de commentaires).

**Question**

Le paramètre Désactiver les e-mails est-il défini pour l’ensemble de l’entreprise ? ou est-ce par Portfolio ?

**Réponse**

Le paramètre situé dans Configuration > E-mail > Révision et approbation qui permet/désactive l’envoi d’e-mails lorsque les destinataires du BAT font des commentaires est défini à l’échelle de l’entreprise (il s’agit d’un paramètre global).

**Question**

J’ai un utilisateur « invité » qui a été ajouté à l’épreuve et qui ne peut pas l’examiner. Et l’utilisateur n’a pas accès à Workfront.

**Réponse**

Si l’invité peut accéder à l’épreuve, mais ne peut pas formuler de commentaires/prendre de décisions, veillez à vérifier son rôle dans l’épreuve. Dans ce cas, il se peut qu’ils aient été ajoutés à l’épreuve avec le rôle d’épreuve « Lecture seule ». S’ils sont configurés en tant que réviseur ou réviseur et approbateur sur l’épreuve et ne peuvent toujours pas faire de commentaires/balises/décisions, envoyez un ticket d’assistance.

**Question**

Les utilisateurs invités ont-ils besoin d’une licence ?

**Réponse**

Les utilisateurs invités n’ont pas besoin de licence.

**Question**

Je ne vois pas la boîte de décision du BAT ?

**Réponse**

Si la case de décision concernant l’épreuve ne s’affiche pas sur une épreuve, cela peut signifier que vous avez été configuré pour l’épreuve avec un rôle d’épreuve en lecture seule ou de réviseur, ou que l’étape à laquelle vous vous trouvez sur l’épreuve n’a pas encore commencé.

**Question**

Pouvez-vous clarifier le paramètre dans WF>Configuration - si vous avez la possibilité d’envoyer un e-mail pour chaque commentaire - ils sont envoyés même si l’e-mail dans PHQ est Désactivé ? et qui reçoit les e-mails ??

**Réponse**

L’option Configuration de Workfront > E-mail > Notification de révision et d’approbation est indépendante des options Alerte par e-mail au niveau du BAT. Si cette option est activée, tous les utilisateurs de chaque épreuve recevront un e-mail chaque fois qu’un utilisateur des épreuves auxquelles il appartient ajoute un commentaire.

**Question**

Auparavant, vous recommandiez « désactivé » pour les alertes par e-mail en dehors du propriétaire du BAT. Les destinataires recevront-ils toujours une notification par e-mail indiquant qu’une épreuve leur a été attribuée dans ce cas ?

**Réponse**

Oui. Les alertes par e-mail (qui peuvent être définies sur Toutes les activités, Désactivé, Décisions, etc.) sont indépendantes des e-mails de notification de BAT (Nouvelle épreuve, Nouvelle version, BAT à risque, BAT en retard, @Mentions).

**Question**

Que se passe-t-il si une personne est ajoutée à une épreuve et estime qu’elle ne devrait pas y figurer ? Est-ce que le fait de supprimer le mot « non pertinent » ne leur donnerait pas la possibilité de choisir?

**Réponse**

Il s’agit d’une bonne utilisation de l’option Décision non pertinente . Cependant, si quelqu&#39;un ne devrait pas figurer sur la preuve, je lui recommande de @Mention le propriétaire de la preuve dans un commentaire sur la preuve et de demander à être supprimé. Si une personne qui doit prendre une décision au sujet de l’épreuve rend une décision « Non pertinente » alors qu’elle doit prendre une décision Approuvée ou Modifications requises, cela peut modifier le fonctionnement du workflow appliqué à cette épreuve.

**Question**

Où puis-je trouver la case à cocher « Exiger une connexion » pour les utilisateurs invités ?

**Réponse**

Elle se trouve dans les paramètres de l’épreuve sur la page de création de l’épreuve lors de la création d’une épreuve. Si l’épreuve a déjà été créée, vous pouvez accéder à ce paramètre en sélectionnant l’épreuve dans l’onglet Documents et en cliquant sur Détails de l’épreuve > Paramètres. Notez que vous ne pouvez partager des épreuves de connexion requises qu&#39;avec des personnes qui disposent d&#39;une licence de relecture.

**Question**

Quelqu&#39;un peut-il se retirer d&#39;une épreuve s&#39;il a été ajouté par quelqu&#39;un d&#39;autre ?

**Réponse**

Si la personne dispose de droits de modification sur la preuve à laquelle elle a été ajoutée, elle peut se supprimer elle-même. Les personnes disposant de droits de modification seront des utilisateurs de Workfront disposant d’une licence de relecture au niveau de l’administrateur ou du superviseur, ainsi que des personnes ajoutées à l’épreuve avec des rôles d’épreuve d’auteur ou de modérateur. Toute autre personne devra être supprimée par une personne disposant de droits de modification.

**Question**

Pourquoi utiliser l’approbation de document plutôt que l’approbation d’épreuve ou vice versa ?

**Réponse**

L’approbation de document peut être utilisée pour un document qui ne nécessite pas de commentaires ni de balises en ligne avec le document en cours d’approbation. Par exemple, j&#39;ai juste besoin que vous examiniez ce document et que vous l&#39;approuviez ou le rejetiez. Dans Proof, les commentaires et les annotations sont autorisés dans le document dans l’outil Visionneuse d’épreuve. Par exemple, j’ai besoin que vous examiniez cette épreuve, que vous ajoutiez des commentaires, des balises et que vous preniez une décision. À l’avenir, il est prévu d’unifier les deux éléments de fonctionnalité, car ils sont très similaires.

**Question**

Nous sommes un service marketing et nous effectuons une validation interne des BAT. Nous devons ensuite l’envoyer en externe au demandeur. Nous ne donnons pas accès aux demandeurs à nos projets. Nous ne voulons pas non plus qu&#39;ils voient tous nos commentaires dans la preuve interne. Nous sommes en train de créer une nouvelle épreuve propre, de la télécharger et de l’envoyer par e-mail. Nous voulons qu&#39;ils utilisent Proof HQ, mais nous ne savons pas comment y parvenir sans leur donner également accès à notre projet. Des suggestions ?

**Réponse**

Je vous recommande d’utiliser les modèles de workflow automatisés , qui vous permettront d’utiliser les « étapes privées ». Les étapes privées vous permettent de masquer les commentaires, les balises et les décisions des réviseurs invités lors d’autres étapes. Cela permet de masquer complètement votre révision d’épreuve interne au demandeur externe.

**Question**

Une fois qu’une épreuve a été créée par quelqu’un d’autre, quel est le meilleur moyen de vous ajouter en tant que réviseur et approbateur ?

**Réponse**

Si vous êtes un utilisateur de Workfront avec l’autorisation Épreuve d’administrateur ou de superviseur, vous pouvez vous ajouter en tant que réviseur et approbateur à toute épreuve à laquelle vous avez accès. Sinon, vous souhaiterez que le propriétaire de l’épreuve (ou une autre personne disposant de droits de modification sur l’épreuve) vous ajoute.

**Question**

Nous avons essayé de baliser les utilisateurs dans une épreuve, mais ils ne reçoivent pas de notification par e-mail. Y a-t-il quelque chose dans les paramètres du compte pour s’assurer qu’un e-mail est envoyé ?

**Réponse**

Je vous recommande de vérifier le dossier Filtres d’e-mail/Spam pour voir si les notifications y ont été envoyées, puis d’effectuer les ajustements nécessaires dans l’application de messagerie pour whitelister ces e-mails. Vous pouvez également contacter notre équipe d’assistance pour obtenir de l’aide à ce sujet.

**Question**

Vous ne pouvez @ quelqu&#39;un que s&#39;il a une licence d&#39;épreuve, n&#39;est-ce pas ? Comme dans , cette personne n’a jamais fait partie de l’épreuve et vous souhaitez l’identifier (@).

**Réponse**

Si vous êtes un invité ou un utilisateur Workfront disposant d’une licence de relecture de Manager, vous pouvez @Mention toute personne qui figure dans l’épreuve (que cette personne dispose d’une licence ou non). Si vous êtes un utilisateur de Workfront avec une licence de relecture de superviseur ou d’administrateur, ou que vous êtes le propriétaire de la relecture, vous pouvez @Mention n’importe qui dans votre liste de contacts sur la plateforme de relecture.

**Question**

Problème majeur ici : adressage e-mail %2B (adresses e-mail en double). Pourquoi et comment cela se produit-il et comment peut-on y remédier ?

**Réponse**

Cela peut se produire si quelqu’un ajoute manuellement une personne à une épreuve en utilisant la mauvaise adresse e-mail. Si vous rencontrez ce problème, un administrateur peut supprimer l’adresse e-mail incorrecte du compte d’épreuve en suivant ce chemin : Connexion PHQ > Contacts > Sélectionner l’adresse e-mail/l’instance d’invité incorrecte > Supprimer. Si vous rencontrez des problèmes avec l’ajout d’utilisateurs avec des adresses e-mail en double, contactez notre équipe d’assistance.

**Question**

Une fois la décision prise, il faut remettre l&#39;épreuve en production. Quel type d’accès devez-vous accorder à l’équipe de production pour qu’elle puisse utiliser l’action du commentaire si l’épreuve est verrouillée ?

**Réponse**

Si une épreuve est verrouillée, vous devrez la déverrouiller pour que les gens puissent agir dans les commentaires ou répondre aux commentaires. Les personnes disposant des autorisations suivantes peuvent déverrouiller l’épreuve : le propriétaire de l’épreuve, les utilisateurs Workfront avec un niveau de licence de relecture d’administrateur ou de superviseur.

**Question**

Quelle est la meilleure solution pour que les équipes connaissent les BAT qui se trouvent déjà dans la file d’attente des personnes ?

**Réponse**

Vous pouvez créer un rapport Validations des épreuves dans Workfront. Vous pouvez ensuite appliquer des filtres qui n’affichent que les BAT pour des utilisateurs spécifiques qui nécessitent toujours qu’une décision soit prise.

**Question**

Existe-t-il un moyen de télécharger des épreuves avec leurs validations associées dans un dossier ?

**Réponse**

Vous pouvez accéder à un rapport de résumé d’impression et le télécharger pour vos épreuves. Ce rapport contiendra tous les commentaires, réponses, annotations, actions et décisions, quelle que soit la version.

**Question**

Lorsque vous demandez aux utilisateurs d&#39;avoir accès à Reporting ProofHQ, cela leur donnera-t-il également accès à la section sur la gauche (c&#39;est-à-dire workflows, contacts, paramètres de compte, etc) ?

**Réponse**

Cela dépendra de leur niveau de licence d&#39;épreuve. S’ils disposent de la licence Responsable ou Superviseur, ils pourront accéder aux Contacts, mais pas aux Paramètres du compte ni aux Workflows. S’ils sont configurés avec la licence d’administrateur, ils auront accès aux paramètres du compte et aux workflows.

**Question**

Dans mon entreprise, le chef de projet envoie une demande d’approbation aux parties prenantes pour examen/commentaires. Vous avez mentionné que nous ne devrions pas ajouter de noms aux champs d’approbation. En tant que Premier ministre, comment partagez-vous les preuves créatives avec les parties prenantes ?

**Réponse**

Le champ Approbation concerne les approbations de documents, ce qui est idéal si vous avez besoin d’une simple approbation de document. Si vous souhaitez une approbation d’épreuve (avec des commentaires, des balises et une décision d’épreuve), vous devez ajouter les parties prenantes à l’épreuve avec le rôle de réviseur et d’approbateur d’épreuve.

**Question**

Comment ajouter des personnes en tant que nouveaux rôles pour une épreuve déjà créée ?

**Réponse**

Pour ajouter des destinataires de BAT et sélectionner leur rôle dans un BAT existant, vous devez suivre le chemin suivant : sélectionnez le BAT dans l’onglet Documents > puis cliquez sur Détails du BAT. Lorsque la fenêtre Détails du BAT s&#39;ouvre, cliquez sur le bouton Ellipses en haut à droite de la scène et sélectionnez « Partager ». Vous pourrez ensuite ajouter les destinataires et sélectionner leur rôle de BAT et leur alerte par e-mail.

**Question**

Si nous accordons l’accès à Proof HQ aux gestionnaires/créateurs de BAT, sommes-nous en mesure de bloquer les zones d’administration telles que les workflows, les groupes, etc. ?

**Réponse**

Oui, cela est déterminé par l’autorisation Épreuve destinée aux utilisateurs. Les utilisateurs disposant de l&#39;autorisation Épreuve du responsable ou du superviseur n&#39;auront pas accès aux paramètres du compte et aux modèles de workflow. Les utilisateurs disposant de l’autorisation d’épreuve de l’administrateur auront accès aux paramètres du compte et aux modèles de workflow. Tous les utilisateurs ayant accès pourront accéder à la zone des Groupes.

**Question**

Comment les utilisateurs peuvent-ils voir toutes les épreuves qui leur sont attribuées sans être gestionnaire d’épreuves ?

**Réponse**

Si l’utilisateur souhaite afficher toutes les épreuves pour lesquelles il doit encore prendre une décision, il peut utiliser la zone Accueil ou Mes mises à jour dans Workfront (selon son niveau d’accès). Vous pouvez également créer un rapport Approbation de l’épreuve et appliquer des filtres pour afficher uniquement les épreuves pour lesquelles l’utilisateur connecté est Réviseur et approbateur.

**Question**

Bonjour, pouvez-vous passer en revue les workflows de relecture automatisée, pour les situations où il existe trois cycles de conception et de commentaires, et comment tenir compte du moment où les commentaires sont fournis tardivement, et comment cela peut-il être lié au mieux aux tâches dans WF pour chaque cycle (commentaires sur la conception et le responsable de projet) ?

**Réponse**

Vous pouvez adopter de nombreuses approches différentes pour l’utilisation des tâches avec la révision et l’approbation. Une approche que j’aime adopter consiste à avoir une tâche pour « Routage du BAT » et j’utilise le workflow du BAT pour gérer les notifications aux destinataires (au lieu de leur affecter une tâche). Vous pouvez ensuite créer une tâche pour la « deuxième ronde de routage du BAT » et la « troisième ronde de routage du BAT » qui peuvent vous aider à suivre le nombre de rondes effectuées. Vous pourrez également suivre la progression des BAT dans le tableau de bord du BAT (PHQ Login > Tableau de bord > BAT à gérer). Cette vue indique le nombre d’épreuves en retard (ainsi que les épreuves à risque) que vous gérez.

**Question**

Lorsqu’une épreuve est supprimée, une copie de cette épreuve se trouve-t-elle toujours sur vos serveurs ?

**Réponse**

Oui. Si vous supprimez une épreuve qu’elle réside dans la corbeille du compte d’épreuve associé, elle peut être restaurée à partir de là si nécessaire et y restera jusqu’à ce que la corbeille soit vidée.

**Question**

Existe-t-il un moyen de déclencher une nouvelle décision si un autre utilisateur la rejette ou l’approuve avec des modifications. c&#39;est-à-dire. Le service de relecture voit quelque chose, le chef de projet devra prendre une nouvelle décision... même s&#39;il l&#39;a déjà examinée et approuvée. (essayer de ne pas obliger le gestionnaire de projet à attendre le service de relecture pour effectuer sa révision) ?

**Réponse**

Bien que cela ne puisse pas être automatisé, vous pouvez définir le Gestionnaire de projets avec l’alerte par e-mail des décisions. Ainsi, lorsque le service de relecture prend sa décision, le chef de projet est informé de la décision qui a été prise. Il peut ensuite revenir sur le relecture, consulter les commentaires du service de relecture et modifier sa décision si nécessaire.

**Question**

Pourquoi lorsque je coche « Demander l’approbation » lorsque j’envoie une Mise à jour dans la section Détails du BAT, je ne vois que le statut SOC et non SOCD. Devrions-nous éviter d&#39;utiliser cette case à cocher ? Quelle est la bonne pratique pour envoyer une mise à jour d’une épreuve ?

**Réponse**

Lors de l’utilisation de la fonction « Demander l’approbation », vous utilisez la fonctionnalité d’approbation de document qui sera indépendante de la relecture et de la barre de progression SOCD. Si vous devez mettre à jour le rôle d’un BAT ou d’une destinatrice de BAT, vous devez suivre le chemin suivant : Dans l’onglet Documents , sélectionnez le BAT > puis cliquez sur Détails du BAT . Lorsque la fenêtre Détails du BAT s’ouvre, vous voyez la liste des destinataires et l’option Rôle du BAT (ainsi que l’alerte par e-mail) peut être ajustée en ligne. Vous pouvez ainsi (par exemple) modifier le rôle de l’épreuve de Réviseur à Réviseur et approbateur.

**Question**

Est-il possible de s’assurer que les approbateurs finaux n’ont pas accès aux versions précédentes (et aux commentaires) si elles figurent dans le même document de BAT ? Faut-il créer un nouveau document BAT ou existe-t-il un moyen de conserver toutes les versions et tous les commentaires dans un seul document et de désigner l’accès aux versions ?

**Réponse**

Dans les Paramètres du compte au sein de l’épreuve, vous pouvez contrôler l’accès de partage/visibilité à vos épreuves. Pour mettre à jour ce paramètre afin que les destinataires du BAT ne voient que les versions de BAT que vous désignez (au lieu de voir toutes les versions du BAT), vous devez suivre ce chemin : PHQ Login > Paramètres du compte > Paramètres > Partage > Les destinataires peuvent voir toutes les versions = Désactivé.

**Question**

Pouvez-vous ajouter l’écran du tableau de bord du BAT en tant que page externe à un tableau de bord WF ? Les utilisateurs non-administrateurs verront-ils le tableau de bord ?

**Réponse**

Vous pouvez ajouter le tableau de bord du BAT sous la forme d’une page externe dans un tableau de bord. Notez que cette option n’est visible que par les utilisateurs disposant d’une licence de relecture.

**Question**

Les fonctionnalités de tableau de bord et de création de rapports de ProofHQ ne sont toutefois disponibles que pour les administrateurs qui ont accès à Proof, n’est-ce pas ? Les planificateurs généraux qui n&#39;ont pas d&#39;accès administrateur ne peuvent-ils pas le faire?

**Réponse**

C&#39;est exact. Cependant, vous pouvez soumettre un cas d’assistance avec Workfront pour demander que tous les utilisateurs de votre licence de relecture aient accès au système de relecture.

**Question**

Bonjour, une question sur la flexibilité de la propriété d’une épreuve : si un nouveau chargement de la version de l’épreuve est nécessaire en l’absence du propriétaire d’origine, est-il recommandé d’ajouter un collègue au workflow en tant qu’auteur et il décidera « Non pertinent » ? (La délégation de propriété semble fonctionner uniquement pour une seule version).

**Réponse**

Ce cas d’utilisation et ce workflow fonctionneraient parfaitement. Vous pouvez également envisager, cependant, de configurer avec le niveau d’autorisation de l’épreuve du superviseur ou de l’administrateur les utilisateurs susceptibles de devoir charger de nouvelles versions dans des épreuves dont ils ne sont pas le propriétaire. Ce niveau d’autorisation leur permettra de charger de nouvelles versions dans des épreuves dont ils ne sont pas propriétaires, sans avoir à les ajouter à l’épreuve en tant qu’auteur ou modérateur (ce qui nécessiterait une décision pour les deux).

**Question**

Si j’ai bien compris, vous ne pouvez pas ajouter le même utilisateur aux étapes suivantes d’un workflow automatisé, ce qui nous pose problème. Est-ce quelque chose que vous pouvez modifier pour permettre au même utilisateur de se trouver en plusieurs étapes ?

**Réponse**

Bien que vous ne puissiez pas ajouter un destinataire d’épreuve à plusieurs étapes de révision d’une épreuve, une fois que l’étape de révision dans laquelle il se trouve est activée, il sera présent dans l’épreuve tout au long des étapes restantes pour cette version. Cela leur permettrait de continuer à commenter et à répondre aux commentaires même si d&#39;autres étapes ont commencé. Pour que cela fonctionne, veillez à ce que les étapes ne soient pas verrouillées au démarrage des nouvelles étapes.

**Question**

Pouvez-vous expliquer le routage des BAT entre les étapes ? Comment pouvez-vous en fermer une et passer à l’étape suivante ?

**Réponse**

Il existe quelques options disponibles dans les modèles de workflow automatisés qui permettront au de passer d’une étape à l’autre. Vous pouvez utiliser les options suivantes : Lors de la création de l’épreuve, Lorsque toutes les décisions sont approuvées dans une étape parent, Lorsque toutes les décisions sont approuvées ou approuvées avec des modifications dans une étape parent, Lorsque toutes les décisions sont prises dans une étape parent, etc., ainsi que d’autres options.

**Question**

Pouvez-vous supprimer une épreuve d&#39;un document qui a été généré automatiquement, mais que vous ne souhaitiez pas comme épreuve ?

**Réponse**

Si le paramètre « Générer automatiquement des épreuves lors du chargement de documents » est activé, vous ne pourrez pas supprimer une épreuve d’un document. Vous pouvez plutôt la charger à nouveau à l’aide du bouton Ajouter > Documents .

**Question**

Un utilisateur peut-il dire à l’étape 3 du flux de l’épreuve d’ajouter une autre personne en tant que Réviseur et approbateur ?

**Réponse**

Si cet utilisateur dispose de droits de modification sur l’épreuve, il peut : Les personnes disposant de droits de modification seront : le propriétaire de l&#39;épreuve, les destinataires de l&#39;épreuve ajoutés à l&#39;épreuve avec le rôle d&#39;auteur ou de modérateur de l&#39;épreuve, les utilisateurs de la licence d&#39;épreuve avec le niveau d&#39;autorisation de l&#39;épreuve de superviseur ou d&#39;administrateur.

**Question**

Si un utilisateur est désigné comme auteur, peut-il charger une nouvelle version de l’épreuve ? Il s’agit de quelqu’un d’autre que l’auteur de la preuve.

**Réponse**

Les destinataires d’épreuves avec le rôle d’auteur et de modérateur peuvent ajouter de nouvelles versions aux épreuves sur lesquelles ils se trouvent avec ce rôle d’épreuve.

**Question**

Les utilisateurs externes reçoivent un e-mail par BAT pour révision. Cela peut s’avérer difficile pour eux de suivre le statut de toutes les épreuves qu’ils ont en jeu. Existe-t-il des options de tableaux de bord, de liste de statut des e-mails ou des fonctionnalités à venir permettant aux utilisateurs externes de suivre leur statut sur plusieurs épreuves ?

**Réponse**

Je vous recommande d’ajouter ces utilisateurs externes à Workfront avec une licence de réviseur gratuite. Ils auront ainsi accès à une page Mes mises à jour qui contiendra la liste de toutes les épreuves en attente pour lesquelles une décision devra être prise.

**Question**

Pouvez-vous nous en dire plus sur les notifications Decisions ? Vais-je recevoir uniquement des notifications contenant des commentaires sur les épreuves de la part des réviseurs et des approbations ou vais-je également recevoir les commentaires des réviseurs et quand les recevrais-je ?

**Réponse**

Les notifications d’alerte par e-mail de décision ne sont envoyées que lorsque des décisions sont prises sur le BAT. Elles ne seront pas envoyées lorsque des commentaires seront faits. Cependant, si vous recevez une alerte e-mail de décision qui indique qu’un destinataire présent dans l’épreuve a pris une décision concernant les modifications requises, vous saurez que c’est le bon moment pour passer en revue les commentaires qu’il a ajoutés (qui figureront dans l’épreuve).

**Question**

En ce qui concerne le problème de transfert des e-mails, vous connectez-vous en tant que propriétaire de l’e-mail ? Cela se produirait-il dans des environnements verrouillés ? Cela se produirait-il avec un environnement SSO ?

**Réponse**

Vous serez alors connecté au BAT en tant que personne qui vous a transféré l’e-mail. L’utilisation de la connexion requise sur les épreuves et l’utilisation de la connexion unique vous empêcheront d’accéder à l’épreuve en tant que personne qui vous a transféré l’e-mail.

**Question**

Où puis-je accéder au tableau de bord et aux rapports dans la relecture ?

**Réponse**

Si une icône de case à cocher se trouve à droite de votre barre de recherche dans Workfront, cela signifie que vous disposez d’un compte Workfront et BAT intégré. En cliquant sur cette case à cocher, vous accédez à Workfront Proof et l’écran d’accueil devient le tableau de bord. Les rapports peuvent être créés à l’aide de l’option Vues dans le panneau de gauche.

**Question**

Sous la section « Rôle », deux coches en bas indiquent que vous êtes sur le point d’ajouter une personne à l’aide d’un @mention, etc. Dans les paramètres de l’épreuve, vous pouvez définir des rôles par défaut pour chaque personne, mais il n’est pas possible de cocher automatiquement ces cases, vous devez donc le faire chaque fois que vous créez une épreuve. Comment pouvez-vous en faire une valeur par défaut pour un utilisateur ?

**Réponse**

Il n’existe actuellement aucun moyen de faire de ce paramètre un paramètre par défaut pour les destinataires du BAT. Cependant, vous pouvez les enregistrer en tant que paramètres par défaut pour les destinataires dans les modèles de processus automatisés.

**Question**

Comment changer de propriétaire d’épreuve ?

**Réponse**

Pour changer le propriétaire d’une épreuve, vous devez suivre le chemin suivant : dans l’onglet Documents , sélectionnez l’épreuve et cliquez sur « Détails de l’épreuve ». L’onglet Détails du BAT s’ouvre. Si la personne que vous souhaitez rendre propriétaire de l’épreuve ne figure pas encore dans l’épreuve, vous souhaiterez l’ajouter en tant que destinataire en cliquant sur le bouton Ellipses et en sélectionnant Partager. Une fois que la personne est ajoutée au BAT (ou si elle en fait déjà partie), vous sélectionnerez son bouton Ellipses correspondant pour sélectionner « Rendre propriétaire ». Ils seront désormais les propriétaires de la preuve.

**Question**

En ce qui concerne les nouvelles versions des BAT... la seule façon dont je comprends cela est de faire un glisser-déposer du fichier au-dessus du fichier existant. Est-ce la bonne façon de le faire ?

**Réponse**

Je vous recommande de créer les nouvelles versions de la manière suivante : sélectionnez l&#39;épreuve dans l&#39;onglet Documents , puis cliquez sur le bouton Plus , choisissez Nouvelle version > Épreuve. Vous accédez alors à la page Nouvelle version qui transfère le workflow et vous permet d’effectuer les ajustements que vous devez effectuer avant d’acheminer la nouvelle version.

**Question**

Êtes-vous en mesure de désactiver les commentaires sur les BAT afin de les partager avec un client pour qu’il ne voie pas tous les commentaires internes de l’équipe ? Pour que vous n’ayez pas à générer une nouvelle épreuve.

**Réponse**

Je vous recommande d’utiliser les modèles de workflow automatisés , qui vous permettront d’utiliser les « étapes privées ». Les étapes privées vous permettent de masquer les commentaires, les balises et les décisions des réviseurs invités lors d’autres étapes. Cela permet de masquer complètement votre révision d’épreuve interne au demandeur externe.

**Question**

L’étape Workfront Proof est-elle ajoutée uniquement lorsque les workflows automatisés sont utilisés et qu’une personne non ajoutée au workflow ouvre l’épreuve ?

**Réponse**

L’étape « Workfront Proof » est ajoutée aux BAT si un non-destinataire clique dessus. Elle s’applique également si quelqu’un convertit une épreuve de workflow de base en Workfront Proof automatisée.

**Question**

Avons-nous la possibilité de configurer un workflow de BAT dans lequel plusieurs décisions peuvent être prises ?

Nous essayons de fournir des rapports à notre équipe juridique interne sur le moment où le conseiller juridique externe a terminé les examens des épreuves (combien de jours en moyenne il lui faut pour terminer son examen, qui le termine, etc.)

Nous avons commencé par ajouter une nouvelle décision au workflow de BAT appelée « Révision OC terminée » et avons pensé que nous pourrions créer un rapport pour les suivre.

Le problème est qu’il semble qu’une seule décision puisse être prise concernant le workflow.

**Réponse**

Plusieurs décisions peuvent être prises sur une épreuve (cependant, il n’y aura qu’un seul statut global sur une épreuve qui proviendra de la décision sur l’épreuve du scénario le plus défavorable) ou de la décision prise par un décideur Principal.

En raison de vos exigences de création de rapports, je vous recommande de faire en sorte que tous les membres du BAT utilisent les mêmes options de décision (Approuvé, Approuvé avec modifications, Modifications requises), puis d’utiliser les Rapports dans le Tableau de bord du BAT (Connexion PHQ > Rapports) et d’appliquer l’option de filtrage pour filtrer par destinataires (inclure les destinataires du service juridique externe dans le filtre). Vous pourrez alors voir le temps de rotation moyen sur leurs BAT.

**Question**

Une fois qu’une nouvelle version est glissée-déposée sur une épreuve existante, pourquoi TOUS les rôles changent-ils ou disparaissent-ils spécifiquement ?

**Réponse**

Lorsque vous faites glisser et déposez un document en tant que nouvelle version, vous avez raison de dire que le workflow est supprimé de la nouvelle version. Si vous souhaitez conserver le workflow de la version précédente à la version suivante, sélectionnez l’épreuve dans l’onglet Documents , puis cliquez sur le bouton Plus , choisissez Nouvelle version > Épreuve . Vous accédez alors à la page Nouvelle version qui transfère le workflow et vous permet d’effectuer les ajustements que vous devez effectuer avant d’acheminer la nouvelle version.

**Question**

Scénario - Transfert de BAT : un client externe qui examine un BAT peut vouloir le faire circuler en interne au sein de son entreprise avant d’approuver notre BAT. Les autres révisions ne seront pas nécessairement dans le système, il ne semble donc pas que le @ dans les commentaires puisse fonctionner. Comment devraient-ils procéder pour partager au mieux ? Transférez l’e-mail et indiquez au destinataire que les commentaires n’apparaîtront pas comme son nom.

**Réponse**

Il est recommandé d’utiliser la fonctionnalité Abonnements aux épreuves. Cette option peut être activée dans les paramètres du BAT et permet aux destinataires du BAT de transférer un lien public générique vers le BAT, puis de permettre aux personnes de s’abonner au BAT (en s’ajoutant essentiellement elles-mêmes).

**Question**

Quelle est la bonne pratique pour utiliser les dossiers dans des documents ?

**Réponse**

Cela dépendra de la nature du projet, mais vous pouvez envisager un dossier d’épreuves actives qui contient toutes les épreuves/versions activement acheminées et un dossier d’épreuves approuvées qui contient toutes les épreuves finalisées et approuvées. Une fois qu’une épreuve est entièrement approuvée, vous la déplacez du dossier Épreuves actives vers le dossier Épreuves approuvées.

**Question**

Si j&#39;ai 3 personnes sur un groupe d&#39;avis, puis-je établir que j&#39;ai besoin des approbations de 2 d&#39;entre eux sur les 3 ?

**Réponse**

Oui. Vous souhaiterez ajouter les deux personnes dont vous avez besoin d&#39;une décision en tant que réviseurs et approbateurs et la troisième personne en tant que réviseur.

**Question**

Nous souhaiterions envoyer un BAT à un client externe (non-utilisateur Workfront) pour examen et commentaires. Nous voulons leur envoyer un bon à tirer (en d&#39;autres termes, un bon à tirer sans commentaires internes). Quelles sont les étapes supplémentaires appropriées pour que cela se produise afin de s&#39;assurer que le client externe obtient le BAT (seulement le BAT, pas d&#39;accès au projet lui-même) et comment les clients externes nous « envoient »-ils leur BAT marqué ? Nous n’utilisons actuellement aucun modèle de BAT/workflow automatisé.

**Réponse**

Pour cela, je vous recommande d’utiliser des modèles de workflow automatisés/automatisés, car ils vous permettent d’utiliser la fonctionnalité « Étape privée ». Lors de l’utilisation de la fonctionnalité Étape privée , les commentaires/décisions et les destinataires de certaines étapes de révision peuvent rester masqués pour les personnes des autres étapes. Par exemple, vous pouvez avoir une étape interne en tant qu’étape privée et une étape client. Les clients ne pourront rien voir en rapport avec l’étape interne, alors que vous pourriez voir l’activité dans l’étape client.

**Question**

Est-il possible de conserver des utilisateurs spécifiques (ou relecteurs) à un stade précoce sans qu’ils soient reconnectés à des stades ultérieurs ?

**Réponse**

Une fois qu’une personne est ajoutée à une version d’une épreuve dans une étape, elle reste sur cette version de l’épreuve tout au long des étapes restantes. Vous avez la possibilité de verrouiller leur étape lorsque l’étape suivante commence (ou manuellement), ce qui les empêchera de faire d’autres commentaires.

**Question**

Où pouvons-nous voir la liste de toutes les personnes qui ont examiné et/ou approuvé une épreuve, un jour et une heure ? À des fins d’audit, etc. Y a-t-il également un endroit où nous pouvons voir tous les avis et approbations pour toutes les versions d’une épreuve ?

**Réponse**

Pour afficher une liste d’activités telle que la date à laquelle les commentaires et les décisions ont été pris, vous devez cliquer sur dans l’Historique des activités dans les Détails du BAT. Pour y accéder, procédez comme suit : sélectionnez le BAT dans l’onglet Documents > cliquez sur Détails du BAT > Développez la section Activité . Si vous souhaitez afficher ces informations au niveau de la version, procédez comme suit : sélectionnez le BAT dans l’onglet Documents > cliquez sur l’onglet Détails > Vers le bas de l’écran, une section Versions s’affiche. De là, vous pouvez accéder aux détails du BAT au niveau de la version.

**Question**

Pourriez-vous nous parler un peu des étapes privées de la relecture ?

**Réponse**

Lorsqu’une étape est privée, les commentaires et les décisions ne sont pas visibles pour les personnes qui ne sont pas ajoutées à cette étape ou qui ne sont pas Superviseurs, Administrateurs ou Administrateurs de facturation dans le compte. En outre, les réviseurs et réviseuses ajoutés à une étape privée ne peuvent voir que l’étape à laquelle ils sont ajoutés dans le BAT et les commentaires ajoutés à cette étape.
