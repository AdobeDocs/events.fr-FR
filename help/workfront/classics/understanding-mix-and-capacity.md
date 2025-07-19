---
title: Demandez à l’expert - Comprendre la combinaison et la capacité
description: Apprenez à mesurer le mix et la capacité au sein de votre entreprise. Ce webinaire a été enregistré le 2 octobre 2019.
doc-type: feature video
team: Technical Marketing
kt: 9913
exl-id: 49cce53f-457b-4973-a0d9-1b5ce2272884
duration: 4239
source-git-commit: 91f20c3e9ee5ae5b259d5cb3da476974acdc6585
workflow-type: tm+mt
source-wordcount: '2229'
ht-degree: 0%

---

# Demandez à l’expert - Comprendre la combinaison et la capacité

Apprenez à mesurer le mix et la capacité au sein de votre entreprise. Ce webinaire a été enregistré le 2 octobre 2019.

>[!VIDEO](https://video.tv.adobe.com/v/341119/?quality=12)

## Questions/Réponses

**Question**

Comment mettre %s sur un graphique en colonnes ?

**Réponse**

Les valeurs de % répertoriées dans le rapport mixte étaient présentes, car dans l’onglet du graphique, nous avons choisi « Colonnes du groupe » et « Empilées à 100 % ». Si nous choisissions « Empilé », les totaux des heures prévues s’afficheraient, et non le pourcentage.

**Question**

Si la charge de travail de votre ministère/organisation est un mélange de projets/tâches et de problèmes/demandes, comment recommandez-vous d&#39;obtenir un examen de haut niveau (dans un rapport Workfront) d&#39;un API.

**Réponse**

Les projets, tâches et événements doivent chacun avoir leurs propres rapports avec leurs propres formulaires personnalisés. Cependant, ils peuvent tous utiliser le même champ Type de travail. Vous pouvez afficher les trois rapports dans un seul tableau de bord.

**Question**

Devons-nous modifier en bloc les tâches pour les rendre opérationnelles ou stratégiques ?

**Réponse**

La technique que nous suggérons est de créer un rapport qui vous permettra d&#39;obtenir une liste des tâches opérationnelles. Une fois que vous avez que vous pouvez sélectionner toutes les tâches en même temps, les modifier en bloc, puis joindre le formulaire personnalisé avec le type de travail et définir le type de travail sur Opérationnel pour toutes les tâches en même temps. Vous devez suivre la même procédure pour rassembler une liste de tâches stratégiques, les modifier en masse et ajouter le formulaire personnalisé, etc.

Le webinaire présente quelques idées d’invites personnalisées qui peuvent vous aider à obtenir une liste, comme la recherche de certains mots dans le nom de la tâche, le propriétaire du projet, le portfolio ou les utilisateurs affectés. Ce ne sont que des idées. Vous devez concevoir un rapport qui fonctionne le mieux dans votre situation.

**Question**

Si j’ai 4 catégories dans ma combinaison, puis-je créer un objectif pour chacune d’elles, puis générer des rapports sur les écarts entre les prévisions, les plans et les chiffres réels ? (4 catégories : Campagne, Unité opérationnelle, Web et Produit). Les catégories sont disponibles au niveau du projet dans des formulaires/champs personnalisés. L’objectif serait de créer des prévisions trimestrielles (budget/prévision), puis d’effectuer le suivi des heures prévues en vue de ces prévisions et, finalement, des heures réelles.

**Réponse**

Si toutes les catégories sont regroupées dans un champ personnalisé (appelons-le Type de travail pour l’instant), créez simplement un regroupement Rapport de projet pour les heures prévues en premier et le Type de travail en second. Filtrez le rapport de votre projet pour afficher les projets dans Planning au cours des périodes souhaitées. Utilisez un graphique avec des colonnes groupées ou des barres empilées à 100 % si vous souhaitez afficher des pourcentages. Il peut s’agir de votre rapport de prévision.

Vous pouvez copier le rapport et le modifier pour créer un rapport basé sur les projets actuels, tout en affichant la répartition en fonction des heures prévues.

Vous pouvez copier à nouveau le rapport, le modifier pour regrouper par heures réelles au lieu d&#39;heures prévues et afficher uniquement les projets terminés dans les périodes souhaitées. La répartition en pourcentage s’affiche alors en fonction des heures réelles.

**Question**

Cela fonctionnera-t-il si vous disposez de plusieurs identifiants de catégorie pour un projet ou une tâche ?

**Réponse**

Oui, si vous disposez de plusieurs identifiants, ils doivent être séparés par un onglet, comme suit :

```
EXISTS:1:$$EXISTSMOD=NOTEXISTS
EXISTS:1:$$OBJCODE=OBJCAT
EXISTS:1:categoryID=5d76d82600e7926bb51eeb1e0886810e 5d54288d01034619f2eb2c74f6472f18
EXISTS:1:objID=FIELD:ID
```

La meilleure façon de les séparer avec un caractère de tabulation est de créer d’abord votre liste de catégories dans le créateur. Insérez plusieurs noms de formulaire personnalisé et lorsque vous passez en mode texte, vous les verrez sous la forme d’identifiants séparés par des onglets.

Les différents identifiants sont traités comme des OU ; par conséquent, si l’un d’eux est associé à la tâche, il n’apparaîtra pas sur le rapport.

**Question**

Les invites du rapport sont-elles de type ANDed ou ORed ?

**Réponse**

Les invites personnalisées individuelles sont « ANDed ». Ainsi, si vous spécifiez Pam comme propriétaire du projet et Facturation comme affectée à la tâche, vous ne verrez que les tâches affectées à Facturation qui se trouvent dans des projets où Pam est propriétaire du projet.

**Question**

Pourquoi ne pouvez-vous trier que par certaines colonnes ? c’est-à-dire que vous ne pouvez pas trier par affectations.

**Réponse**

« Affectations » est une liste. Vous ne pouvez pas trier ni regrouper des éléments dans une liste. Vous pouvez uniquement trier ou regrouper un élément individuel.

Pour illustrer ce point, imaginez une liste d’affectations comme celle-ci sur une seule tâche :

```
Jane
Bill
Dan
```

Et une liste d&#39;affectations comme celle-ci sur une autre tâche :

```
Bill
Jane
Helen
```

Quelle tâche doit apparaître en premier dans un tri ? Vous pouvez dire « trier par prénom dans la liste », mais cela n’est pas nécessairement utile, car vous ne pouvez pas contrôler l’ordre. Workfront évite le problème en ne vous permettant pas du tout de trier par listes.

Que diriez-vous d&#39;un regroupement par liste ? Si nous pouvions regrouper par une liste de noms, vous verriez toutes les tâches assignées à Jane, Bill, Dan regroupées et toutes les tâches assignées à Jane, Dan, Bill (même liste, mais dans un ordre différent) dans un regroupement différent. Là encore, Workfront évite le problème en n’autorisant pas le regroupement par listes.

**Question**

Les heures prévues sont-elles utilisées pour les tâches stratégiques et les heures réelles pour les activités opérationnelles ?

**Réponse**

Non. Dans notre exemple, nous utilisons les heures prévues pour montrer le niveau d’effort prévu pour les tâches stratégiques et opérationnelles. Cela nous permet de les comparer facilement, que ce soit dans le passé, le présent ou le futur. Vous pouvez également utiliser les heures réelles pour comparer des tâches stratégiques et opérationnelles, mais uniquement pour les tâches antérieures, car les heures réelles correspondent aux heures passées réellement à travailler sur les tâches.

**Question**

Dans le planificateur de ressources, comment comptabilisons-nous les tâches planifiées dans le passé, mais non terminées ? Les heures planifiées ne semblent pas être reportées et ne s’affichent donc pas dans les semaines à venir comme des tâches/heures nécessitant des ressources.

**Réponse**

Il n’y a pas de report « automatique » des travaux non terminés. Vous devrez replanifier votre projet lorsque cela se produira. Peut-être que les ressources que vous aviez affectées à une certaine tâche ne sont pas disponibles dans le nouveau calendrier, de sorte que le gestionnaire de projet doit examiner cela et décider de la meilleure façon de replanifier. Cela peut impliquer la participation des parties prenantes et l’obtention des approbations pour les modifications du plan.

**Question**

Plutôt que de saisir 2 heures/jour pour vérifier les pauses d’e-mail, recommanderiez-vous d’ajuster leur équivalent temps complet ?

**Réponse**

Oui, si vous définissez l’équivalent temps complet sur .75, un utilisateur sera affiché comme disponible 6 heures par jour dans le Planificateur de ressources. Ce sera leur disponibilité tous les jours. Si vous souhaitez les afficher comme indisponibles pour différentes périodes en fonction de la date, par exemple indisponibles le dernier jour de chaque trimestre, un projet de frais généraux est la solution.

Certaines personnes préfèrent les projets indirects, car elles peuvent les créer elles-mêmes et les modifier quand elles le souhaitent, alors qu’elles ne disposent peut-être pas des droits de modification de leur propre équivalent temps complet.

**Question**

Les données du tableau de bord de capacité de l’équipe sont-elles disponibles pour toute personne avec laquelle vous partagez le rapport, quelles que soient les autorisations dont elle dispose sur le travail ?

**Réponse**

Si un utilisateur n’est pas autorisé à afficher l’objet, il ne sera pas visible dans le rapport/tableau de bord. Cependant, si vous souhaitez que tous les utilisateurs voient les mêmes résultats, vous pouvez accéder à Actions du rapport > Modifier > Paramètres des rapports et saisir en votre nom dans le champ « Exécuter ce rapport avec les droits d’accès de ». Cela permettra aux utilisateurs qui sont partagés sur ce rapport d’afficher les résultats exacts que vous voyez. Il ne leur accordera pas un accès supplémentaire au résultat lui-même. Par conséquent, certains résultats peuvent être cliquables ou non.

**Question**

Comment créer un rapport qui présente l&#39;ensemble du personnel affecté à un projet (et non au niveau des tâches) ?

**Réponse**

Vous pouvez créer une colonne dans un rapport de projet qui affiche tous les utilisateurs répertoriés dans le cadre de l&#39;onglet Personnel (équipe de projet). Vous souhaiterez utiliser le mode texte suivant :

```
displayname=Project Team
listdelimiter=<p>
listmethod=nested(projectUsers).lists
textmode=true
type=iterate
valuefield=user:name
valueformat=HTML
```

**Question**

Je voudrais avoir un rapport/tableau de bord qui incorpore le fonctionnement de mon équipe. En particulier les scénarios suivants : - Projets que je possède / Projets créés pour moi / Tâches que j’ai affectées à d’autres / Tâches qui me sont affectées

**Réponse**

Projets dont je suis propriétaire

Il existe un rapport intégré nommé « Projets actuels » qui affiche tous les projets actuels. Vous pouvez modifier ce projet et ajouter une règle de filtrage :Project > Identifiant du propriétaire > Égal à > $$USER.IDT. Ensuite, enregistrez et renommez le rapport en « Projets dont je suis propriétaire ».

Projets créés pour moi

Il existe un rapport intégré nommé « Mes projets » qui vous montre tous les projets actuels dont vous faites partie de l&#39;équipe du projet (ce qui signifie que vous êtes le propriétaire, le sponsor ou l&#39;affecté à la tâche). Je ne sais pas si c&#39;est ce que vous demandez, mais il n&#39;y a pas d&#39;autres moyens de savoir si quelqu&#39;un a créé un projet pour vous que de vous en faire le propriétaire, le sponsor ou l&#39;assignateur d&#39;une tâche.

Tâches que j&#39;ai affectées à d&#39;autres

Créez un rapport de tâche avec les filtres de votre choix, puis accédez à l’onglet Filtre et cliquez sur Basculer en mode texte. Ajoutez ce code à tout ce qui est déjà là :

```
EXISTS:1:$$OBJCODE=ASSGN
EXISTS:1:taskID=FIELD:ID
EXISTS:1:assignedByID=$$USER.ID
```

Toutes les tâches pour lesquelles l’utilisateur connecté a affecté au moins un des cessionnaires actuels s’affichent. Si des personnes désignées ont été affectées par plusieurs personnes, seul le nom de la première personne qui a affecté une personne apparaît comme « Demandé par » sur la page de destination de la tâche. Si vous souhaitez afficher toutes les personnes affectées et celles qui ont affecté chacune d&#39;elles, vous pouvez ajouter une colonne à votre vue, passer en mode texte et remplacer tout ce qui s&#39;y trouve par ceci :

```
displayname=All Assignees and Requesters
listdelimiter=<p>
listmethod=nested(assignments).lists
textmode=true
type=iterate
valueexpression=CONCAT("Assigned To: ",{assignedTo}.{name},"; Requested By: ",{assignedBy}.{name})
valueformat=HTML
```

Tâches qui me sont affectées

Il existe un rapport intégré nommé « Mes tâches » qui vous montre toutes les tâches incomplètes dans les projets actuels dont vous êtes le propriétaire. Je vous suggère de modifier le filtre afin de vous montrer toutes les tâches pour lesquelles vous êtes l’un des nombreux utilisateurs potentiellement affectés, et pas seulement le propriétaire de la tâche. Pour ce faire, supprimez la règle de filtrage

```
Task > Assigned To ID > Equal > $$USER.ID 
```

et le remplacer par

```
Assignment Users > ID > Equal > $$USER.ID
```

**Question**

Existe-t-il un moyen de personnaliser les libellés des graphiques ? J&#39;ai constaté que lorsque je crée un graphique pour refléter les statuts du projet, le nom du groupe principal finit par être inclus dans le libellé.

**Réponse**

Les libellés des graphiques utilisent le nom du champ sur lequel vous effectuez un regroupement. Ainsi, la seule façon de modifier les libellés consiste à utiliser un champ personnalisé calculé avec le nom de votre choix. Dans la section de calcul du champ, placez le nom du champ natif par lequel vous souhaitez effectuer un regroupement.

**Question**

Comment codez-vous les barres de rapports sur les affectations d&#39;équipe de Chuck ? C’est-à-dire ambre pour derrière, rouge pour tard et vert pour quand ? Pouvez-vous également modifier l’ordre pour qu’il soit plus logique, c’est-à-dire rouge/orange/vert ou l’inverse ?

**Réponse**

Pour modifier les couleurs utilisées dans le rapport pour les options Etat d&#39;avancement , modifiez le rapport et cliquez sur l&#39;onglet Graphique . Recherchez le menu déroulant « Couleurs personnalisées > ». Il s’affiche en regard de la zone « Axe de gauche (Y) » ou de la zone « Regrouper les données par », selon que vous choisissez de regrouper ou non les colonnes ou les barres. Dans ce menu déroulant, vous pouvez sélectionner des couleurs. Si vous cliquez sur les numéros en bas à droite des options de couleur, vous pourrez sélectionner votre couleur à partir d&#39;une palette plus grande.

Malheureusement, vous ne pouvez pas modifier l’ordre de ces éléments.

**Question**

Pouvez-vous créer un graphique qui indique le nombre de projets dans lesquels une tâche est affectée à un collaborateur ?

**Réponse**

Oui, voici comment :

* Créer un rapport de projet
* Si l’utilisateur en question est l’utilisateur connecté, le filtre doit inclure la ligne suivante :

```
   Project Users > ID > Equal >$$USER.ID 
```

* Dans le cas contraire, remplacez le nom d’utilisateur par [!DNL $$USER.ID]. Cette option affiche tous les projets pour lesquels une tâche est affectée à cette personne, ou qui en sont le propriétaire ou le sponsor. Si vous souhaitez uniquement afficher les projets auxquels des tâches sont affectées, vous devez ajouter ces deux règles de filtrage supplémentaires :

```
   Project > Owner ID > Not Equal > $$USERID
   Project > Sponsor ID > Not Equal > $$USERID
```

* Créez au moins un regroupement pour pouvoir créer un graphique. Regroupez-vous sur n&#39;importe quoi, comme une entreprise. Cliquez ensuite sur l&#39;onglet Graphique et choisissez un graphique. « Nombre d’enregistrements » sera le nombre par défaut pour un axe. Il s&#39;agit du nombre de projets dans lesquels l&#39;utilisateur a une affectation.

Lorsque l’utilisateur reçoit une affectation pour un projet (affecté à une tâche, un propriétaire de projet ou un sponsor de projet), il est ajouté à l’équipe du projet et est visible dans l’onglet Personnel sous le sous-onglet Personnes . Si un utilisateur n’est plus propriétaire du projet, ni sponsor, ni aucune affectation de tâche, son nom reste dans l’équipe du projet. Il doit être supprimé manuellement si vous le souhaitez. Gardez à l’esprit que cela peut avoir une incidence sur l’exactitude des résultats de votre rapport. Pour supprimer une personne de l&#39;équipe du projet, accédez à Personnel > Personnes, sélectionnez la ou les personnes, puis cliquez sur le bouton Supprimer qui s&#39;affiche au-dessus de la liste.

**Question**

Comment modifier l’ordre décroissant d’une colonne en mode texte (dans un regroupement) ?

**Réponse**

Vous pouvez choisir de trier la plupart des colonnes dans l’onglet Colonnes (Vue) lors de la création d’un rapport. Le rapport de liste complète sera trié si vous ne disposez d’aucun regroupement. S’il existe des regroupements, ils sont triés en fonction de ce choix au sein de chaque regroupement.

**Question**

Comment créer une colonne qui identifiera les membres de l’équipe affectés à une étape d’approbation ?

**Réponse**

Si vous exécutez un rapport de tâche ou d’événement/demande, une colonne intitulée « Approbateurs et statut » est disponible dans le Report Builder pour extraire ces informations.
