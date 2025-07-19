---
title: Demandez à l’expert - Surcharger les rapports en mode texte de base à l’aide de l’explorateur d’API
description: Découvrez l’explorateur d’API, comment l’utiliser et comment améliorer vos rapports à l’aide du mode texte de base. Ce webinaire a été enregistré le 22 janvier 2020.
doc-type: feature video
team: Technical Marketing
kt: 9918
exl-id: f859c4eb-8b3c-4d91-9765-9957dc4678f5
duration: 4068
source-git-commit: 91f20c3e9ee5ae5b259d5cb3da476974acdc6585
workflow-type: tm+mt
source-wordcount: '1658'
ht-degree: 0%

---

# Demandez à l’expert - Surcharger les rapports en mode texte de base à l’aide de l’explorateur d’API

Découvrez l’[[!UICONTROL explorateur d’API]](https://developer.adobe.com/workfront/api-explorer/), comment l’utiliser et comment améliorer vos rapports à l’aide du mode texte de base. Ce webinaire a été enregistré le 22 janvier 2020.

>[!VIDEO](https://video.tv.adobe.com/v/341124/?quality=12)

## Ressources supplémentaires

![Graphique présentant des exemples de règles de code de mode texte](assets/text-mode-chart.png)


**Colonne « Toutes les fonctions » finale**

```
description="Primary =" indicates the user's primary job role
displayname=All Job Roles
listdelimiter=<p>
listmethod=nested(userRoles).lists
textmode=true
type=iterate
valueexpression=IF({user}.{roleID}={role}.{ID},CONCAT("Primary = ",{role}.{name}),{role}.{name})
valueformat=HTML
```

**Mode texte pour la colonne « Toutes les équipes »**

```
displayname=All Teams
listdelimiter=<p>
listmethod=nested(teams).lists
textmode=true
type=iterate
valueexpression={name}
valueformat=HTML
```

**Mode texte pour la colonne « Tous les groupes »**

```
displayname=All Groups
listdelimiter=<p>
listmethod=nested(userGroups).lists
textmode=true
type=iterate
valuefield=group:name
valueformat=HTML
```

**Mode texte pour la colonne « Rapports directs »**

```
displayname=Direct Reports
listdelimiter=<p>
listmethod=nested(directReports).lists
textmode=true
type=iterate
valueexpression={name}
valueformat=HTML
```

## Questions/Réponses

**Question**

Est-il possible d&#39;utiliser n&#39;importe quelle collection dans un rapport en mode texte ?

**Réponse**

Oui, vous pouvez utiliser n’importe quel objet dans la zone des collections. Vous voudrez explorer et voir ce à quoi vous avez accès. Tout le monde n’aura pas accès à la fois à l’objet utilisateur et à l’objet de fonction comme nous l’avons vu avec l’objet Rôles utilisateur dans l’explorateur d’API.

**Question**

Pouvez-vous discuter de « l’utilisation conditionnelle de différentes collections dans la même colonne (mises à jour de projet ou mises à jour de tâche) » ?

**Réponse**

Lorsque vous vous trouvez dans la zone d’itération et que vous voyez le champ de valeur ou l’expression de valeur, cela revient à accéder à l’un des éléments de votre liste de collection. En utilisant le champ de valeur, nous pouvons obtenir le nom de cette fonction, par exemple, ou tout ce qui se trouve dans cet élément de la liste. Si vous vous trouvez dans une tâche, un objet de tâche peut référencer le projet dans lequel il se trouve.

**Question**

Pouvez-vous nous dire si la « collection de mises à jour de tâches n’est possible que dans un rapport de tâches ? »

**Réponse**

Lorsque vous créez un rapport de problème, vous pouvez voir les informations sur la tâche si le problème a été signalé pour la tâche, et vous pouvez également voir ces informations à partir de la collection. À l’exception de ces situations, vous devez être dans un rapport de tâche pour afficher les données de collecte de tâches.

**Question**

Pouvez-vous partager des exemples de format texte ([!DNL CSS]) ?

**Réponse**

Workfront ne prend pas en charge le [!DNL CSS] en mode texte.

**Question**

Quel est le meilleur moyen et/ou le plus rapide de localiser un nom de champ personnalisé (pour les rapports en mode texte) ? J&#39;ai utilisé l&#39;option d&#39;édition HTML dans le navigateur OU en ajoutant un champ dans un rapport et en passant en mode texte pour l&#39;attraper MAIS... curieux de savoir comment les autres font cela

**Réponse**

Je trouve qu’il est plus rapide de sélectionner le champ dans l’interface utilisateur, puis de passer en mode texte et de copier le nom du champ. Cela garantit que j’obtiens l’orthographe correcte du champ.

**Question**

Comment utiliser le mode texte pour identifier les membres d&#39;une équipe dans un rapport ? Nous utilisons actuellement les affectations d&#39;équipes dans les workflows d&#39;approbation de tâche et nous aimerions répertorier les membres de l&#39;équipe à l&#39;étape d&#39;approbation actuelle dans une colonne similaire au fonctionnement du champ Approbateurs et statut .

**Réponse**

Pour référencer les membres de l’équipe associés à l’étape d’approbation actuelle, vous devez référencer une collection d’une collection référencée, ce qui n’est actuellement pas possible grâce aux fonctionnalités du mode texte de Workfront. La colonne actuellement utilisée par votre organisation et indiquant l’équipe associée à l’approbation est votre meilleure option.

**Question**

Le champ et le nom de l’objet doivent-ils respecter la casse (par exemple, rôle ou rôle) ?

**Réponse**

Lorsque vous référencez des objets en mode texte, vous souhaiterez les écrire exactement comme le montre la colonne de droite de l’explorateur d’API. Par exemple, si vous souhaitez référencer un nom de projet à partir d’un rapport de tâche, votre champ de valeur ressemblera à ce qui suit :

```
valuefield=project:name
```

Toutefois, dans le cas des problèmes, ils sont appelés opTasks dans l&#39;explorateur d&#39;API. Ainsi, si vous deviez exécuter un rapport Heure et que vous souhaitez ajouter une colonne pour le nom de l&#39;événement, le champ de valeur
ressemblez à ce qui suit :

```
valuefield=opTask:name
```

**Question**

Je cherche à créer un rapport qui affiche pour chaque projet, la ou les tâches actives actuelles sur lesquelles je travaille. Comment ferais-je pour le mieux ? J’imagine qu’il s’agirait d’un rapport de tâche auquel des colonnes Informations sur le projet seraient également ajoutées ?

**Réponse**

C&#39;est exact. Un rapport de tâche serait préférable à cet effet. Vous devez définir « Tâches actives ». Si vous utilisez des prédécesseurs, il s’agit de tâches prêtes. Vous pouvez donc filtrer par Prêt = Vrai. Toutes les tâches prêtes à démarrer seront alors importées. Je vous recommande ensuite de regrouper par nom de projet, de cette manière vos tâches sont toutes regroupées et vous pouvez voir en un coup d’œil quelles tâches appartiennent à quel projet.

**Question**

Existe-t-il un moyen de créer des rapports qui calculent les données (par exemple, le pourcentage de projets qui répondent à certains critères) ?

**Réponse**

La meilleure façon de créer un rapport pour présenter ou calculer des données (% par exemple) serait d&#39;appliquer des regroupements à votre rapport, puis d&#39;appliquer un graphique. Si vous deviez ajouter un graphique en secteurs à votre rapport, vous avez la possibilité que les secteurs soient exprimés en valeurs ou en pourcentages.

**Question**

Pouvez-vous utiliser le mode texte pour identifier les membres d&#39;une équipe qui sont affectés à l&#39;étape d&#39;approbation de tâche actuelle de la même manière que les approbateurs et la colonne Statut ?

**Réponse**

Vous devez ajouter une colonne de collection en mode texte à votre rapport de tâche avec les éléments suivants :

```
displayname=Current Approval Stage Approvers 
listdelimiter=<p> 
listmethod=nested(currentApprovalStep.stepApprovers).lists 
textmode=true
type=iterate 
valuefield=user:name 
valueformat=HTML
```

**Question**

Êtes-vous en mesure de filtrer l’emplacement où Tous les groupes contiennent un groupe particulier ?

**Réponse**

Si vous souhaitez filtrer les éléments de votre rapport, vous devez le faire sous l’onglet Filtrer de votre rapport. Ainsi, si vous souhaitez afficher uniquement les utilisateurs dont l’un des groupes est Comptabilité, vous devez ajouter une règle de filtrage qui indique :

```
Other Groups>ID>Equal>Accounting
```

**Question**

Existe-t-il un moyen de créer un rapport qui détermine la durée réelle d’une combinaison de tâches ?

**Réponse**

Vous devez filtrer votre rapport pour n’inclure que la combinaison de tâches souhaitée. Vous devez ensuite placer une colonne Durée réelle dans votre affichage et la synthétiser par Somme dans les Paramètres de colonne. Enfin, vous devez regrouper votre rapport d&#39;une manière ou d&#39;une autre. Lorsque vous exécutez le rapport, la barre de regroupement affiche le total des durées réelles contenues dans les lignes regroupées.

**Question**

Existe-t-il un moyen de soustraire des tâches qui relèvent d&#39;un parent pour déterminer la durée du reste des tâches relevant d&#39;un parent ?

**Réponse**

La durée d&#39;une tâche parent est calculée en soustrayant la date de début de la tâche de début la plus ancienne de la date de fin de la dernière tâche de fin sous ce parent. Dans un rapport, vous ne connaissez que chaque tâche individuelle qui est prise en compte pour savoir s’il faut l’afficher ou non. Le moteur de rapports n’a aucun moyen de se raccrocher aux informations d’une tâche et de les utiliser lorsqu’il examine une autre tâche. Ainsi, la seule façon d&#39;accomplir ce que vous demandez est de supprimer une tâche de la liste des tâches d&#39;un projet d&#39;être sous un certain parent tout en observant comment la durée de la tâche parent est recalculée.

**Question**

Pour les regroupements conditionnels, un formulaire personnalisé (pensez « États de l’Ouest », « États du Centre », « États de l’Est ») permettant de décoder les groupes individuels est une technique courante qui fonctionne bien à cet égard. Quand recommandez-vous d’utiliser des regroupements calculés plutôt que des paramètres calculés ?

**Réponse**

Les regroupements calculés (ou expression de valeur dans un regroupement) sont un moyen pratique d’obtenir un résultat à afficher dans la barre de regroupement. Vous pouvez également le faire à l’aide d’un champ personnalisé calculé. Chaque approche comporte des avantages et des inconvénients, à savoir :

* Les expressions de valeur sont calculées chaque fois que la page du navigateur est actualisée. Cela peut être préférable aux champs personnalisés calculés qui sont recalculés chaque fois que l’objet auquel ils sont associés est modifié, ou lorsque les champs calculés sont recalculés dans une modification en bloc, ou lorsque le formulaire personnalisé est modifié et que l’option « Mettre à jour les calculs précédents » est sélectionnée.
* Toutefois, les expressions de valeur ne peuvent pas être utilisées dans les graphiques, la mise en forme conditionnelle ou les filtres. Vous devrez utiliser des champs personnalisés calculés pour ces éléments.

**Question**

N’existe-t-il aucun moyen de remplacer le nom d’affichage du regroupement « Aucune valeur » par tout autre nom que nous choisirons pour le signaler ? en d’autres termes, il s’agira TOUJOURS de « Aucune valeur » ?

**Réponse**

Il existe un moyen de remplacer « Aucune valeur » par quelque chose de différent. Supposons que vous ayez un rapport de projet regroupé par nom de Portfolio. Tous les projets qui ne sont pas affectés à un portefeuille se retrouvent dans un regroupement avec le titre :

```
Portfolio: Name: No Value
```

Pour modifier ce paramètre, modifiez le regroupement en mode texte et remplacez cette ligne :

```
group.0.valuefield=portfolio:name
```

avec cette ligne :

```
group.0.valueexpression=IF(ISBLANK({portfolio}.{name}),"Not in any Portfolio",{portfolio}.{name})
```

Le regroupement porte désormais le titre suivant :

```
Portfolio: Name: Not in any Portfolio
```

**Question**

Existe-t-il un paramètre pour effectuer le suivi des affectations incomplètes, à savoir :

1. Tâches à affectation unique auxquelles aucun individu n&#39;a été affecté ou
1. Tâches avec plusieurs affectations ayant au moins une personne non affectée pour les rôles demandés

**Réponse**

Pour ce faire, utilisez un rapport d’affectation et filtrez pour

```
Assigned To ID > Is Blank and Role ID > Is Not Blank
```

Cette action permet d’extraire toutes les tâches ou tous les événements affectés à un rôle, mais pas nécessairement à un utilisateur spécifique. Vous devrez ajouter les colonnes du nom de la tâche et de l’événement pour voir à quel objet appartient l’affectation. Si elle est regroupée par nom de projet, elle doit permettre de conserver son organisation.

**Question**

Chuck, j’oublie, mais vous souvenez-vous de la propriété en mode texte qui s’affichera alors sous forme d’info-bulle, au survol ?

**Réponse**

description= permet d’afficher une info-bulle lorsque vous pointez sur l’en-tête de colonne.

**Question**

Puis-je créer un rapport sur un champ de case à cocher qui autorise plusieurs sélections, mais qui n’extrait que la première sélection dans le rapport ?

**Réponse**

Oui. Les choix sélectionnés dans le champ de case à cocher se trouvent tous dans une chaîne, chaque sélection étant séparée par une virgule. Utilisez l’expression SEARCH pour trouver la position de la première virgule dans le Champ de case à cocher, puis utilisez cet index avec l’expression LEFT pour afficher autant de caractères depuis le début de la liste. Voici le code :

```
valueexpression=IF(SEARCH(",",{DE:Checkbox Field},0)>0,LEFT({DE:Checkbox Field},SEARCH(",",{DE:Checkbox Field},0)),{DE:Checkbox Field})
```

Si vous utilisez une virgule dans le nom d’une sélection dans votre champ de case à cocher, seule la partie de cette sélection s’affiche jusqu’à la première virgule.
