---
title: Demandez à l’expert - Évaluation de la qualité et de l’engagement
description: Découvrez comment créer des rapports qui répondent aux questions de qualité et d’engagement. Ce webinaire a été enregistré le 13 novembre 2019.
doc-type: feature video
team: Technical Marketing
kt: 9914
exl-id: 76a8e418-71c7-414a-9938-e64e4e73c184
duration: 3980
source-git-commit: 91f20c3e9ee5ae5b259d5cb3da476974acdc6585
workflow-type: tm+mt
source-wordcount: '1210'
ht-degree: 0%

---

# Demandez à l’expert - Évaluation de la qualité et de l’engagement

Découvrez comment créer des rapports qui répondent aux questions de qualité et d’engagement. Ce webinaire a été enregistré le 13 novembre 2019.

>[!VIDEO](https://video.tv.adobe.com/v/341120/?quality=12)

## Questions/Réponses

**Question**

Certains champs sont disponibles pour le filtrage, mais ne sont pas disponibles lorsque vous essayez de les regrouper. Vous efforcez-vous de rendre ces options cohérentes ?

**Réponse**

Les outils de création de rapports ne vous permettent pas d’effectuer un regroupement en fonction d’un champ dynamique ou comportant plusieurs choix à la fois, comme un champ de case à cocher. Vous ne pouvez regrouper que des champs ayant une seule valeur, même s’ils peuvent avoir plusieurs choix.

Vous pouvez filtrer par cases à cocher et les afficher, mais vous ne pouvez pas les regrouper.

**Question**

Dans l’exemple d’itération sur les fonctions, puis-je afficher la fonction principale en gras ?

**Réponse**

Dans l’itération, nous pouvons identifier la fonction principale. Nous devons le faire dans une expression de valeur, mais les codes HTML ne sont pas reconnus dans une expression de valeur. Nous devons donc trouver une autre façon d&#39;identifier le rôle comme étant le premier. J’ai placé « ** » avant et après le nom du rôle principal dans ce code. Essayez-le et voyez ce que vous en pensez :

```
displayname=All Job Roles 
listdelimiter=<p> 
listmethod=nested(userRoles).lists 
textmode=true
type=iterate 
valueexpression=IF({user}.{roleID}={role}.{ID},CONCAT("**",{role}.{name},"**"),{role}. {name})
valueformat=HTML
```

Vous obtiendrez ainsi une liste comme celle-ci :

```
Support Engineer 
QA Engineer 
**Designer**
```

Où Designer est le rôle principal de cet utilisateur.

**Question**

Bonjour ! Je suis en train de mettre au point un workflow pour notre équipe de rédaction qui suit où en est un article dans son cycle de vie (rédaction initiale —> revue(s) de service —> modifications finales —> publication). Ils souhaitent voir facilement à quel jalon ou à quelle tâche elle se trouve actuellement. Le retour d’informations que j’obtiens est que la vue Jalon standard (avec l’ombrage rouge ou vert) est trop « occupée et complexe ». Existe-t-il un moyen d’afficher simplement le « Nom du projet » et le « Jalon actuel » dans un tableau ou une grille ?

**Réponse**

Oui. Vous pouvez créer un rapport de tâche qui affichera les tâches jalonnées en cours de réalisation et la tâche à laquelle elles sont associées. Vous pouvez le faire dans un tableau ou dans un rapport de liste.

**Question**

Pouvons-nous avoir des informations sur les épreuves associées à des informations sur le projet dans un rapport ?

**Réponse**

Si vous avez créé un rapport Approbation de l&#39;épreuve, les informations du projet peuvent être extraites en colonnes à l&#39;aide du mode texte. Par exemple, si vous souhaitez référencer le nom du projet dans une colonne, vous pouvez utiliser ce qui suit :

```
displayname=Project Name
textmode=true 
valuefield=documentVersion:document:project:name 
valueformat=HTML
```

**Question**

Je souhaiterais également obtenir plus d’informations sur les rapports concernant les données de preuve en ce qui concerne le projet. Par exemple, un rapport de projet qui inclut la décision sur l’épreuve et les commentaires.

**Réponse**

Pour référencer les informations de projet et les informations sur les BAT dans un seul rapport, vous devez créer un rapport Approbation du BAT. Actuellement, les commentaires d’une épreuve ne peuvent pas être intégrés dans ce rapport. Cependant, chaque décision d’approbateur d’épreuve figure sur son propre élément de ligne dans la colonne Décision de l’approbateur .

**Question**

J’utilise souvent sharecol pour créer le statut d’une seule page (plusieurs colonnes). Cependant, je trouve que si, après avoir créé un rapport, je souhaite ajouter une colonne en haut de la page, il est très long de revenir en arrière et de la modifier. Avez-vous des conseils ou des astuces pour effectuer ce type de changement ?

**Réponse**

Si vous envisagez de placer une colonne en haut d&#39;une liste de colonnes de mode texte, il vous suffira de renuméroter vos colonnes manuellement.

Mais si vous avez déjà créé le rapport avec la première colonne composée de colonnes partagées et que vous souhaitez placer une autre colonne partagée en haut de la liste, c’est plus facile.

Dans l’éditeur de rapports, ajoutez simplement quelques nouvelles colonnes et faites-les glisser à l’extrémité gauche de l’écran Colonnes (affichage). après cela, jetez un coup d’œil à ce qui était auparavant la colonne de gauche et vous remarquerez que les numéros des colonnes du mode texte ont tous été incrémentés. Faites glisser autant de colonnes vides que nécessaire. Assurez-vous de mettre quelque chose dans ces colonnes vides avant de l’enregistrer ou ils seront supprimés.

**Question**

Bonjour, en ce qui concerne le rapport de bogue final, comment les rapports peuvent-ils être générés pour plusieurs projets si des bogues surviennent pour plusieurs projets ??

**Réponse**

Vous pouvez filtrer par portefeuille ou projet, selon la manière dont vous avez organisé votre travail.

Vous pouvez également filtrer les files d’attente de demandes. Vous pouvez configurer des files d&#39;attente de demandes pour chaque projet, dans lesquelles vous pouvez créer des utilisateurs clients en tant que réviseurs qui peuvent se connecter et envoyer des tickets directement aux files d&#39;attente de demandes que vous avez partagées avec eux.

**Question**

Les premiers rapports étaient basés sur les projets/noms de projet, peut-on faire de même pour les tâches et si oui, quelle est la meilleure façon de les regrouper, car le nom de la tâche serait peut-être différent le plus souvent... merci !

**Réponse**

Tous ces rapports peuvent être créés sous la forme de rapports de tâche, de problème ou de projet, selon la manière dont vous décidez d’effectuer le suivi.

Une méthode courante pour regrouper des tâches consiste à les regrouper d’abord par nom de projet, puis par nom de tâche dans chaque projet. De cette façon, si vous avez deux tâches portant le même nom, il est facile de voir dans quel projet elles se trouvent.

**Question**

Je veux savoir quelles épreuves sont en suspens, à quelle tâche et à quel projet elles sont liées, quand elles ont été acheminées, quand elles sont dues, et qui est le modérateur et l’approbateur.

**Réponse**

Les épreuves en attente peuvent être filtrées en sélectionnant Décision en attente > Est égal à > Vrai dans un rapport Approbation de l’épreuve . Il existe une colonne pour l&#39;approbateur qui vous indique qui n&#39;a pas encore pris de décision.

Vous pouvez référencer la tâche ou le projet auquel l’épreuve est liée en mode texte (voir les exemples ci-dessous).

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

Pour ce qui est de la date d’acheminement, de l’échéance et du modérateur, ces champs ne peuvent actuellement être extraits dans aucun des rapports Workfront. Vous devez donc cliquer directement sur le BAT pour afficher ces informations.

**Question**

Pouvez-vous configurer un formulaire personnalisé à envoyer automatiquement à un demandeur une fois sa demande remplie ? Comme une enquête de « satisfaction client » ?

**Réponse**

Voici une chose que vous pouvez faire qui pourrait répondre à vos besoins. Vous pouvez joindre une notification de rappel à un événement qui enverra un e-mail au « Validé par » après la saisie d’une date d’achèvement effective. L&#39;entité Saisie par est la personne qui a créé l&#39;événement.

Vous pouvez créer la notification de rappel comme nous l’avons fait dans le webinaire pour « Rappel pour remplir la révision après action (AAR) », sauf qu’il s’agirait d’un rappel d’événement. Vous souhaiterez probablement créer un modèle d’e-mail pour celui-ci afin de fournir un lien vers le questionnaire. Vous devrez appliquer manuellement la notification de rappel à chaque événement (ou utiliser la modification en bloc).

Une intégration serait préférable, car elle pourrait automatiser les étapes manuelles, mais la notification de rappel peut être effectuée immédiatement.

**Question**

J&#39;ai créé un rapport présentant les projets par type de modèle. Je peux répertorier le propriétaire du projet, mais pas les personnes affectées à un projet.

**Réponse**

Si vous souhaitez extraire l’équipe de projet (onglet Personnel) dans une colonne de votre rapport de projet, vous devez la créer via le mode texte. Le mode texte est le suivant :

```
displayname=Staffing 
listdelimiter=<p> 
listmethod=nested(projectUsers).lists 
textmode=true
type=iterate 
valuefield=user:name 
valueformat=HTML
```

## Code du mode texte pour le rapport d’engagement de l’AAR

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
