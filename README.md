# Game of Live


Le jeu de la vie a été inventé par le mathématicien John H. Conway en 1970. C’est un « jeu à zéro joueur », puisqu'il ne nécessite pas l'intervention du joueur lors de son déroulement. Il est un bon exemple d’un système où une règle locale simple donne lieu à un comportement global complexe. 
 
Le jeu se déroule sur une grille à deux dimensions, théoriquement infinie (mais de longueur et de largeur finies et plus ou moins grandes dans la pratique), dont les cases — qu’on appelle des « cellules », par analogie avec les cellules vivantes — peuvent prendre deux états distincts : « vivante » ou « morte ». 
 
Une cellule possède huit voisins, qui sont les cellules adjacentes horizontalement, verticalement et diagonalement. 
 
À chaque étape, l’évolution d’une cellule est entièrement déterminée par l’état de ses huit voisines de la façon suivante : 

    une cellule morte possédant exactement trois voisines vivantes devient vivante (elle naît) ; 
    une cellule vivante possédant deux ou trois voisines vivantes le reste, sinon elle meurt. 

 
On peut également formuler cette évolution ainsi : 

    si une cellule a exactement trois voisines vivantes, elle est vivante à l’étape suivante. 
    si une cellule a exactement deux voisines vivantes, elle reste dans son état actuel à l’étape suivante.
    si une cellule a strictement moins de deux ou strictement plus de trois voisines vivantes, elle est morte à l’étape suivante. 


## API: Flask API 

### Route init
 
*Route* : `/init_game`  
*Paramettres :*  
- format : `JSON`
```json
    {
        "start_points": {
            "type": "array",
            "description": "coordoné des cellule vivante",
            "required": false
          },
        "length": {
            "type":  "int",
            "description": "hauteur du tableau",
          "required": false
          }, 
          "width": {
            "type":  "int",
            "description": "Largeur du tableau",
            "required": false
          }
    }
```

- start_points: coordoné des cellule vivante
- lenght: hauteur du tableau
- width: largeur


*reponse* :
- format : `JSON`

````json
{
  "alive_cell_points": {
    "type": "array",
    "description": "coordoné des cellule vivante"
  },
  "length": {
    "type":  "int",
    "description": "hauteur du tableau"
  }, 
  "width": {
    "type":  "int",
    "description": "Largeur du tableau"
  },
  "nb_alive_cell": {
    "type":  "int",
    "description": " nombre de cellule vivante"
  }, 
}
````
- start_points: coordoné des cellule vivante
- lenght: hauteur du tableau
- width: largeur
- nb_alive_cell: nombre de cellule vivante



### Route next tour
 
*Route* : `/next_tour`  
*Paramettres :*  
- format : `JSON`
```json
    {
        "start_points": {
            "type": "array",
            "description": "coordoné des cellule vivante",
            "required": false
          },
        "length": {
            "type":  "int",
            "description": "hauteur du tableau",
          "required": false
          }, 
          "width": {
            "type":  "int",
            "description": "Largeur du tableau",
            "required": false
          }, 
        "nb_tour": {
          "type":  "int",
            "description": "nombre de tour a effectuer",
            "required": false
        }
    }
```

- start_points: coordoné des cellule vivante
- lenght: hauteur du tableau
- width: largeur
- nb_tour: nombre de tour a effectuer


*reponse* :
- format : `JSON`

````json
{
  "alive_cell_points": {
    "type": "array",
    "description": "coordoné des cellule vivante"
  },
  "length": {
    "type":  "int",
    "description": "hauteur du tableau"
  }, 
  "width": {
    "type":  "int",
    "description": "Largeur du tableau"
  },
  "nb_alive_cell": {
    "type":  "int",
    "description": " nombre de cellule vivante"
  }, 
}
````
- start_points: coordoné des cellule vivante
- lenght: hauteur du tableau
- width: largeur
- nb_alive_cell: nombre de cellule vivante


