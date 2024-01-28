---
title: Poser des questions à l’expert - Comprendre le mélange et la capacité
description: Découvrez comment mesurer la combinaison et la capacité au sein de votre entreprise. Ce webinaire a été enregistré le 2 octobre 2019.
doc-type: feature video
team: Technical Marketing
kt: 9913
exl-id: 49cce53f-457b-4973-a0d9-1b5ce2272884
duration: 4239
source-git-commit: 9a297cda953d4414131657f9ac84580aea0eabeb
workflow-type: tm+mt
source-wordcount: '2230'
ht-degree: 0%

---

# Poser des questions à l’expert - Comprendre le mélange et la capacité

Découvrez comment mesurer la combinaison et la capacité au sein de votre entreprise. Ce webinaire a été enregistré le 2 octobre 2019.

>[!VIDEO](https://video.tv.adobe.com/v/341119/?quality=12)

## Q&amp;R

**Question**

Comment positionner %s sur un graphique en colonnes ?

**Réponse**

Les valeurs % répertoriées dans le rapport de combinaison étaient présentes car, dans l’onglet du graphique, nous avons choisi &quot;Colonnes de groupe&quot; et &quot;Empilé à 100 %&quot;. Si nous choisissons &quot;Empilé&quot;, les totaux des heures planifiées s’affichent et non le pourcentage.

**Question**

Si la charge de travail de votre service/entreprise est un mélange de projets/tâches, de problèmes/requêtes, comment recommander une révision de haut niveau (dans un rapport Workfront) d’un WPI.

**Réponse**

Les projets, tâches et problèmes doivent chacun avoir leurs propres rapports avec leurs propres formulaires personnalisés. Ils peuvent toutefois utiliser le même champ Type de travail. Vous pouvez afficher les trois rapports dans un seul tableau de bord.

**Question**

Devons-nous modifier les tâches en masse pour les rendre opérationnelles ou stratégiques ?

**Réponse**

La technique que nous suggérons est de créer un rapport qui vous permettra d’obtenir la liste des tâches opérationnelles. Une fois que vous avez la possibilité de sélectionner toutes les tâches en même temps, modifiez-les en bloc, puis joignez le formulaire personnalisé à l’aide de l’option Type de travail et définissez le type de travail sur Opérationnel pour toutes les tâches en même temps. Vous devez suivre la même procédure pour rassembler une liste de tâches stratégiques, les éditer en masse et ajouter le formulaire personnalisé, etc.

Quelques idées sont mentionnées dans le webinaire pour des invites personnalisées qui peuvent vous aider à obtenir une liste, comme la vérification de certains mots dans le nom de la tâche, le propriétaire du projet, le portefeuille ou les utilisateurs affectés. Ce ne sont que des idées. Vous devez concevoir un rapport qui fonctionne le mieux dans votre situation.

**Question**

Si je dispose de 4 catégories, puis-je créer un objectif pour chacune d’elles, puis générer un rapport sur les différences entre les prévisions et les plans et les faits ? (4 catégories : Campaign, unité opérationnelle, web et produit). Nous avons les catégories au niveau du projet dans un ou plusieurs champs personnalisés. L’objectif serait de créer une prévision trimestrielle (budget/prévision), puis de suivre les heures prévues jusqu’à ce niveau et, au final, les chiffres réels.

**Réponse**

Si vous avez toutes les catégories dans un champ personnalisé (appelons-le Type de travail pour l’instant), créez un groupe de rapports de projet sur Heures planifiées en premier et Type de travail en second. Filtrez le rapport de projet pour afficher les projets dans Planification au cours des périodes souhaitées. Utilisez un graphique avec des colonnes ou des barres groupées empilées à 100 % si vous souhaitez afficher des pourcentages. Il peut s’agir de votre rapport de prévision.

Vous pouvez copier le rapport et le modifier pour créer un rapport basé sur les projets en cours, tout en affichant le mélange selon les heures planifiées.

Vous pouvez copier à nouveau le rapport, le regrouper par Heures réelles au lieu des Heures planifiées et afficher uniquement les projets terminés dans les plages de dates souhaitées. Cela montrerait le pourcentage de mélange en fonction des heures réelles.

**Question**

Cela fonctionnera-t-il si vous disposez de plusieurs ID de catégorie sur un projet ou une tâche ?

**Réponse**

Oui, si vous disposez de plusieurs identifiants, ils doivent être séparés par un onglet, comme ceci :

```
EXISTS:1:$$EXISTSMOD=NOTEXISTS
EXISTS:1:$$OBJCODE=OBJCAT
EXISTS:1:categoryID=5d76d82600e7926bb51eeb1e0886810e 5d54288d01034619f2eb2c74f6472f18
EXISTS:1:objID=FIELD:ID
```

La meilleure façon de les séparer avec un caractère de tabulation consiste à créer d’abord votre liste de catégories dans le créateur. Insérez plusieurs noms de formulaire personnalisés. Lorsque vous passez en mode texte, ils s’affichent sous la forme d’identifiants séparés par des onglets.

Les différents identifiants sont traités comme des OR. Par conséquent, si l’un d’eux est associé à la tâche, il n’apparaîtra pas sur le rapport.

**Question**

Le rapport est-il affiché sous la forme &quot;ANDed&quot; ou &quot;ORed&quot; ?

**Réponse**

Les invites personnalisées individuelles sont &quot;ANDed&quot;. Ainsi, si vous spécifiez Pam comme propriétaire du projet et Bill comme affecté à la tâche, seules les tâches affectées à Bill se trouvent dans les projets où Pam est le propriétaire du projet.

**Question**

Pourquoi ne pouvez-vous trier que par certaines colonnes ? c&#39;est-à-dire qu&#39;on ne peut pas trier par missions.

**Réponse**

&quot;Affectations&quot; est une liste et vous ne pouvez pas trier ou regrouper une liste d’éléments. Vous pouvez uniquement trier ou regrouper un élément.

Pour illustrer ce point, imaginez une liste d’affectations comme celle-ci sur une tâche :

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

Quelle tâche doit apparaître en premier dans un tri ? Vous pourriez dire &quot;trier par le prénom dans la liste&quot; mais cela n&#39;est pas nécessairement utile, car vous ne pouvez pas contrôler l&#39;ordre. Workfront évite le problème en ne vous permettant pas du tout de trier par listes.

Qu&#39;en est-il du regroupement par liste ? Si nous pouvions regrouper par une liste de noms vous trouveriez toutes les tâches assignées à Jane, Bill, Dan regroupées et toutes les tâches assignées à Jane, Dan, Bill (même liste, mais dans un ordre différent) dans un autre groupe. Encore une fois, Workfront évite le problème en n’autorisant pas le regroupement par liste.

**Question**

Les heures prévues sont-elles utilisées pour les tâches stratégiques et les heures réelles pour les opérations ?

**Réponse**

Non. Dans notre exemple, nous utilisons les heures prévues pour montrer le niveau d&#39;effort planifié pour les tâches stratégiques et opérationnelles. Cela nous permet de les comparer facilement, que ce soit dans le passé, le présent ou le futur. Vous pouvez également utiliser des heures réelles pour comparer les tâches stratégiques et opérationnelles, mais seulement pour les tâches du passé puisque les heures réelles sont les heures que les gens ont signalées comme étant le temps qu&#39;ils ont réellement passé à travailler sur les tâches.

**Question**

Dans le planificateur de ressources, comment tenir compte des tâches planifiées dans le passé, mais non terminées ? Les heures planifiées ne semblent pas être remontées et ne s’affichent donc pas dans les semaines à venir sous forme de tâches/heures nécessitant des ressources.

**Réponse**

Il n’existe pas de roulement &quot;automatique&quot; des travaux non terminés. Vous devrez replanifier votre projet lorsque cela se produira. Peut-être que les ressources que vous aviez affectées à l’origine à une certaine tâche ne sont pas disponibles dans la nouvelle période. Le chef de projet doit donc examiner cette question et déterminer la meilleure manière de la replanifier. Cela peut signifier la participation des parties prenantes et l’obtention d’approbations pour les changements du plan.

**Question**

Plutôt que de saisir 2 heures par jour pour vérifier les courriers électroniques, les pauses, recommanderiez-vous d’ajuster leur éditeur de texte enrichi ?

**Réponse**

Oui, si vous définissez l’éditeur de texte enrichi sur 0,75, qui affiche un utilisateur disponible 6 heures par jour dans le planificateur de ressources. Ce sera leur disponibilité quotidienne. Si vous souhaitez les afficher comme non disponibles pour différentes périodes selon la date, par exemple si vous n’êtes pas disponible le dernier jour de chaque trimestre, une surcharge est la méthode pour cela.

Certaines personnes préfèrent les projets de frais généraux parce qu’elles peuvent les construire par elles-mêmes et les modifier quand elles le souhaitent, alors qu’elles peuvent ne pas avoir les droits de modifier leur propre éditeur de texte enrichi.

**Question**

Les données du tableau de bord des capacités de l’équipe sont-elles disponibles pour toute personne avec laquelle vous partagez le rapport, quelles que soient les autorisations dont elles disposent sur le travail ?

**Réponse**

Si un utilisateur n’est pas autorisé à afficher l’objet, celui-ci ne sera pas visible dans le rapport/tableau de bord. Cependant, si vous souhaitez que tous les utilisateurs voient les mêmes résultats, vous pouvez accéder à Actions de rapport > Modifier > Paramètres de rapport et saisir votre nom dans le champ &quot;Exécuter ce rapport avec les droits d’accès de&quot;. Les utilisateurs qui sont partagés sur ce rapport pourront ainsi visualiser les résultats exacts. Il ne leur donnera pas un accès supplémentaire au résultat lui-même, de sorte que certains résultats peuvent ou non être cliquables.

**Question**

Comment créer un rapport qui affiche l’ensemble du personnel affecté à un projet (et non au niveau de la tâche) ?

**Réponse**

Vous pouvez créer une colonne dans un rapport de projet qui répertorie tous les utilisateurs répertoriés dans l’onglet Personnel (équipe de projet). Vous souhaitez utiliser le mode texte suivant :

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

Je voudrais un rapport/tableau de bord qui incorpore le fonctionnement de mon équipe. En particulier, les scénarios suivants : - Projets dont je suis propriétaire / Projets créés pour moi / Tâches que j’ai assignées à d’autres / Tâches qui m’ont été assignées

**Réponse**

Projets que je possède

Il existe un rapport intégré intitulé &quot;Projets en cours&quot; qui vous montrera tous les projets en cours. Vous pouvez modifier ce projet et ajouter une règle de filtrage : Projet > Identifiant du propriétaire > Egal > $$USER.IDTlorsque vous enregistrez et renommez le rapport en &quot;Projets que je possède&quot;.

Projets créés pour moi

Il existe un rapport intégré intitulé &quot;Mes projets&quot; qui montre tous les projets en cours dans lesquels vous appartenez à l’équipe de projet (c’est-à-dire que vous êtes le propriétaire, le parrain ou la tâche qui vous a été affectée). Vous ne savez pas si c’est ce que vous demandez, mais il n’y a pas d’autre moyen de savoir si quelqu’un a créé un projet pour vous autre que vous faire le propriétaire, le sponsor ou vous affecter à une tâche.

Tâches que j’ai assignées à d’autres

Créez un rapport de tâche avec les filtres de votre choix, puis accédez à l’onglet Filtre et cliquez sur Passer en mode Texte. Ajoutez ce code à ce qui existe déjà :

```
EXISTS:1:$$OBJCODE=ASSGN
EXISTS:1:taskID=FIELD:ID
EXISTS:1:assignedByID=$$USER.ID
```

Vous verrez alors toutes les tâches pour lesquelles l’utilisateur connecté a attribué au moins l’un des personnes actuellement désignées. Si des personnes désignées ont été affectées par plusieurs personnes, seul le nom de la première personne qui a affecté une personne apparaît comme &quot;Demandé par&quot; sur la page d’entrée de la tâche. Si vous souhaitez voir toutes les personnes affectées et qui ont chacune attribué, vous pouvez ajouter une colonne à votre vue, passer en mode texte et remplacer tout ce qui y est associé par ceci :

```
displayname=All Assignees and Requesters
listdelimiter=<p>
listmethod=nested(assignments).lists
textmode=true
type=iterate
valueexpression=CONCAT("Assigned To: ",{assignedTo}.{name},"; Requested By: ",{assignedBy}.{name})
valueformat=HTML
```

Tâches qui me sont assignées

Il existe un rapport intégré intitulé &quot;Mes tâches&quot; qui vous montre toutes les tâches incomplètes sur les projets en cours dont vous êtes le propriétaire de la tâche. Je vous suggère de modifier le filtre pour vous montrer toutes les tâches pour lesquelles vous êtes l’un des nombreux utilisateurs potentiels affectés, et pas seulement le propriétaire de la tâche. Pour ce faire, supprimez la règle de filtrage.

```
Task > Assigned To ID > Equal > $$USER.ID 
```

et le remplacer par

```
Assignment Users > ID > Equal > $$USER.ID
```

**Question**

Existe-t-il un moyen de personnaliser les libellés des graphiques ? J&#39;ai découvert que lorsque je crée un graphique pour refléter les états du projet, le nom du groupe d&#39;accueil finit par être inclus dans le libellé.

**Réponse**

Les libellés des graphiques utilisent le nom du champ sur lequel vous effectuez le regroupement. Ainsi, la seule façon de modifier les libellés consiste à utiliser un champ personnalisé calculé avec le nom de votre choix. Dans la section de calcul du champ, indiquez le nom du champ natif par lequel vous souhaitez effectuer le groupement.

**Question**

Comment codez-vous les barres de rapports sur les affectations de l&#39;équipe de Chuck s&#39;il vous plaît ? C&#39;est-à-dire ambre pour l&#39;arrière, rouge pour le retard et vert pour l&#39;heure ? Pouvez-vous également modifier l’ordre pour qu’il soit plus logique, c’est-à-dire rouge/ambre/vert ou l’inverse ?

**Réponse**

Pour modifier les couleurs utilisées dans le rapport pour les options Etat d&#39;avancement , éditez le rapport et cliquez sur l&#39;onglet Graphique . Recherchez la liste déroulante &quot;Couleurs personnalisées >&quot;. Il apparaîtra à côté de la zone &quot;Axe gauche (Y)&quot; ou de la zone &quot;Grouper les données par&quot;, selon que vous avez choisi de regrouper des colonnes ou des barres. Dans cette liste déroulante, vous pouvez sélectionner des couleurs. Si vous cliquez sur les nombres en bas à droite des options de couleur, vous pourrez sélectionner votre couleur dans une palette plus grande.

Malheureusement, vous ne pouvez pas changer l&#39;ordre de ceux-ci.

**Question**

Pouvez-vous créer un graphique indiquant le nombre de projets dans lesquels une tâche est affectée à un programme de travail ?

**Réponse**

Oui, voici comment :

* Création d’un rapport de projet
* Si l’utilisateur en question est l’utilisateur connecté, le filtre doit inclure cette ligne :

```
   Project Users > ID > Equal >$$USER.ID 
```

* Dans le cas contraire, remplacez le nom d’utilisateur par [!DNL $$USER.ID]. Tous les projets pour lesquels cette personne se voit attribuer une tâche, ou est le propriétaire ou le sponsor. Si vous souhaitez uniquement voir les projets auxquels des tâches sont affectées, vous devez ajouter ces deux règles de filtrage supplémentaires :

```
   Project > Owner ID > Not Equal > $$USERID
   Project > Sponsor ID > Not Equal > $$USERID
```

* Créez au moins un groupement afin de pouvoir créer un graphique. Regroupez-vous sur n&#39;importe quoi, comme votre compagnie. Cliquez ensuite sur l&#39;onglet Graphique et choisissez un graphique. &quot;Record Count&quot; sera la valeur par défaut pour un axe. Il s’agira du nombre de projets dans lesquels l’utilisateur a une affectation.

Lorsqu’un utilisateur reçoit une affectation sur un projet (assignée à une tâche, à un propriétaire de projet ou à un sponsor de projet), cette personne est ajoutée à l’équipe de projet et est visible dans l’onglet Personnel sous le sous-onglet Personnes . Si un utilisateur est exclu du statut de propriétaire, de sponsor ou d’affectation de tâche, son nom figure toujours dans l’équipe de projet. Il doit être supprimé manuellement si vous souhaitez le supprimer. Gardez à l’esprit que cela peut avoir une incidence sur l’exactitude des résultats de votre rapport. Pour supprimer une personne de l’équipe de projet, accédez à Personnel > Personnes, sélectionnez la ou les personnes, puis cliquez sur le bouton Supprimer qui s’affiche au-dessus de la liste.

**Question**

Comment modifier l’ordre décroissant d’une colonne en mode texte (dans un groupement) ?

**Réponse**

Lorsque vous créez un rapport, vous pouvez choisir de trier la plupart des colonnes dans l’onglet Colonnes (vues) . Si vous n’avez aucun groupe, le rapport de la liste complète sera trié. Si vous avez des groupements, ils seront triés en fonction de ce choix au sein de chaque groupement.

**Question**

Comment créer une colonne qui identifiera les membres de l’équipe affectés à une étape d’approbation ?

**Réponse**

Si vous exécutez un rapport Tâche ou Problème/Requête, une colonne intitulée &quot;Approbateurs et état&quot; est disponible dans le Report Builder et permet d’extraire ces informations.
