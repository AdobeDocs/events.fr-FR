---
title: Demander à l’expert - Mesurer la vitesse
description: Découvrez comment mesurer et suivre la vitesse à l’aide de [!DNL Workfront] création de rapports. Cet atelier a été enregistré le 14 août 2019.
activity: use
doc-type: feature video
team: Technical Marketing
kt: 9912
source-git-commit: edd0bdb28a9b3d065a64a95af6a216b747577c77
workflow-type: tm+mt
source-wordcount: '3919'
ht-degree: 1%

---

# Demander à l’expert - Mesurer la vitesse

Découvrez comment mesurer et suivre la vitesse à l’aide de [!DNL Workfront] création de rapports. Cet atelier a été enregistré le 14 août 2019.

>[!VIDEO](https://video.tv.adobe.com/v/341057/?quality=12)

## Champs personnalisés utilisés dans la présentation

Gagnez du temps en copiant et en collant les calculs ci-dessous.

**Date de première validation**

Format : Date

Calcul :

```
IF(ISBLANK(First Commit Date),Default Baseline.Planned Completion Date,First Commit Date)
```

**Première durée**

Format : Texte

Calcul :

```
IF(ISBLANK(First Duration),Default Baseline.Duration,First Duration)
```

**Rapport travail-validation**

Format : nombre

Calcul :

```
ROUND(DIV(Actual Duration,First Duration),1)
```

**État du ratio travail-validation**

Format:Texte

Calcul :

```
IF({Work-to-Commit Ratio}>2,"Terrible",IF({Work-to-CommitRatio}>1.6,"Poor",IF({Work-to-Commit Ratio}>1.2,"Not Bad","Exc ellent")))
```

**Vitesse ajustée**

Format : nombre

Calcul :

```
ROUND(DIV(Actual Duration,Duration),1)
```

**État de vitesse ajusté**

Format:Texte

Calcul :

```
IF(Adjusted Velocity>2,"Terrible",IF(Adjusted Velocity>1.6,"Poor",IF(Adjusted Velocity>1.2,"Not Bad","Excellent")))
```

## Q&amp;R

**Question**

Bonjour, merci d&#39;avoir organisé ce webinaire. J’ai une question à propos de Field dans Workfront. Dans notre système, nous avons créé un champ personnalisé appelé &quot;Etat&quot; qui est une combinaison de Statut et de Condition. Ce champ État contient beaucoup de statues dans mille projets, ce qui est très important pour notre extraction de données Tableau. Cependant, nous voulons maintenant éliminer ce champ et utiliser le champ Condition , le champ natif à la place. Avez-vous la moindre idée de comment je peux retourner ce champ sans perdre de données ? Tout ce que je peux imaginer de le faire maintenant sans perdre de données, c&#39;est de le changer manuellement d&#39;un projet à l&#39;autre.

**Réponse**

Dans une situation de ce type, vous pouvez utiliser le filtrage et la modification en masse pour semi-automatiser la corvée de remplissage du champ Condition en fonction de votre champ personnalisé État .

Voici la procédure à suivre :

1. Déterminez les valeurs d’état que vous souhaitez mapper aux valeurs de condition. Par exemple, supposons que vous ayez une valeur d’état &quot;En retard&quot; et &quot;Très en retard&quot; qui correspondent toutes deux à une valeur de condition &quot;En problème&quot;.
1. Créez un rapport de projet présentant tous les projets pour lesquels la valeur d’état est &quot;En retard&quot; et &quot;Très en retard&quot;.
1. Exécutez le rapport. Assurez-vous d’afficher tous les projets (voir les options en bas à droite du rapport).
1. Cochez la case en haut à gauche du rapport dans la barre avec les en-têtes de colonne. Tous les projets du rapport seront alors sélectionnés.
1. Cliquez sur le bouton Modifier situé au-dessus de la liste des rapports.
1. Définir le type de condition sur Manuel
1. Définissez le champ Condition sur En problème .
1. Cliquez sur Enregistrer les modifications


**Question**

Comment est défini Excellent, Not Bad, etc. ?

**Réponse**

Ce n&#39;était qu&#39;un exemple, mais voici comment je l&#39;ai configuré. J&#39;ai d&#39;abord calculé deux index :

Vitesse ajustée

La formule pour cela est Durée réelle/Durée planifiée (qui est stockée dans le champ Durée d’un projet). Puisque la durée planifiée du projet peut changer chaque fois que le projet est replanifié, la durée planifiée représente la planification finale.

Rapport travail-validation

Cette formule est semblable à la vitesse ajustée, sauf qu’au lieu d’utiliser la valeur Durée planifiée du plan de relance final, nous voulons utiliser la Durée planifiée qui a été promise pour la première fois au client. Nous supposons que la ligne de base d’origine contienne ces informations (et nous prévoyons désormais de demander à nos chefs de projet de planifier leurs projets de cette manière afin que nous puissions capturer des données précises). Nous avons capturé cette valeur de durée à partir de la ligne de base d’origine et l’avons appelée Première durée.

En divisant la durée réelle par la durée planifiée ou la première durée, nous obtenons un nombre qui peut nous indiquer à quel point nous nous sommes rapprochés de la cible. Si la durée planifiée ou la première durée est égale à la durée réelle, l’index est égal à 1. Si la durée réelle est supérieure à 1, la réponse sera supérieure à 1. Plus le nombre est élevé, plus nous avons fait du mal lorsque nous avons atteint notre date.

Donc, étant donné tout ce que j&#39;ai décidé d&#39;assigner des états à la fois pour la vitesse ajustée et pour le ratio travail/engagement comme suit :

* 1.1 ou au-dessous j&#39;ai appelé Excellent.
* 1.2 à 1.5 J&#39;ai appelé &quot;Pas Mauvais&quot;.
* 1.6 à 1.9 j&#39;ai appelé Pauvre.
* 2 ou plus j&#39;ai appelé Terrible.

**Question**

Que doit faire le travailleur pour suivre le temps nécessaire à la réalisation des projets ?

**Réponse**

Nous ne suivons pas les heures réelles passées à travailler sur les projets ici, nous ne faisons que suivre et comparer la durée. Mais si vous effectuez le suivi des heures et que vous souhaitez utiliser des heures réelles par rapport aux heures planifiées pour calculer la vitesse, vous pouvez faire ce même type de rapport en comparant les heures planifiées aux heures réelles. Vous souhaitez également capturer les heures planifiées à partir de la ligne de base d’origine.

**Question**

Pouvez-vous fournir des filtres utilisés pour Velocity ?

**Réponse**

J’ai utilisé deux règles de filtrage pour les rapports Velocity :

* Catégories &quot; ID &quot; Egal &quot; Données du projet WPI (il s’agit du formulaire personnalisé qui contenait tous les champs calculés. Je veux uniquement voir les projets qui utilisent ce formulaire personnalisé)
* Projet &quot; État &quot; Égal &quot; Terminé (je souhaite uniquement afficher les projets terminés car ils ont une valeur Durée réelle qui représente le temps nécessaire pour que tout soit fait. Les projets en cours ne fournissent pas de durée réelle précise pour calculer la vitesse)

J’ai également ajouté d’autres filtres pour garder mon rapport suffisamment petit pour le gérer pour le webinaire. Cependant, dans votre environnement de production, vous souhaiterez probablement voir tous les projets avec le formulaire personnalisé WPI pendant une période donnée. Vous pouvez filtrer selon la date d’achèvement du projet.

**Question**

Si vous copiez un projet, celui-ci contient-il les mêmes lignes de base que le nouveau projet ?

**Réponse**

Non, les lignes de base ne sont pas incluses dans le projet copié.

**Question**

Pour un processus d’approbation de tâche, pouvez-vous m’indiquer comment créer un rapport qui fournit un journal d’audit par tâche dans un projet avec un horodatage pour chaque approbateur ?

**Réponse**

Créez un rapport Tâche . Dans l’onglet Colonnes (mode), cliquez sur Ajouter une colonne. Dans la zone &quot;Afficher dans cette colonne :&quot;, saisissez &quot;approv&quot;. Vous y trouverez les différents champs de validation sur lesquels vous pouvez créer un rapport. Je vous suggère d’ajouter une colonne pour tout au début (à l’exception des identifiants), puis de voir quelles informations s’affichent.

Accédez ensuite à l’onglet Filtres et ajoutez une règle de filtrage pour :

Tâche &quot; Est Approbation > Egal &quot; Vrai. Cette option affiche uniquement les tâches auxquelles une approbation est associée.

Ajoutez d’autres filtres si nécessaire.

**Question**

Je voudrais créer un rapport de BAT. Une liste de projets montrant le nombre de bons à tirer et le nombre de versions de ce bon à tirer.

**Réponse**

Créez un rapport de document.

La vue par défaut affiche le numéro de version. Vous pouvez laisser cela à cet endroit, mais vous pouvez modifier n’importe quelle autre colonne.

Regroupez le rapport par nom de projet.

Filtrer le rapport par version actuelle : l’ID de bon à tirer n’est pas vide.

Vous obtiendrez ainsi la liste de tous les bons à tirer de chaque projet. Il y aura une ligne pour chaque BAT et affichera le numéro de version (qui sera le même que le nombre total de versions).

**Question**

Pouvez-vous utiliser la vitesse au niveau de la tâche ? Plutôt qu’au niveau du projet ?

**Réponse**

Oui, mais vous devez copier le formulaire personnalisé du projet et créer un formulaire personnalisé de tâche à partir de celui-ci. Vous devrez ensuite modifier le calcul dans le champ Date de première validation et remplacer la référence par &quot;Ligne de base par défaut&quot; par &quot;Tâche de ligne de base par défaut&quot;. Faites de même pour la première durée. Ensuite, vous pouvez joindre le formulaire personnalisé de tâche à toutes les tâches que vous souhaitez mesurer. Vous devrez créer des rapports de tâche plutôt que des rapports de projet pour ceux-ci. Cependant, vous devrez toujours vous assurer que la ligne de base du projet d’origine est définie comme ligne de base par défaut. Toutes les données de tâche sont conservées dans la même ligne de base que les données du projet.

**Question**

La première date de validation doit-elle être définie manuellement par le propriétaire du projet ? Ou peut-il s&#39;extraire de champs existants ?

**Réponse**

La date de première validation est capturée à partir de la ligne de base par défaut. Tant que la ligne de base par défaut est la ligne de base d’origine, elle affiche la date d’achèvement prévue du projet au moment où elle a été définie sur l’état actuel pour la première fois.

**Question**

Les champs calculés dans les formulaires personnalisés doivent toujours être actualisés périodiquement correctement ? Ou cela se produira-t-il automatiquement du jour au lendemain (ou à un autre déclencheur) ?

**Réponse**

Les champs calculés sont recalculés :

* Lorsqu’un utilisateur modifie l’objet
* Lors d’une modification en masse avec l’option Recalculer les expressions personnalisées activée
* Modifications du formulaire avec l’option &quot;Mettre à jour les calculs précédents&quot; sélectionnée

**Question**

Si la vitesse prend en compte la durée, le pourcentage terminé dans la préférences du projet doit-il être basé sur la durée ?

**Réponse**

Non, l’option Préférences du projet ne fait référence qu’au mode de calcul du pourcentage d’achèvement. La valeur duration elle-même n’est pas affectée par ce paramètre.

**Question**

Quelle est la différence entre la première et la durée du plan ?

**Réponse**

Première durée est le nombre de jours que vous avez initialement promis au client que le projet prendrait. Nous obtenons ce nombre à partir de la ligne de base d’origine qui a été enregistrée lorsque le projet a été modifié de Planification à En cours.

Durée planifiée est le nombre de jours entre le début du projet et la date d’achèvement prévue. Au départ, ces deux durées sont identiques, mais si le projet a déjà été replanifié et que la date d’achèvement prévue a été modifiée, la durée planifiée l’a également été.

La valeur des rapports Velocity provient du fait que nous pouvons voir à quel point la durée planifiée a changé par rapport à la première durée. Nous pouvons voir cela dès le début de l’enregistrement des lignes de base, car les projets ont changé de Planification à Actuel.

**Question**

Les objets Worker peuvent-ils être définis par couleur afin qu’ils soient identiques dans tous les rapports ?

**Réponse**

Si vous effectuez un groupement par Affecté à &quot; Nom dans un rapport de tâche, vous pouvez attribuer une couleur à des programmes de travail spécifiques dans l’onglet Graphique . Choisissez simplement l’option Couleurs personnalisées en regard de la zone Affectée à &quot; Nom dans l’onglet Graphique et ajoutez une couleur pour chaque programme de travail.

**Question**

Je tente de déterminer s’il est possible de créer un tableau de bord avec une zone qui examine un formulaire personnalisé au niveau de la tâche pour voir s’il est présent et secondaire si certains champs ne sont pas vides. Est-ce possible ?

**Réponse**

Voyons si je comprends votre question. Supposons que j’ai un formulaire personnalisé de tâche appelé Tammy Form avec un champ nommé Tammy Field.

Vous souhaitez un rapport de tâche qui affiche toutes les tâches auxquelles est associé Tammy Form et où Tammy Field a une valeur.

Oui, vous pouvez le faire. Vous avez simplement besoin d’un filtre dans votre rapport de tâches avec deux règles de filtrage :

Catégories &quot; ID égal à formulaire Tammy

Tâche &quot; Le Champ Tammy N’Est Pas Vide

**Question**

Existe-t-il un moyen de créer un rapport pour rechercher un document nommé spécifique dans la bibliothèque de documents ? Partie du tableau de bord que nous voulons mesurer s’il existe certains documents.

**Réponse**

Oui. Vous devez créer un rapport Document . Il semble que vous souhaitiez attribuer un nom de document spécifique chaque fois que vous exécutez le rapport. Dans ce cas, je vous recommande d’accéder aux Options de rapport et de sélectionner les invites de rapport. Ajoutez une invite pour Document > Nom.

**Question**

Pouvez-vous choisir une couleur/valeur hexadécimale non répertoriée dans l&#39;onglet graphique mais c&#39;est une nouvelle couleur qui est une nouvelle valeur hexadécimale, par exemple une nouvelle couleur des couleurs de ma marque pour me permettre de personnaliser les rapports ?

**Réponse**

Oui, vous pouvez saisir n’importe quel code de RGB que vous avez pu trouver. Il s’agit d’un code standard qui indique la quantité de rouge, vert et bleu contenue dans la couleur. Workfront accepte toute valeur hexadécimale de 000000 à FFFFF. Ainsi, si vous connaissez le code de votre couleur de marque, vous pouvez l’utiliser.

**Question**

Pouvez-vous préciser à nouveau la définition des rapports dans le tableau de bord (indiquez la manière dont chaque rapport mesure) ?

**Réponse**

Graphique d’état de vitesse ajusté

> Cela montre à quel point nous avons bien réussi à exécuter les projets à temps en comparant la durée réelle du projet à la durée planifiée. La durée planifiée ayant été ajustée à mesure que le projet a été replanifié au cours de son cycle de vie.

Graphique d’état du ratio travail-validation

> Cela montre à quel point nous avons bien réussi à exécuter les projets à temps en comparant la durée réelle du projet à la première durée. Première durée étant l’heure d’origine à laquelle nous avons promis au client que le projet serait terminé. La première durée a été calculée à partir de la valeur Durée du projet lorsqu’elle a été changée pour la première fois de l’état Planification à l’état actuel. Il s’agit de la durée enregistrée dans la ligne de base initiale.

Rapport Liste des états de Velocity

> Ce rapport contient tous les champs personnalisés calculés et les dates significatives pour les mêmes projets dans les graphiques. Son objectif est de nous permettre de vérifier nos calculs et d’obtenir plus d’informations si vous le souhaitez.

**Question**

Comment avez-vous ajouté les nouvelles données à l’axe X ?

**Réponse**

Lorsque vous effectuez un groupement sur n’importe quel élément d’un rapport, vous pouvez créer un graphique. Vous pouvez ensuite définir l’axe X ou Y dans l’onglet Graphique .

**Question**

Pouvez-vous passer en revue la différence entre la première durée et la durée réelle ?

**Réponse**

Première durée est le nombre de jours que vous avez initialement promis au client que le projet prendrait. Nous obtenons ce nombre à partir de la ligne de base d’origine qui a été enregistrée lorsque le projet a été modifié de Planification à En cours.

Durée réelle est le nombre de jours entre le début de votre projet et la date d’achèvement réelle.

**Question**

Comment le facteur de base du projet est-il pris en compte dans ce rapport ?

**Réponse**

La ligne de base d’origine du projet contient la date d’achèvement prévue et la durée planifiée qui existaient lorsque le projet a été modifié pour la première fois en état actuel. Si votre processus devait planifier le projet avant de le définir sur Actuel , cela représenterait la date à laquelle vous vous êtes engagé à terminer le projet.

**Question**

Existe-t-il un moyen d’appliquer en masse le nouveau formulaire aux anciens projets ?

**Réponse**

Oui, vous pouvez sélectionner plusieurs projets dans une liste. Lorsque vous procédez de la sorte, une option &quot;Modifier&quot; s’affiche en haut à gauche de votre liste. Cliquez sur Modifier lorsque plusieurs objets sont sélectionnés pour effectuer ce que nous appelons &quot;modification en masse&quot;. Vous pouvez ainsi ajouter un formulaire personnalisé à plusieurs projets.

Un raccourci pour ajouter des formulaires personnalisés à un grand nombre de projets consiste à créer un rapport que vous filtrez pour n’inclure que les projets de votre choix. Ensuite, au lieu de sélectionner des projets individuellement, cochez la case située au-dessus de la première case de la liste pour sélectionner la liste entière.

**Question**

Est-il possible de supprimer les entrées en double dans le groupement d’un rapport d’affectation, mais pas entre les regroupements ?

**Réponse**

Voici la meilleure façon de penser aux groupements dans les rapports de listes :

Tout d’abord, vous pouvez contrôler les éléments qui s’affichent dans la liste à l’aide de l’onglet Filtre . Il n’y aura pas d’entrées en double. Le filtre est appliqué à chaque objet. S’il passe par le filtre, il apparaîtra une fois dans la liste, s’il n’apparaît pas du tout.

Le regroupement suivant est appliqué à la liste filtrée. Un regroupement identifie une chose au sujet des objets de la liste, comme le nom du portefeuille dans lequel il se trouve (vous ne pouvez pas les regrouper sur une liste d’objets, mais sur une seule chose). Tous les objets ayant la même valeur apparaissent alors dans ce regroupement, comme tous les projets du même portfolio. Tous les projets pour lesquels aucun portefeuille n’est sélectionné s’affichent dans le regroupement nommé &quot;Aucune valeur&quot;.

Il n’existe donc aucun moyen pour qu’un objet apparaisse dans plusieurs regroupements. Et si un objet apparaît dans la liste est entièrement contrôlé par le filtre (et si la personne qui exécute le rapport a les droits de l’afficher).

**Question**

recommanderiez-vous un autre rapport pour suivre Velocity ? Une recommandation de haut niveau est géniale parce que je sais qu&#39;il n&#39;y a pas assez de temps pour entrer dans les détails.

**Réponse**

Comme pour tout rapport, la première chose à faire est de décider ce que vous voulez savoir. L’étape suivante consiste à accéder à ces informations, ce qui signifie dans certains cas que vous devez commencer à les suivre.

Une des raisons pour lesquelles j&#39;ai décidé de comparer la durée réelle à deux types de durée planifiée était que je pensais qu&#39;elle fournissait des informations intéressantes sur la vitesse. Les données étaient déjà disponibles, je n&#39;avais donc pas besoin de commencer à les suivre. Avec quelques calculs, je pourrais extraire les données sous forme de rapport.

Mais vous pouvez tout aussi bien décider de suivre d’autres informations sur les tâches ou les projets sur lesquels créer des rapports.

Workfront ne comporte aucun rapport de vitesse intégré. Je vous recommande donc, ainsi qu’à votre équipe, de réfléchir sur ce que vous souhaitez savoir pour déterminer la vitesse, puis de voir ce dont vous avez besoin pour effectuer le suivi.

**Question**

Pouvez-vous calculer quoi que ce soit au niveau COLONNE ? Au lieu d’appeler un CHAMP calculé à partir d’un formulaire personnalisé ?

**Réponse**

Il aurait été possible d’utiliser une expression de valeur en mode texte pour effectuer ces calculs. Nous n&#39;aurions pas pu faire la première durée ou la première date de validation, cependant, nous avions besoin de capturer ceux-ci dans un endroit où ils ne changeraient pas.

En ce qui concerne l’état du ratio travail/validation et l’état de vitesse ajusté, il s’agissait de champs personnalisés afin que nous puissions les utiliser dans l’onglet Graphique . L&#39;onglet Graphique ne reconnaît pas les regroupements en mode texte. Il doit s&#39;agir de champs personnalisés. Et comme nous avions besoin d&#39;un ratio travail/validation et d&#39;une vitesse ajustée pour calculer ces états, nous avions également besoin qu&#39;ils soient des champs personnalisés. Dans ce cas, ils devaient tous être des champs personnalisés, mais il est toujours bon de considérer les deux façons et de choisir ce qui fonctionnera le mieux. Merci pour la question.

**Question**

Nos projets changent souvent en raison des délais ou des changements des clients. Notre rapport pourrait tout montrer comme &quot;terrible&quot;. Quelle est la recommandation pour le suivi des raisons de changement ? Nous avons envisagé d’ajouter au niveau du document un formulaire personnalisé qui indique les raisons d’un changement (interne ou client), mais nous nous demandons quelle est la bonne pratique.

**Réponse**

Il est recommandé d’utiliser une liste déroulante pour en effectuer le suivi. Ajoutez autant de &quot;raisons&quot; que vous pouvez y penser, puis une option &quot;autre&quot; pour capturer une raison qui ne figure pas dans la liste. Si cette nouvelle raison apparaît ou devient courante, ajoutez-la à votre liste déroulante. Vous pouvez facilement créer des rapports sur les éléments d’une liste déroulante et vous pouvez les regrouper sur ce champ (vous ne pouvez pas les regrouper dans des cases à cocher ou une liste déroulante à sélection multiple).

Juste un autre commentaire à ce sujet. Vous pouvez ne pas inclure tous les projets dans vos rapports Velocity. Si vous réparez des bogues ou si vous &quot;allez où personne n’est allé auparavant&quot;, vous ne prenez probablement pas le même engagement à une date d’achèvement que si vous construisez une maison que vous avez construite plusieurs fois auparavant.

Veillez donc à concentrer vos rapports de vitesse sur les endroits où ils peuvent vous aider à atteindre vos objectifs.

**Question**

Si je définit la ligne de base par défaut d’un projet sur &quot;Original&quot;, puis que je retire le projet de l’état actuel et le réactualise, changera-t-elle ma ligne de base par défaut ?

**Réponse**

Oui. Chaque fois que vous définissez l’état sur Actuel, vous obtenez une nouvelle ligne de base et ce sera la nouvelle valeur par défaut. Cependant, toutes les lignes de base précédentes existent toujours et vous pouvez définir manuellement la ligne de base d’origine pour qu’elle soit à nouveau la ligne de base par défaut.

**Question**

Existe-t-il un moyen de configurer dans un rapport les champs modifiables ? Puis-je définir des restrictions pour certains champs ?

**Réponse**

Vous pouvez restreindre les droits d’affichage et de modification des champs d’un formulaire personnalisé. Vous devez inclure les champs dans une section. Dans les paramètres de la section, vous pouvez choisir les droits nécessaires pour que les utilisateurs puissent afficher ou modifier les champs de la section.

**Question**

Pouvez-vous créer un rapport qui recherche un document nommé spécifique dans la bibliothèque de documents ?

**Réponse**

Oui. Vous devez créer un rapport Document . Il semble que vous souhaitiez attribuer un nom de document spécifique chaque fois que vous exécutez le rapport. Dans ce cas, je vous recommande d’accéder aux Options de rapport et de sélectionner les invites de rapport. Ajoutez une invite pour Document > Nom.

**Question**

Dans les rapports, pourquoi les valeurs sont-elles disponibles en colonne, mais pas en sélection ou regroupement ? Par exemple : Source du problème.

**Réponse**

La principale raison pour laquelle une colonne peut être visible, mais n’est pas disponible pour le regroupement, est qu’elle peut contenir une liste, comme des cases à cocher, des champs personnalisés ou des affectations de tâche. Le regroupement sur une liste n’est pas autorisé.

**Question**

Comment puis-je séparer dans un rapport (par quels champs) le moment où la saisie des heures a eu lieu et celui où les heures ont été réellement effectuées ?

**Réponse**

Le champ Date d’entrée de l’objet Heure fait référence à la date à laquelle les heures ont été travaillées. La date d’entrée est ainsi différente de celle des autres objets, où elle correspond à la date de création de l’objet. Même s’il n’existe pas de date de création pour les heures, il existe une &quot;Date de dernière mise à jour&quot;, qui est initialement la date de création, puis toute date à laquelle l’heure a été modifiée par la suite.

**Question**

Du point de vue des rapports, comment accéder aux données de base ? J’ai un projet avec plusieurs lignes de base. Je veux voir comment des tâches individuelles ont été planifiées dans chaque ligne de base. Existe-t-il un moyen d’écrire un rapport qui affichera le plan de projet pour chaque ligne de base ?

**Réponse**

Un rapport indique les champs que vous souhaitez afficher pour la ligne de base actuellement définie comme valeur par défaut. Vous pouvez donc modifier la ligne de base et actualiser votre rapport afin d’afficher les champs correspondant à la nouvelle ligne de base.

Mais si vous souhaitez afficher des informations sur vos tâches sous forme graphique, vous pouvez le faire à l’aide de la fonctionnalité de graphique de Gantt. Activez Gantt dans une liste de tâches (à l’aide de l’icône Gantt en haut à droite en regard de l’enregistrement automatique), puis accédez à l’icône Paramètres juste en bas à droite et cliquez dessus. Cochez la case Ligne de base pour afficher toutes les lignes de base. Vous pouvez les sélectionner individuellement et afficher les modifications apportées à vos tâches dans la vue Gantt.

**Question**

Comment créer un rapport pour retrouver les modifications de son état pour une période définie, par exemple le mois dernier.

**Réponse**

La fonctionnalité Analytics de Workfront vous permet d’afficher facilement les données historiques, y compris les modifications d’état.

Vous pouvez également obtenir des informations sur les modifications d’état à l’aide d’un rapport Remarque . Vous pouvez filtrer pour afficher les modifications d’état sur les projets si vous effectuez le suivi du champ État du projet .

Pour commencer, accédez à Configuration > Interface > Mettre à jour les flux et assurez-vous que l’état du projet est l’un des champs intégrés qui est suivi. Si ce n’est pas le cas, vous devez l’ajouter.

Créez maintenant un rapport Remarque et procédez comme suit :

Dans l’onglet Colonnes (affichage) :

* Remplacez la colonne &quot;Texte de la remarque&quot; pour &quot;Texte de l’audit&quot;. Cette opération affiche des informations sur le changement d’état de et de .
* Laissez le &quot;Projet&quot; : Nom&quot; et les colonnes &quot;Date d’entrée&quot;
* Cliquez sur la colonne &quot;Date d’entrée&quot;, puis cochez l’option &quot;Trier par cette colonne&quot; dans le panneau Paramètres de colonne. Si vous souhaitez voir les modifications d’état les plus récentes en haut, triez-les par ordre décroissant.

Dans l&#39;onglet Groupements :

* Groupe par projet : Nom

Dans l’onglet Filtres , créez les règles de filtrage suivantes :

* Remarque &quot; Type d’audit &quot; Égal &quot; Changement d’état
* ajoutez toute règle supplémentaire à filtrer selon la Date d’entrée de la note. Vous préférerez peut-être ne pas utiliser cette option Filtres et utiliser une invite de rapport à la place.
* Filtrez selon vos besoins sur le projet, le portefeuille ou d’autres données.

**Question**

En tant que planificateur, pouvez-vous extraire des rapports pour d’autres utilisateurs ?

**Réponse**

Un planificateur peut créer des rapports et les partager avec n’importe quel utilisateur, même avec des personnes qui ne sont pas des utilisateurs. Lors de l’affichage du rapport, accédez à Actions de rapport > Partage, puis cliquez sur l’icône en forme d’engrenage en haut à droite de la zone Accès aux rapports . Sélectionnez &quot;Rendre ceci public aux utilisateurs externes&quot;. option. Vous pouvez copier le lien fourni et l’envoyer à n’importe qui. Le rapport s’affichera en temps réel dans leur navigateur.
