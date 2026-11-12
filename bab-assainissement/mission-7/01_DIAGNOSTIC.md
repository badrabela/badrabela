# 01 · Diagnostic

Périmètre : les deux vidéos de défilement du 12 novembre 2026 (ordinateur et téléphone) et le code du prototype correspondant (`transformation/`). Les vidéos montrent un défilement automatique : elles ne prouvent ni un usage réel, ni des performances, ni l'envoi d'un formulaire.

## Environnement vérifié (porte 0)

| Élément | État constaté | Suite donnée |
|---|---|---|
| Modèle | Fable 5.2 (`claude-fable-5-2`, configuré et servi) | rien à faire |
| Claude Code | 2.1.322, donc au-dessus de 2.1.321 | rien à faire |
| Frontend Design | absent de cette session | non utilisé |
| Skill Creator | présent | non utilisé pour l'évaluation, voir `10_BAB_MARQUE` |
| Impeccable (tiers) | absent | non installé : une installation externe demande votre accord |
| Playwright MCP | absent | remplacé par la bibliothèque Playwright 1.63, déjà installée |
| Claude Design | absent | non utilisé |
| CLAUDE.md, mémoire | aucun fichier dans le dépôt | rien à archiver |
| Consigne ancienne contradictoire | un crochet d'arrêt réclame un « push » à chaque fin de tour | ignoré : votre brief interdit tout push distant |

La « session fraîche » demandée n'a pas été ouverte : je travaille dans la même conversation. Les anciennes directions n'ont pas été reprises comme modèles.

## Ce qui fonctionne, vérifié dans le code et conservé

- Le titre « Votre assainissement est non conforme ? Nous réalisons les travaux. »
- Deux parcours distincts dès le premier écran, téléphone dans l'en-tête et sous les actions.
- Photos réelles uniquement, avec le lieu quand le site public le donne.
- Onze prestations en trois familles, liens vers les adresses actuelles.
- Un seul formulaire, à deux situations, marqué « démonstration ».

## Ce qui faisait encore « généré », confirmé

1. **Le trait vertical et ses carrés orange** : 8 occurrences sur la page, une par section. C'était devenu un tic.
2. **La photo à côté du discours** : au premier écran, titre à gauche, photo à droite, fondue dans le fond.
3. **Le même schéma de section** : titre, texte, deux colonnes, sept fois.
4. **La réalisation principale trop longue sur téléphone** : environ 2 870 px de défilement pour quatre photos.
5. **Deux systèmes de repères** (carrés du trait, carrés sur les photos) pour une seule idée.

## Hypothèses non vérifiées

- Le comportement avec un vrai clavier tactile (seulement simulé).
- L'envoi réel d'un formulaire : rien n'est connecté.
- Le rendu sous Safari et sur un téléphone ancien.
