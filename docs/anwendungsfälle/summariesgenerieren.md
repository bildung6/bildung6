---
description: "KI kann bei der Erstellung von Summaries helfen, indem sie Texte zusammenfasst."
id: summariesgenerieren
image: "anwendungsf\xE4lle/images/ideas_bearbeitet.svg" 
tags:
- studierende
title: Summaries generieren
type: usecase
---


# Summaries generieren

## Beschreibung

Das Generieren von Summaries oder Zusammenfassungen kann in verschiedenen Phasen der wissenschaftlichen Arbeit eingesetzt werden. 

So können beispielsweise wissenschaftliche Quellen schnell zusammengefasst werden. Diese Zusammenfassungen können einen Überblick über die Forschungsergebnisse geben, der für die Gliederung eines Berichts verwendet werden kann.

Eine weitere Anwendungsmöglichkeit ist das Zusammenfassen eigener Texte für die Erstellung eines Abstracts.


---


## Tools für diesen Anwendungsfall

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: summariesgenerieren-chatgpt
```


## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: contains
  property: id
  value: abhaengigkeit
- condition: contains
  property: id
  value: abnahme-reflexionsfaehigkeit
- condition: contains
  property: id
  value: fehlende-transparenz
- condition: contains
  property: id
  value: geschuetzte-daten
- condition: contains
  property: id
  value: kompetenzverlust
- condition: contains
  property: id
  value: monopolbildung
- condition: contains
  property: id
  value: nachvollziehbarkeit
- condition: contains
  property: id
  value: plagiate
- condition: contains
  property: id
  value: wem-gehoert-die-ki
```

---

## Chancen

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: sprachliche-barrieren-aufloesen
- condition: contains
  property: id
  value: zweitmeinung
```


---


## Links


---


## Quellen


