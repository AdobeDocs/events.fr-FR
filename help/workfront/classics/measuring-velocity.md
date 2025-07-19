---
title: Demandez à l’expert - Mesure de la vitesse
description: Découvrez comment mesurer et suivre la vitesse à l’aide  [!DNL Workfront]  rapports. Cet atelier a été enregistré le 14 août 2019.
doc-type: feature video
team: Technical Marketing
jira: KT-9912
last-substantial-update: 2023-08-15T00:00:00Z
exl-id: 83053de2-e386-4243-a9c8-a2ad9d51790f
duration: 4630
source-git-commit: 91f20c3e9ee5ae5b259d5cb3da476974acdc6585
workflow-type: tm+mt
source-wordcount: '3962'
ht-degree: 0%

---

# Demandez à l’expert - Mesure de la vitesse

Découvrez comment mesurer et suivre la vitesse à l’aide des rapports [!DNL Workfront]. Cet atelier a été enregistré le 14 août 2019.

>[!VIDEO](https://video.tv.adobe.com/v/341057/?quality=12)

## Champs personnalisés utilisés dans la présentation

Gagnez du temps en copiant et collant les calculs ci-dessous.

>[!NOTE]
>
>La syntaxe des calculs des champs personnalisés a changé depuis la présentation de 2019, mais les concepts et autres instructions présentés dans la présentation restent exacts.
>>**Les calculs inclus ci-dessous ont été mis à jour pour prendre en compte les dernières règles de syntaxe.**

**Première date d&#39;engagement**

Format : Date

Calcul :

```
IF(ISBLANK({DE:First Commit Date}),{defaultBaseline}.{plannedCompletionDate},{DE:First Commit Date})
```

**Première durée**

Format : Texte

Calcul :

```
IF(ISBLANK({DE:First Duration}),{defaultBaseline}.{durationMinutes},{DE:First Duration})
```

**Rapport travail-engagement**

Format :Number

Calcul :

```
ROUND(DIV({actualDurationMinutes},{DE:First Duration}),1)
```

**Statut du ratio travail-engagement**

Format :Text

Calcul :

```
IF({DE:Work-to-Commit Ratio}>2,"Terrible",IF({DE:Work-to-Commit Ratio}>1.6,"Poor",IF({DE:Work-to-Commit Ratio}>1.2,"Not Bad","Excellent")))
```

**Vitesse Ajustée**

Format :Number

Calcul :

```
ROUND(DIV({actualDurationMinutes},{durationMinutes}),1)
```

**Statut de vitesse ajusté**

Format :Text

Calcul :

```
IF({DE:Adjusted Velocity}>2,"Terrible",IF({DE:Adjusted Velocity}>1.6,"Poor",IF({DE:Adjusted Velocity}>1.2,"Not Bad","Excellent")))
```

## Questions/Réponses

**Question**

Bonjour, merci d’avoir organisé ce webinaire. J&#39;ai une question sur Field in Workfront. Dans notre système, nous avons créé un champ personnalisé appelé « État » qui est une combinaison de Statut et de Condition. Ce champ d&#39;état contient beaucoup de statues dans des milliers de projets, ce qui est très important pour notre extrait de données Tableau. Cependant, nous voulons maintenant éliminer ce champ et utiliser le champ Condition, le champ natif à la place. Avez-vous une idée de la manière dont je peux retourner ce champ sans perdre de données ? Tout ce que je peux penser de faire sans perdre de données en ce moment, c&#39;est de les faire passer manuellement d&#39;un projet à un autre.

**Réponse**

Dans une situation comme celle-ci, vous pouvez utiliser le filtrage et la modification en masse pour semi-automatiser la tâche de remplissage du champ Condition en fonction de votre champ personnalisé État .

La procédure est la suivante :

1. Déterminez les valeurs d’état à mapper aux valeurs de condition. Par exemple, supposons que vous ayez une valeur d’état « Tard » et « Très tard » qui correspondent toutes deux à une valeur de condition « En difficulté »
1. Créez un rapport de projet affichant tous les projets dont la valeur d’état est « En retard » et « Très tard »
1. Exécutez le rapport. Veillez à afficher tous les projets (voir les options dans le coin inférieur droit du rapport)
1. Cochez la case en haut à gauche du rapport dans la barre avec les en-têtes de colonne. Tous les projets du rapport seront sélectionnés
1. Cliquez sur le bouton Modifier situé au-dessus de la liste des rapports
1. Définissez le Type de condition sur Manuel
1. Définir le champ Condition sur En difficulté
1. Cliquez sur Enregistrer les modifications


**Question**

Comment est défini le paramètre Excellent, Pas mal, etc. ?

**Réponse**

Ce n&#39;était qu&#39;un exemple, mais voici comment je l&#39;ai configuré. J&#39;ai d&#39;abord calculé deux index :

Vitesse Ajustée

La formule pour cela est Durée réelle/Durée prévue (qui est stockée dans le champ Durée dans un projet). Comme la durée planifiée du projet peut changer à chaque nouvelle planification du projet, la durée planifiée représente la replanification finale.

Ratio travail-engagement

Cette formule est similaire à la vitesse ajustée, si ce n’est qu’au lieu d’utiliser la valeur de durée prévue de la replanification finale, nous voulons utiliser la durée prévue promise au client pour la première fois. Nous supposons que la base de référence originale contient ces informations (et nous prévoyons désormais de demander à nos chefs de projet de planifier leurs projets de cette manière afin que nous puissions recueillir des données précises). Nous avons capturé cette valeur de durée à partir de la ligne de base d&#39;origine et l&#39;avons appelée Première durée.

En divisant la durée réelle par la durée prévue ou la première durée, nous obtenons un nombre qui peut nous indiquer à quel point nous avons été proches de l’objectif. Si la durée prévue ou la première durée sont égales à la durée réelle, l&#39;index sera égal à 1. Si la durée réelle est supérieure, la réponse sera supérieure à 1. Plus le nombre est élevé, plus nous avons mal respecté notre date.

Ainsi, compte tenu de tout ce que j’ai décidé d’attribuer aux statuts pour la vitesse ajustée et le rapport travail/engagement, comme suit :

* 1.1 ou moins J&#39;ai appelé Excellent.
* 1.2 à 1.5 J&#39;ai appelé Pas Mauvais.
* 1.6 à 1.9 J&#39;ai appelé Poor.
* 2 ou plus j&#39;ai appelé Terrible.

**Question**

Que doit faire le travailleur pour suivre le temps qu&#39;il faut pour réaliser les projets?

**Réponse**

Nous ne faisons pas le suivi des heures réellement consacrées à ces projets, nous ne faisons que suivre et comparer la durée. Mais si vous suivez des heures et souhaitez utiliser des heures réelles sur des heures planifiées pour calculer la vitesse, vous pouvez créer ce même type de rapport en comparant les heures planifiées aux heures réelles. Vous souhaiteriez également capturer les heures planifiées à partir de la planification initiale.

**Question**

Pouvez-vous fournir les filtres utilisés pour Velocity ?

**Réponse**

J’ai utilisé deux règles de filtrage pour les rapports Velocity :

* Catégories >> ID >> Égal >> Données de projet API (il s’agit du formulaire personnalisé qui contenait tous les champs calculés. Je souhaite uniquement afficher les projets qui utilisent ce formulaire personnalisé)
* Projet >> Statut >> Égal à >> Terminé (je souhaite uniquement afficher les projets terminés, car ils ont une valeur de durée réelle qui représente la durée nécessaire pour tout terminer. Les projets actuels ne fourniraient pas une durée réelle précise pour le calcul de la vitesse)

J’ai également ajouté d’autres filtres pour que mon rapport reste suffisamment petit pour être géré pendant le webinaire, mais dans votre environnement de production, vous souhaiterez probablement voir tous les projets avec le formulaire personnalisé API pendant une période donnée. Vous pouvez filtrer par date d&#39;achèvement effective du projet.

**Question**

Si vous copiez un projet, celui-ci conserve-t-il les mêmes lignes de base dans le nouveau projet ?

**Réponse**

Non, les références ne sont pas incluses dans le projet copié

**Question**

Dans le cas d&#39;un processus d&#39;approbation de tâche, pouvez-vous me montrer comment créer un rapport qui fournit un journal d&#39;audit par tâche dans un projet avec un horodatage pour chaque approbateur ?

**Réponse**

Créez un rapport de tâche. Dans l’onglet Colonnes (Vue) , cliquez sur Ajouter une colonne. Dans la zone « Afficher dans cette colonne : », saisissez « approuver ». Vous verrez ainsi les différents champs d’approbation sur lesquels vous pouvez créer des rapports. Je vous suggère d’ajouter d’abord une colonne pour tout (à l’exception des ID), puis vous pouvez voir les informations affichées.

Accédez ensuite à l’onglet Filtres et ajoutez une règle de filtrage pour :

Tâche >> Est une approbation >> Est égal à >> Vrai. Seules les tâches ayant une approbation sont affichées.

Ajoutez des filtres supplémentaires si nécessaire.

**Question**

Je voudrais créer un rapport de BAT. Liste de projets indiquant le nombre d’épreuves dont ils disposent et le nombre de versions de cette épreuve.

**Réponse**

Créez un rapport de document.

La vue par défaut affiche le numéro de version. Vous voudrez la laisser là, mais vous pouvez modifier n&#39;importe quelle autre colonne.

Regroupez les rapports par nom de projet.

Filtrer le rapport par version actuelle :Proof l’ID n’est pas vide.

Vous obtiendrez ainsi une liste de toutes les épreuves de chaque projet. Elle comporte une ligne pour chaque BAT et affiche le numéro de version (qui sera identique au nombre total de versions).

**Question**

Pouvez-vous utiliser la vitesse au niveau de la tâche ? Plutôt qu&#39;au niveau du projet ?

**Réponse**

Oui, mais vous devrez copier le formulaire personnalisé du projet et créer un formulaire personnalisé de tâche à partir de celui-ci. Vous devez ensuite modifier le calcul dans le champ Date du premier engagement et remplacer la référence à « Planification par défaut » par « Tâche Planification par défaut ». Faites de même pour la première durée. Ensuite, vous pouvez joindre le formulaire personnalisé de tâche à toutes les tâches que vous souhaitez mesurer. Vous devrez créer des rapports de tâches au lieu de rapports de projet pour ces tâches. Cependant, vous devez toujours vous assurer que la planification initiale du projet d&#39;origine est définie comme planification initiale par défaut. Toutes les données de la tâche sont conservées dans la même ligne de base avec les données du projet.

**Question**

La première date de validation doit-elle être définie manuellement par le propriétaire du projet ? Ou pourrait-il extraire des champs existants ?

**Réponse**

La date de premier engagement est capturée à partir de la ligne de base par défaut. Tant que la ligne de base par défaut est la ligne de base d&#39;origine, la date d&#39;achèvement prévue du projet s&#39;affiche au moment où elle a été définie pour la première fois sur le statut Actuel.

**Question**

Les champs calculés des formulaires personnalisés doivent toujours être régulièrement actualisés. Ou cela se produira-t-il automatiquement du jour au lendemain (ou à un autre déclencheur) maintenant ?

**Réponse**

Les champs calculés sont recalculés :

* Lorsqu’un utilisateur modifie l’objet
* Modification en bloc avec les expressions personnalisées de recalcul activées
* Modifications du formulaire avec l&#39;option &#39;Mettre à jour les calculs précédents&#39; sélectionnée

**Question**

Si la vitesse prend en compte la durée, le pourcentage d’achèvement dans les préférences du projet doit-il être basé sur la durée ?

**Réponse**

Non, l’option Préférences du projet fait uniquement référence à la manière dont le pourcentage d’achèvement est calculé. La valeur de durée elle-même n’est pas affectée par ce paramètre.

**Question**

Quelle est la différence entre la durée du premier plan et celle du plan ?

**Réponse**

La première durée correspond au nombre de jours que vous avez promis au client pour le projet. Nous obtenons ce chiffre à partir de la base de référence d’origine qui a été enregistrée lorsque le projet est passé de Planification à Actuel.

La Durée planifiée correspond au nombre de jours entre le début de votre projet et la date d&#39;achèvement planifiée. Au départ, ces deux durées sont identiques, mais si le projet a jamais été replanifié et que la date d’achèvement prévue a changé, la durée prévue a également changé.

La valeur des rapports Velocity vient de notre capacité à voir combien la durée prévue a changé depuis la première durée. Nous pouvons le constater dès le début de l&#39;enregistrement des niveaux de référence, lorsque les projets sont passés de Planification à Actuel.

**Question**

Pouvez-vous définir les programmes de travail par couleur afin qu’ils soient identiques dans tous les rapports ?

**Réponse**

Si vous regroupez par Affecté à >> Nom dans un rapport de tâche, vous pouvez affecter une couleur à des programmes de travail spécifiques dans l&#39;onglet Graphique. Sélectionnez simplement l’option Couleurs personnalisées en regard de la zone Affecté à > Nom dans l’onglet Graphique et ajoutez une couleur pour chaque programme de travail.

**Question**

J’essaie de déterminer s’il est possible de créer un tableau de bord avec une zone qui examine un formulaire personnalisé au niveau de la tâche pour voir s’il est présent et secondaire si certains champs ne sont pas vides. Est-ce possible ?

**Réponse**

Voyons si je comprends votre question. Supposons que je dispose d’un formulaire personnalisé de tâche appelé Formulaire de saisie semi-automatique contenant un champ nommé Champ de saisie semi-automatique.

Vous souhaitez obtenir un rapport de tâches qui affichera toutes les tâches auxquelles le formulaire Tammy est joint et où le champ Tammy a une certaine valeur.

Oui, vous pouvez le faire. Il vous suffirait d’un filtre dans votre rapport de tâche avec deux règles de filtrage :

Catégories >> Formulaire de tammy d&#39;ID égal

Le Champ Tâche >> Tammy N’Est Pas Vide

**Question**

Existe-t-il un moyen de créer un rapport pour rechercher un document nommé spécifique dans la bibliothèque de documents ? Partie du tableau de bord que nous voulons mesurer si certains documents existent.

**Réponse**

Oui. Vous devez créer un rapport de document. Il semble que vous souhaitiez fournir un nom de document spécifique chaque fois que vous exécutez le rapport. Si tel est le cas, je vous recommande d’accéder à Options de rapport et de sélectionner des invites de rapport. Ajoutez une invite pour Document > Nom.

**Question**

Pouvez-vous choisir une couleur/valeur hexadécimale qui n’est pas répertoriée dans l’onglet du graphique, mais qui correspond à une nouvelle couleur, par exemple une nouvelle couleur de mes couleurs de marque pour me permettre de personnaliser les rapports ?

**Réponse**

Oui, vous pouvez saisir n’importe quel code RGB que vous avez pu trouver. Il s’agit d’un code standard qui indique la quantité de rouge, de vert et de bleu contenue dans la couleur. Workfront accepte toute valeur hexadécimale comprise entre 000000 et FFFFFF. Ainsi, si vous connaissez le code de la couleur de votre marque, vous pouvez l’utiliser.

**Question**

Pourriez-vous reformuler la définition des rapports dans le tableau de bord (en indiquant ce que chaque rapport mesure) ?

**Réponse**

Graphique de statut de vitesse ajusté

> Cela montre à quel point nous avons réussi à terminer les projets dans les délais en comparant la durée réelle du projet à la durée prévue. La durée prévue a été ajustée au fur et à mesure de la replanification du projet pendant son cycle de vie.

Graphique d&#39;état du ratio travail-engagement

> Cela montre à quel point nous avons réussi à terminer les projets dans les délais en comparant la durée réelle du projet avec la première durée. La première durée étant le temps original que nous avons promis au client que le projet prendrait pour se terminer. La première durée a été calculée à partir de la valeur Durée du projet lorsqu&#39;il a été modifié pour la première fois du statut Planifiée au statut Actuelle. Il s’agissait de la durée enregistrée dans la ligne de base d’origine.

Rapport de liste de statut de vitesse

> Ce rapport contient tous les champs personnalisés calculés et les dates importantes pour les mêmes projets dans les graphiques. Son but est de nous permettre de vérifier nos calculs et d&#39;obtenir plus de détails si vous le souhaitez.

**Question**

Comment avez-vous ajouté les nouvelles données à l’axe des x ?

**Réponse**

Lorsque vous effectuez un regroupement dans un rapport, vous pouvez créer un graphique. Vous pouvez ensuite définir l’axe X ou Y dans l’onglet Graphique .

**Question**

Pouvez-vous nous expliquer la différence entre la première durée et la durée réelle ?

**Réponse**

La première durée correspond au nombre de jours que vous avez promis au client pour le projet. Nous obtenons ce chiffre à partir de la base de référence d’origine qui a été enregistrée lorsque le projet est passé de Planification à Actuel.

La durée réelle correspond au nombre de jours entre le début de votre projet et la date d&#39;achèvement effective.

**Question**

Comment la ligne de base du projet est-elle prise en compte dans ce rapport ?

**Réponse**

La planification initiale du projet contient la date d&#39;achèvement prévue et la durée prévue qui existait lorsque le projet a été modifié pour la première fois pour obtenir le statut Actuel. Si votre processus devait planifier le projet avant de le définir sur Actuel , cela représenterait la date à laquelle vous vous êtes engagé à terminer le projet.

**Question**

Existe-t-il un moyen d’appliquer en masse le nouveau formulaire aux anciens projets ?

**Réponse**

Oui, vous pouvez sélectionner plusieurs projets dans une liste. Lorsque vous effectuez cette opération, une option « Modifier » s’affiche en haut à gauche de votre liste. Cliquer sur Modifier lorsque plusieurs objets sont sélectionnés vous permet d’effectuer ce que nous appelons une « modification en bloc ». Vous pouvez ainsi ajouter un formulaire personnalisé à plusieurs projets.

Un raccourci permettant d’ajouter des formulaires personnalisés à un grand nombre de projets consiste à créer un rapport que vous filtrez afin d’inclure uniquement les projets de votre choix. Ensuite, au lieu de sélectionner les projets individuellement, il vous suffit de cocher la case au-dessus de la première case de la liste pour sélectionner la liste complète.

**Question**

Est-il possible de supprimer les entrées en double du regroupement dans un rapport d’affectation, mais pas entre les regroupements ?

**Réponse**

La meilleure façon d’envisager les regroupements dans des rapports de listes est la suivante :

Tout d’abord, vous pouvez contrôler les éléments qui s’affichent dans la liste à l’aide de l’onglet Filtre . Il n’y aura pas d’entrées en double. Le filtre est appliqué à chaque objet. S&#39;il passe par le filtre, il apparaîtra une fois dans la liste, sinon il n&#39;apparaîtra pas du tout.

Le regroupement suivant est appliqué à la liste filtrée. Un regroupement identifie une chose à propos des objets dans la liste, comme le nom du portfolio dans lequel il se trouve (vous ne pouvez pas regrouper une liste de choses, vous pouvez seulement en regrouper une seule). Tous les objets de même valeur apparaîtront alors dans ce regroupement, comme tous les projets d&#39;un même portfolio. Tous les projets pour lesquels aucun portefeuille n’a été sélectionné s’affichent dans le regroupement nommé « Aucune valeur ».

Par conséquent, aucun objet ne peut apparaître dans plusieurs regroupements. Et si un objet apparaît dans la liste est entièrement contrôlé par le filtre (et si la personne qui exécute le rapport a le droit de l’afficher).

**Question**

Recommanderiez-vous un autre rapport pour suivre la vitesse ? Une simple recommandation de haut niveau est excellente, car je sais que nous n&#39;avons pas suffisamment de temps pour l&#39;examiner en détail.

**Réponse**

Comme pour tout rapport, la première chose à faire est de décider ce que vous voulez savoir. L’étape suivante consiste à accéder à ces informations, ce qui, dans certains cas, signifie que vous devez commencer à les suivre.

L’une des raisons pour lesquelles j’ai décidé de comparer la durée réelle à deux types de durée planifiée était que je pensais qu’elle fournissait des informations intéressantes sur la vitesse. Les données étaient déjà disponibles, donc je n&#39;ai pas eu à commencer à les suivre. Avec quelques calculs, je pourrais extraire les données sous une forme que je pourrais rapporter.

Mais vous pouvez tout aussi bien décider de suivre d&#39;autres informations sur les tâches ou les projets sur lesquels établir des rapports.

Workfront ne dispose d’aucun rapport de vitesse intégré. Je vous recommande donc, à vous et à votre équipe, de réfléchir à ce que vous souhaitez savoir pour déterminer la vitesse, puis de voir ce que vous devez suivre.

**Question**

Êtes-vous en mesure de calculer quoi que ce soit au niveau COLONNE ? Au lieu d’appeler un CHAMP calculé à partir d’un formulaire personnalisé ?

**Réponse**

Il aurait été possible d&#39;utiliser une expression de valeur en mode texte pour effectuer ces calculs. Nous n&#39;aurions pas pu définir la première durée ou la première date d&#39;engagement, mais nous devions les consigner à un endroit où elles ne changeraient pas.

En ce qui concerne le statut du rapport travail-engagement et le statut de vitesse ajusté, il devait s’agir de champs personnalisés afin que nous puissions les utiliser dans l’onglet Graphique. L’onglet Graphique ne reconnaît pas les regroupements en mode texte ; ils doivent être des champs personnalisés. Et comme nous avions besoin du rapport travail-engagement et de la vitesse ajustée pour calculer ces statuts, nous avions besoin qu’ils soient également des champs personnalisés. Dans ce cas, ils devaient tous être des champs personnalisés, mais il est toujours préférable de tenir compte des deux aspects et de choisir ce qui fonctionnera le mieux. Merci pour la question.

**Question**

Nos projets changent souvent en raison de retards ou de changements de clients. Notre rapport peut tout montrer comme &#39;terrible&#39;. Qu’est-ce qu’une recommandation pour le suivi des raisons du changement ? Nous avons pensé à ajouter un formulaire personnalisé au niveau du document qui signale les raisons du changement (interne ou client), mais nous nous demandons quelle est la bonne pratique.

**Réponse**

La bonne pratique consiste à utiliser une liste déroulante pour effectuer le suivi. Insérez autant de « raisons » que vous pouvez imaginer dans cette liste pour commencer, puis ajoutez une option « autre » pour saisir une raison qui ne figure pas sur la liste. Si cette nouvelle raison apparaît ou devient courante, ajoutez-la à votre liste déroulante. Vous pouvez facilement créer des rapports sur des éléments dans une liste déroulante, puis effectuer un regroupement dans ce champ (vous ne pouvez pas effectuer de regroupement sur des cases à cocher ou une liste déroulante à sélection multiple).

Encore un commentaire à ce sujet. Il se peut que vous ne souhaitiez pas inclure tous les projets dans vos rapports Velocity. Si vous corrigez des bogues ou que vous « allez là où personne n&#39;est allé auparavant », vous ne prenez probablement pas le même type d&#39;engagement à une date d&#39;achèvement que si vous construisez une maison que vous avez construite plusieurs fois auparavant.

Veillez donc à concentrer vos rapports de vitesse sur les domaines où ils peuvent vous aider à atteindre vos objectifs.

**Question**

Si je définit la ligne de base par défaut d&#39;un projet sur « Original », puis que je retire le projet de la ligne de base actuelle et que je le remets sur la ligne de base actuelle, est-ce que cela modifiera ma ligne de base par défaut ?

**Réponse**

Oui. Chaque fois que vous changez le statut en Actuel, vous obtenez une nouvelle ligne de base qui sera la nouvelle valeur par défaut. Mais toutes les configurations de référence précédentes existent toujours et vous pouvez définir manuellement la configuration de référence d&#39;origine pour qu&#39;elle soit à nouveau la configuration de référence par défaut.

**Question**

Existe-t-il un moyen de configurer dans un rapport les champs modifiables ? Puis-je définir des restrictions pour certains champs ?

**Réponse**

Vous pouvez restreindre les droits d’affichage et de modification des champs d’un formulaire personnalisé. Vous devez inclure les champs dans une section. Dans les paramètres de la section, vous pouvez choisir les droits nécessaires pour que les utilisateurs puissent afficher ou modifier les champs de la section.

**Question**

Pouvez-vous créer un rapport qui recherche un document nommé spécifique dans la bibliothèque de documents ?

**Réponse**

Oui. Vous devez créer un rapport de document. Il semble que vous souhaitiez fournir un nom de document spécifique chaque fois que vous exécutez le rapport. Si tel est le cas, je vous recommande d’accéder à Options de rapport et de sélectionner des invites de rapport. Ajoutez une invite pour Document > Nom.

**Question**

Dans les rapports, pourquoi les valeurs sont-elles disponibles en tant que colonne, mais pas pour la sélection ou le regroupement ? Par exemple : Problème Source.

**Réponse**

La principale raison pour laquelle une colonne peut être visible mais n’est pas disponible pour le regroupement est qu’elle peut contenir une liste, comme des cases à cocher, un champ personnalisé ou des affectations de tâches. Le regroupement sur une liste n’est pas autorisé.

**Question**

Comment puis-je séparer dans un rapport (par quels champs) le moment où la saisie des heures a eu lieu et le moment où les heures ont été réellement effectuées ?

**Réponse**

Le champ Date de saisie de l&#39;objet Heure fait référence à la date à laquelle les heures ont été travaillées. Cela rend la date d&#39;entrée différente de celle des autres objets, où elle correspond à la date de création de l&#39;objet. Même s’il n’existe pas de date de création pour les heures, il existe une « Date de dernière mise à jour », qui correspond initialement à la date de création, puis à toute date à laquelle l’heure a été modifiée par la suite.

**Question**

Du point de vue de la création de rapports, comment pouvons-nous accéder aux données de référence ? J&#39;ai un projet avec plusieurs niveaux de référence. Je veux voir comment les différentes tâches ont été planifiées dans chaque ligne de base. Existe-t-il un moyen de rédiger un rapport qui affichera le plan du projet pour chaque niveau de référence ?

**Réponse**

Un rapport vous montre tous les champs que vous souhaitez afficher pour la ligne de base actuellement définie comme ligne de base par défaut. Vous pouvez donc modifier la ligne de base et actualiser votre rapport pour afficher les champs contenant la nouvelle ligne de base.

Mais si vous souhaitez afficher graphiquement des informations sur vos tâches, vous pouvez le faire à l&#39;aide de la fonction de graphique Gantt. Activez Gantt dans une liste de tâches (à l&#39;aide de l&#39;icône Gantt en haut à droite à côté d&#39;Enregistrement automatique), puis accédez à l&#39;icône Paramètres juste en dessous et à droite et cliquez dessus. Cochez la case Ligne de base pour afficher toutes les lignes de base. Vous pouvez les sélectionner un par un et afficher les modifications dans vos tâches dans la vue Gantt.

**Question**

Comment créer un rapport pour trouver les modifications de son statut pour une période définie, par exemple le mois dernier.

**Réponse**

La fonctionnalité Analytics de Workfront vous permet d’afficher facilement les données historiques, y compris les changements de statut.

Mais vous pouvez également obtenir des informations sur le changement de statut à l’aide d’un rapport Note. Vous pouvez filtrer pour afficher les modifications de statut des projets si vous effectuez le suivi du champ Statut du projet .

Accédez donc d’abord à Configuration > Interface > Mettre à jour les flux et assurez-vous que le statut du projet fait partie des champs intégrés qui font l’objet d’un suivi. Si ce n&#39;est pas le cas, vous devez l&#39;ajouter.

Créez maintenant un rapport de notes et procédez comme suit :

Dans l’onglet Colonnes (Vue) :

* Remplacez la colonne « Texte de la note » par « Texte de l’audit ». Cette action affiche des informations sur le changement de statut de et vers
* Laissez les colonnes « Projet : Nom » et « Date de saisie »
* Cliquez sur la colonne « Date d’entrée », puis cochez la case « Trier en fonction de cette colonne » dans le panneau Paramètres des colonnes. Si vous souhaitez afficher les modifications de statut les plus récentes dans la partie supérieure, triez-les par ordre décroissant.

Dans l&#39;onglet Regroupements :

* Regrouper par projet : Nom

Dans l’onglet Filtres , créez les règles de filtrage suivantes :

* Remarque >> Type d’audit >> Égal >> Changement de statut
* ajoutez des règles supplémentaires pour filtrer par date d&#39;entrée de note. Vous pouvez préférer exclure cette option des filtres et utiliser à la place une invite de rapport
* Filtrez les données de projet, de portfolio ou autres selon vos besoins.

**Question**

En tant que planificateur, pouvez-vous extraire des rapports pour d’autres utilisateurs ?

**Réponse**

Un planificateur peut créer des rapports et les partager avec n&#39;importe quel utilisateur, même avec des personnes qui ne sont pas des utilisateurs. Lors de l’affichage du rapport, accédez à Actions du rapport > Partage, puis cliquez sur l’icône en forme d’engrenage en haut à droite de la zone Accès au rapport . Sélectionnez l’option « Rendre ceci public pour les utilisateurs et utilisatrices externes ». option. Vous pouvez copier le lien fourni et l’envoyer à n’importe qui. Ils verront le rapport en temps réel dans leur navigateur.
