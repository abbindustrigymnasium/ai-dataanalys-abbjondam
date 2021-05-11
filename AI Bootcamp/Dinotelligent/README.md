# DINOTELLIGENT

## Innehåll:
  * [Projektbeskrivning](#projektbeskrivning)
  * [Länkar](#Länkar)
  * [Filer](#Filer)
  * [Filer](#Filer)
  * [Programmet](#Programmet)
    * [Installation](#Installation)
    * [Konfiguration av NEAT](#Konfiguration-av-NEAT)
    * [Körning](#Körning)
  * [Utvärdering](#Utvärdering)
    * [Problem](#Problem)
    * [Förbättringar](#Förbättringar)

## Projektbeskrivning
Ett projekt där en dator lär sig att spela google chrome spelet dino. Dator lära sig spela används NeuroEvolution of Augmenting Topologies (NEAT) som är en genetisk algoritm. Algoritmen fungerar genom att utveckla neurala nätverk (både med vikter men också genom att ändra det neurala nätverket).


## Länkar
* [NEAT-PYTHON](https://neat-python.readthedocs.io/en/latest/)
* [Python-Dino-Game](https://www.youtube.com/watch?v=lcC-jiCuDnQ)
* [NEAT-Flappy-Bird](https://www.youtube.com/watch?v=wQWWzBHUJWM)

## Filer
* [`main.py`](main.py) - programmet
* [`config.txt`](config.txt) - config för NEAT
* [`Assets`](Assets/) - Sprites och font

## Programmet

### Installation
Följande python moduler behöver vara nedladdade:
* Pygame
* NEAT
* Numpy

### Konfiguration av NEAT
Konfigurationen av NEAT sker i config.txt filen och antal generationer sätts i main.py när man kallar på funktionen run.

### Körning
Programet körs genom att köra python filen i cmd. 

`python main.py`

## Utvärdering

### Problem
Största problemet var att få NEAT att fungera. I början hoppade de mest random och verkade inte lära sig alls fråm tidigare generation (Jag tror det kan ha och göra med hur jag gav ut fitness). Konfigurationen av NEAT tog också lite tid innan jag fick något som gav bra resultat.


### Förbättringar
* En förbättring som skulle kunna göras är att spara bästa spelarens neurala nätverk och låta den spela individuelt.
* En annan förbättring är att kunna träna utan att visuellt kolla på när de kör (vilket skulle gå mycket fortare) och sedan köra vinnaren som i punkten tidigare.
* En annan förbättring skulle vara att förbättra rensningen av de svaga eftersom fortfarrande efter många generationer så dör de flesta av första hindret.
* Ändra hopp funktionen så att dinosaurierna inte kan hoppa över de högsta flygödlorna vilken tvingar dem att lära sig att ducka.
