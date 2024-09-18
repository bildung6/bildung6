---
id: praesentationenueben
description: "KI kann dich bei Präsentationen unterstützen."
image: "anwendungsfälle/images/candidate_praesentation.svg" 
tags:
- studierende
title: Präsentationen üben
type: usecase
---



# Präsentationen üben

Künstliche Intelligenz (KI) ist längst nicht mehr auf die Verarbeitung von Text beschränkt. Moderne KI-Systeme sind multimodal und können verschiedene Arten von Daten wie Text, Ton und sogar Bilder analysieren und verstehen. Durch die Erkennung von Mustern in Sprache und Ton können diese Systeme Aufgaben wie die automatische Spracherkennung, Transkription und das Generieren von Untertiteln übernehmen.

## Beschreibung

Für Präsentationen bietet KI einen Mehrwert, indem sie als „Zweitmeinung“ agiert. Tools wie der PowerPoint Speaker Coach nutzen KI, um Feedback zu deinem Präsentationsstil zu geben, etwa zu Sprechtempo, Füllwörtern und Ausdrucksweise. 

---



## Tools für diesen Anwendungsfall


```yaml
condition: or
entityType: usecase
rules:
- condition: contains
  property: id
  value: Speaker-Coach
```


---

## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: equals
  property: id
  value: nachvollziehbarkeit
- condition: equals
  property: id
  value: geschuetzte-daten
```

---

## Chancen

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: zweitmeinung
```

---
