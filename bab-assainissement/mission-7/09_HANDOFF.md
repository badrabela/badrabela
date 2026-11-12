# 09 · Passation

## Fichiers

- `06_SITE_LOCAL/index.html` : la page, CSS et JavaScript inclus (environ 50 ko). Aucune bibliothèque.
- `06_SITE_LOCAL/BAB-accueil-autonome.html` : la même, images et police incluses, à ouvrir d'un double-clic.
- `06_SITE_LOCAL/img/` : 15 images WebP. `06_SITE_LOCAL/fonts/sofia-sans.woff2` : la police (licence libre OFL).

## Composants

| Composant | Classe | Remarque |
|---|---|---|
| Bande de moments | `.bande`, `.moment`, `.b-leg` | boutons avec `aria-pressed` ; sans JavaScript, quatre tranches égales |
| Action principale et secondaire | `.btn.plein`, `.btn` | rectangle, libellé sur deux lignes |
| Téléphone | `.tel`, `.monument` | lien `tel:` |
| Liste de prestations | `.liste` | un lien par ligne, vers l'adresse actuelle |
| Paires du rapport | `.paires` | texte seul |
| Schémas | `.schema` | SVG, mention « schémas de principe » |
| Formulaire | `#formulaire` | démonstration, aucun envoi |
| Barre fixe mobile | `.barre` | masquée quand une action est visible ou qu'on écrit |

## Variables

`--sol #E7E6DF`, `--papier #F5F4EF`, `--nuit #10202E`, `--terre #B84A0C`, `--gris #45515A`.

## Images

Toutes viennent du site public, recadrées et réglées de la même façon (niveaux, saturation 94 %). **À confirmer par BAB : l'attribution de chaque chantier et les droits.** La photo de fosse a été recadrée pour retirer une maison et un véhicule identifiables.

## Limites

- Seule la page d'accueil existe. Rien n'est décliné sur les pages prestations, communes, réalisations, envoi de rapport.
- Formulaire non connecté.
- Schémas dessinés par moi : à relire.

## Risques pour le référencement

Le prototype ne reprend pas le titre, la description, l'adresse canonique ni les données structurées de l'accueil actuel, et il est marqué `noindex`. Les 39 adresses de services et de zones, les 368 pages communes et les 20 guides ne sont pas touchés ; les liens de la page pointent vers eux. Toute mise en ligne demande un audit de migration préalable et le maintien du suivi des appels et des formulaires.
