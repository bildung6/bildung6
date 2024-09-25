---
title: Wissenschaftliches Arbeiten
type: "quest"
image: quests/images/wissenschaftlich.svg
description: Welche KI-Tools unterstützen mich beim wissenschaftlichen Arbeiten? 
---


In dieser Quest geht es darum, wie KI zur Unterstützung beim wissenschaftlichen Arbeiten eingesetzt werden kann. 

###	Fragestellung generieren

Das Formulieren einer Fragestellung ist einer der ersten grundlegenden Schritte beim wissenschaftlichen Arbeiten. Nutze KI, um dich dabei zu unterstützen.

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: fragestellungengenerieren
```


###	Journalistischer Artikel
Das Schreiben von wissenschaftsjournalistischen Artikeln kann eine Aufgabe sein, die du im Rahmen deines Studiums erledigen musst. Nutze KI, um Feedback zu deinem Text zu erhalten.


```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: journalistischerartikelfeedback
```


### Literaturrecherche
Die KI kann die Literaturrecherche durch Unterstützung bei der Suche und Auswahl geeigneter Quellen erleichtern.

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: literaturrecherche
```


### Summary erstellen
Künstliche Intelligenz (KI) kann nicht nur eingesetzt werden, um lange Texte automatisch zusammenzufassen, sie kann auch bei der Erstellung von Abstracts wertvolle Hilfe leisten, indem sie die zentralen Punkte eines Textes hervorhebt.

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: summariesgenerieren
```


### Sprachliche Korrektur
Benutze KI, um schriftliche Arbeiten sprachlich zu korrigieren.

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: sprachlichekorrektur
```


### Ideen generieren
Nutze die generative KI bei der Ideenfindung.

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: ideengenerieren
```


### Präsentationen üben
Nutze die generative KI bei Präsentationen.

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: praesentationenueben
```


### Transkription (Verschriftlichung)
Nutze die KI als Assistent bei der Verschriftlichung von Gesprächen.

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: transkription
```


