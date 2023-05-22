---
title: Demander à l’expert - Évaluation de la qualité et de l’engagement
description: Découvrez comment créer des rapports qui répondent aux questions de qualité et d’engagement. Ce webinaire a été enregistré le 13 novembre 2019.
activity: use
doc-type: feature video
team: Technical Marketing
kt: 9914
source-git-commit: edd0bdb28a9b3d065a64a95af6a216b747577c77
workflow-type: tm+mt
source-wordcount: '1211'
ht-degree: 1%

---

# Demander à l’expert - Évaluation de la qualité et de l’engagement

Découvrez comment créer des rapports qui répondent aux questions de qualité et d’engagement. Ce webinaire a été enregistré le 13 novembre 2019.

>[!VIDEO](https://video.tv.adobe.com/v/341120/?quality=12)

## Q&amp;R

**Question**

Certains champs peuvent faire l’objet d’un filtrage, mais ne sont pas disponibles lorsque vous essayez de les regrouper. Travaillez-vous à leur proposer des options cohérentes ?

**Réponse**

Les outils de création de rapports ne vous permettent pas de regrouper un champ dynamique ou un champ pouvant avoir plusieurs options sélectionnées en même temps, comme un champ de case à cocher. Vous ne pouvez regrouper que les champs ayant une seule valeur, même s’ils peuvent avoir de nombreux choix.

Vous pouvez filtrer par cases à cocher, et les afficher, vous ne pouvez simplement pas les regrouper.

**Question**

Dans l&#39;exemple d&#39;itération sur les rôles de tâche, puis-je afficher le Principal en gras ?

**Réponse**

Dans l’itération, nous pouvons identifier le rôle Principal de la tâche. Nous devons le faire dans une expression de valeur, mais les codes de HTML ne sont pas reconnus dans une expression de valeur. Nous devons donc trouver une autre façon d&#39;identifier le rôle comme étant le Principal. J’ai placé &quot;**&quot; avant et après le nom Principal du rôle dans ce code. Essayez-le et voyez comment vous l’aimez :

```
displayname=All Job Roles 
listdelimiter=<p> 
listmethod=nested(userRoles).lists 
textmode=true
type=iterate 
valueexpression=IF({user}.{roleID}={role}.{ID},CONCAT("**",{role}.{name},"**"),{role}. {name})
valueformat=HTML
```

Vous obtenez alors une liste de ce type :

```
Support Engineer 
QA Engineer 
**Designer**
```

Où Designer est le rôle Principal de cet utilisateur.

**Question**

Salut ! Je suis en train de mettre en place un workflow pour notre équipe éditoriale qui effectue le suivi de l’état d’un article dans son cycle de vie (écriture initiale —> révisions du(des) département(s) —> modifications finales —> publication). Ils veulent facilement voir à quel jalon ou à quelle tâche il se trouve actuellement. Le retour que j’obtiens est que la vue Milestone standard (avec l’ombrage rouge ou vert) est trop &quot;occupée et complexe&quot;. Existe-t-il un moyen d’afficher simplement &quot;Nom du projet&quot; et &quot;Jalon actuel&quot; dans une table ou une grille ?

**Réponse**

Oui. Vous pouvez créer un rapport de tâche qui affichera les tâches de jalon en cours de traitement et la tâche à laquelle il est associé. Vous pouvez le faire dans un tableau ou dans un rapport de liste.

**Question**

Est-il possible de combiner les informations de BAT avec les informations de projet dans un rapport ?

**Réponse**

Si vous avez créé un rapport Validation du BAT, les informations du projet peuvent être regroupées en colonnes à l’aide du mode texte. Par exemple, si vous souhaitez référencer le nom du projet dans une colonne, vous pouvez utiliser les éléments suivants :

```
displayname=Project Name
textmode=true 
valuefield=documentVersion:document:project:name 
valueformat=HTML
```

**Question**

Je voudrais aussi plus d&#39;informations sur le reporting des données de BAT en ce qui concerne le projet. Par exemple, un rapport de projet qui comprend la décision et les commentaires du BAT.

**Réponse**

Pour référencer les informations du projet et du BAT dans un seul rapport, vous devez créer un rapport d’approbation de BAT. Actuellement, les commentaires d’un BAT ne peuvent pas être extraits dans ce rapport. Cependant, chaque décision d’approbateur de BAT se trouve sur sa propre ligne sous la colonne Décision d’approbateur .

**Question**

J’utilise souvent sharecol pour créer un état de page unique (plusieurs colonnes). Cependant, je constate que si, après la création d’un rapport, j’ajoute une colonne en haut de la page, il est très long de revenir en arrière et de modifier le rapport. Avez-vous des conseils ou des astuces pour faire ce type de changement ?

**Réponse**

Si vous envisagez de placer une colonne en haut d’une liste de colonnes en mode texte, il vous suffit de renuméroter vos colonnes manuellement.

Mais si vous avez déjà créé le rapport avec la première colonne correspondant à certaines colonnes partagées et que vous souhaitez placer une autre colonne partagée en haut de la liste, cela est plus facile.

Dans l’éditeur de rapports, ajoutez simplement deux nouvelles colonnes et faites-les glisser à l’extrémité gauche de l’écran Colonnes (vues) . une fois que vous avez effectué cette opération, examinez ce qui était la colonne de gauche et vous remarquerez que les numéros des colonnes du mode texte ont tous été incrémentés. Faites glisser autant de colonnes vides que nécessaire. Veillez à placer un élément dans ces colonnes vides avant de l’enregistrer, sinon il sera supprimé.

**Question**

Bonjour - en ce qui concerne le rapport de bogue final - comment les rapports peuvent-ils être créés pour plusieurs projets - si des bogues sont présents pour plusieurs projets??

**Réponse**

Vous pouvez filtrer par portefeuille ou projet, selon la manière dont vous avez organisé votre travail.

Vous pouvez également filtrer selon les files d’attente de requête. Vous pouvez configurer des files d’attente de requêtes pour chaque projet, dans lesquelles vous pouvez créer des utilisateurs clients en tant que réviseurs, qui peuvent se connecter et envoyer des tickets directement aux files d’attente de requêtes que vous avez partagées avec eux.

**Question**

Les premiers rapports étaient basés sur le nom des projets/projets. Cela peut-il également être fait sur les tâches et, si c’est le cas, quelle est la meilleure façon de les regrouper, car le nom de la tâche serait peut-être différent le plus souvent...merci !

**Réponse**

Tous ces rapports peuvent être créés sous la forme de rapports de tâche, de publication ou de projet, selon la manière dont vous décidez de les suivre.

Une méthode courante pour regrouper les tâches consiste à les regrouper d’abord par leur nom de projet, puis par le nom de la tâche au sein de chaque projet. De cette façon, si vous avez deux tâches portant le même nom, il est facile de voir dans quel projet ils se trouvent.

**Question**

Je veux savoir quels bons à tirer sont exceptionnels, à quelle tâche et à quel projet ils sont liés, quand ils ont été routés, quand ils sont dus, et qui est le modérateur et l’approbateur.

**Réponse**

Les bons à tirer en suspens peuvent être filtrés par Décision en attente > Égal à > Vrai dans un rapport Approbation de BAT. Une colonne Approbateur vous indique qui n’a pas encore pris de décision.

Vous pouvez référencer la tâche ou le projet auquel le BAT est associé à l’aide du mode texte (voir les exemples ci-dessous).

```
displayname=Task Name
textmode=true 
valuefield=documentVersion:document:task:name 
valueformat=HTML
```

```
displayname=Project Name
textmode=true 
valuefield=documentVersion:document:project:name
valueformat=HTML
```

En ce qui concerne la date de routage, l’échéance et le modérateur, ces champs ne peuvent actuellement pas être extraits dans aucun des rapports Workfront. Vous devez donc cliquer directement dans le Bon à tirer pour afficher ces informations.

**Question**

Pouvez-vous configurer un formulaire personnalisé à envoyer automatiquement à un demandeur une fois sa demande terminée ? Comme pour un questionnaire de &quot;satisfaction client&quot; ?

**Réponse**

Voici une chose que vous pouvez faire qui pourrait répondre à vos besoins. Vous pouvez joindre une notification de rappel à un problème qui enverra un courrier électronique à &quot;Entré par&quot; après qu’une date de fin réelle ait été saisie. La personne entrée par est celle qui a créé le problème.

Vous pouvez créer la notification de rappel comme nous l’avons fait dans le webinaire pour &quot;Rappel pour remplir la révision après action (AAR)&quot;, sauf qu’il s’agit d’un rappel de problème. Vous souhaiterez probablement créer un modèle d&#39;email pour celui-ci et fournir un lien vers l&#39;enquête. Vous devrez appliquer manuellement la notification de rappel à chaque problème (ou utiliser la modification en masse).

Une intégration serait préférable, car elle pourrait automatiser les étapes manuelles, mais la notification de rappel peut être effectuée immédiatement.

**Question**

J’ai créé un rapport présentant les projets par type de modèle. Je peux répertorier le propriétaire du projet, mais pas les personnes affectées à un projet.

**Réponse**

Si vous souhaitez placer l’équipe de projet (onglet Personnel) dans une colonne de votre rapport de projet, vous devez le créer en mode texte. Le mode texte est le suivant :

```
displayname=Staffing 
listdelimiter=<p> 
listmethod=nested(projectUsers).lists 
textmode=true
type=iterate 
valuefield=user:name 
valueformat=HTML
```

## Code de mode texte pour le rapport Engagement AAR

```
column.0.displayname=Task Details
column.0.value=<b>Project Name:</b>&nbsp;
column.0.valueformat=HTML
column.0.sharecol=true
column.1.valuefield=project:name
column.1.valueformat=HTML
column.1.sharecol=true
column.2.value=<br>
column.2.valueformat=HTML
column.2.sharecol=true
column.3.value=<b>Task Name:</b>&nbsp;
column.3.valueformat=HTML
column.3.sharecol=true
column.4.valuefield=name
column.4.valueformat=HTML
column.4.sharecol=true
column.5.value=<br>
column.5.valueformat=HTML
column.5.sharecol=true
column.6.value=<b>Task Owner:</b>&nbsp;
column.6.valueformat=HTML
column.6.sharecol=true
column.7.valuefield=assignedTo:name
column.7.valueformat=HTML
column.7.sharecol=true
column.8.value=<br>
column.8.valueformat=HTML
column.8.sharecol=true
column.9.value=<b>Actual Completion Date:</b>&nbsp;
column.9.valueformat=HTML
column.9.sharecol=true
column.10.valuefield=actualCompletionDate
column.10.valueformat=HTML
column.11.displayname=Name of Reviewer
column.11.linkedname=Name of Reviewer
column.11.namekey=view.relatedcolumn
column.11.namekeyargkey.0=Name of Reviewer
column.11.namekeyargkey.1=name
column.11.querysort=DE:Name of Reviewer:name
column.11.valuefield=Name of Reviewer:name
column.11.valueformat=customReferenceObjectAsString
column.12.displayname=AAR 1
column.12.description=In your view, does the work match stakeholders’ expectations? Did we achieve the intended results?
column.12.value=<b>AAR 1 Score:</b>&nbsp;
column.12.valueformat=HTML
column.12.sharecol=true
column.13.valuefield=AAR 1 - In your view, does the work match stakeholders’ expectations? Did we achieve the intended results?
column.13.valueformat=customDataLabelsAsString
column.13.sharecol=true
column.14.value=<br>
column.14.valueformat=HTML
column.14.sharecol=true
column.15.value=<br><b>AAR 1 User Comment:</b>&nbsp;
column.15.valueformat=HTML
column.15.sharecol=true
column.16.valuefield=AAR 1 User Comment
column.16.valueformat=customDataLabelsAsString
column.17.linkedname=direct
column.17.namekey=AAR 1 Reviewer Comment
column.17.querysort=DE:AAR 1 Reviewer Comment
column.17.valuefield=AAR 1 Reviewer Comment
column.17.valueformat=customDataLabelsAsString
column.18.linkedname=direct
column.18.displayname=AAR 1 Needs Attn
column.18.querysort=DE:AAR 1 Needs Attention
column.18.valuefield=AAR 1 Needs Attention
column.18.valueformat=customDataLabelsAsString
column.19.linkedname=direct
column.19.displayname=AAR 1 Needs Attn Notes
column.19.querysort=DE:AAR 1 Needs Attention Notes
column.19.valuefield=AAR 1 Needs Attention Notes
column.19.valueformat=customDataLabelsAsString
column.20.displayname=AAR 2
column.20.description=Do You Believe This Work Will Make an Impact?
column.20.value=<b>AAR 2 Score:</b>&nbsp;
column.20.valueformat=HTML
column.20.sharecol=true
column.21.valuefield=AAR 2 - Do You Believe This Work Will Make an Impact?
column.21.valueformat=customDataLabelsAsString
column.21.sharecol=true
column.22.value=<br>
column.22.valueformat=HTML
column.22.sharecol=true
column.23.value=<br><b>AAR 2 User Comment:</b>&nbsp;
column.23.valueformat=HTML
column.23.sharecol=true
column.24.valuefield=AAR 2 User Comment
column.24.valueformat=customDataLabelsAsString
column.25.linkedname=direct
column.25.namekey=AAR 2 Reviewer Comment
column.25.querysort=DE:AAR 2 Reviewer Comment
column.25.valuefield=AAR 2 Reviewer Comment
column.25.valueformat=customDataLabelsAsString
column.26.linkedname=direct
column.26.displayname=AAR 2 Needs Attn
column.26.querysort=DE:AAR 2 Needs Attention
column.26.valuefield=AAR 2 Needs Attention
column.26.valueformat=customDataLabelsAsString
column.27.linkedname=direct
column.27.displayname=AAR 2 Needs Attn Notes
column.27.querysort=DE:AAR 2 Needs Attention Notes
column.27.valuefield=AAR 2 Needs Attention Notes
column.27.valueformat=customDataLabelsAsString
column.28.displayname=AAR 3
column.28.description=Are you proud of the work you did on this?
column.28.value=<b>AAR 3 Score:</b>&nbsp;
column.28.valueformat=HTML
column.28.sharecol=true
column.29.valuefield=AAR 3 - Are you proud of the work you did on this?
column.29.valueformat=customDataLabelsAsString
column.29.sharecol=true
column.30.value=<br>
column.30.valueformat=HTML
column.30.sharecol=true
column.31.value=<br><b>AAR 3 User Comment:</b>&nbsp;
column.31.valueformat=HTML
column.31.sharecol=true
column.32.valuefield=AAR 3 User Comment
column.32.valueformat=customDataLabelsAsString
column.33.linkedname=direct
column.33.namekey=AAR 3 Reviewer Comment
column.33.querysort=DE:AAR 3 Reviewer Comment
column.33.valuefield=AAR 3 Reviewer Comment
column.33.valueformat=customDataLabelsAsString
column.34.linkedname=direct
column.34.displayname=AAR 3 Needs Attn
column.34.querysort=DE:AAR 3 Needs Attention
column.34.valuefield=AAR 3 Needs Attention
column.34.valueformat=customDataLabelsAsString
column.35.linkedname=direct
column.35.displayname=AAR 3 Needs Attn Notes
column.35.querysort=DE:AAR 3 Needs Attention Notes
column.35.valuefield=AAR 3 Needs Attention Notes
column.35.valueformat=customDataLabelsAsString
column.36.displayname=Done
column.36.valuefield=Review Complete
column.36.valueformat=customDataLabelsAsString
```
