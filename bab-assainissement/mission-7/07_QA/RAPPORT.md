# 07 · Contrôle qualité

Chromium sans écran (Playwright 1.63), page servie en local, dans un conteneur en ligne. Aucun téléphone réel, aucun lecteur d'écran, aucun utilisateur.

## Ce qui a été fait

- **46 captures** dans `captures/` : six formats (1440 × 900, 1280 × 800, 1024 × 768, 768 × 1024, 390 × 844, 360 × 800), sept vues chacun (premier écran, rapport, prestations, chantiers, schémas, formulaire, bas de page), plus la navigation ouverte sur les quatre formats qui ont un menu.
- **27 vérifications automatiques sur 27**, détail dans `tests-automatiques.txt`. Elles cliquent et saisissent réellement : bande au clic et au clavier, menu, formulaire avec erreurs puis message de démonstration, barre fixe, zoom.
- **Accessibilité automatique** (axe-core, règles WCAG 2.1 A et AA) : 0 violation sur ordinateur et sur téléphone. Les critères propres à WCAG 2.2 n'ont pas été contrôlés un par un.
- **Zoom à 200 %** et largeur de 320 px : aucun défilement horizontal, aucun titre coupé.
- **Sans JavaScript et en mouvement réduit** : page complète, les quatre photos de la bande visibles.

## Mesures

| Contexte | Texte affiché | Photo principale | Décalage cumulé | Poids initial |
|---|---|---|---|---|
| Ordinateur 1440 × 900, sans bridage | 0,11 s | 0,11 s | 0 | 2,0 Mo |
| Téléphone simulé 390 × 844, 1,6 Mbit/s, processeur ralenti 4 fois | 0,5 s | 2,0 s | 0,002 | 545 ko |

L'interactivité (INP) n'a pas été mesurée. Lighthouse n'a pas été lancé.

## Défauts corrigés

Passe 1
1. Le titre se coupait mal (« Nous / réalisons ») et le paragraphe tombait hors de l'écran sur ordinateur.
2. Sur téléphone, la légende de la bande collait au titre.
3. Dans la direction B, deux étiquettes se chevauchaient sur la photo.

Passe 2
1. Les photos de la fosse et du puisard apparaissaient dans deux sections voisines. Les trois lignes du rapport sont passées en texte seul.
2. Le bouton « Prendre le rapport en photo » tenait sur deux lignes sur ordinateur.

## Non résolu ou non testé

- Sur ordinateur, les quatre photos de la bande se chargent d'emblée : 2,0 Mo au départ. À alléger avec des formats AVIF et des tailles adaptées.
- Photos en 720 à 800 px de large : la photo agrandie manque de piqué sur un grand écran.
- Envoi réel du formulaire, prise de photo sur un vrai téléphone, vrai clavier tactile, Safari : non testés.
- Contraste du texte posé sur les photos (étiquettes des moments) : à vérifier à l'œil, l'outil ne le mesure pas.
