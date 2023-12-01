---
description: "KI kann bei der Erstellung von Summaries helfen, indem sie Texte zusammenfasst."
id: summariesgenerieren
image: "anwendungsfälle/images/ideas_bearbeitet.svg" 
tags:
- studierende
title: Summaries generieren
type: usecase
---


# Summaries generieren
KI kann bei der Erstellung von Summaries helfen, indem sie Texte zusammenfasst.

## Beschreibung

Das Generieren von Summaries oder Zusammenfassungen kann in verschiedenen Phasen der wissenschaftlichen Arbeit eingesetzt werden. 

So können beispielsweise wissenschaftliche Quellen schnell zusammengefasst werden. Diese Zusammenfassungen können einen Überblick über die Forschungsergebnisse geben, der für die Gliederung eines Berichts verwendet werden kann. Eine weitere Anwendungsmöglichkeit ist das Zusammenfassen eigener Texte für die Erstellung eines Abstracts.


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


---


## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: equals
  property: id
  value: halluzinationen
- condition: equals
  property: id
  value: nachvollziehbarkeit
- condition: equals
  property: id
  value: geschuetzte-daten
- condition: equals
  property: id
  value: plagiate
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


