---
id: fragestellungengenerieren
description: "KI kann bei der Erstellung von Fragestellungen helfen, indem sie Vorschläge für Fragestellungen generiert."
image: "anwendungsfälle/images/fragestellung.svg" 
tags:
- fragestellungen
- studierende
title: Fragestellungen generieren
type: usecase
---



# Fragestellungen generieren

KI kann dir bei der Formulierung von Forschungfragen helfen, indem sie Vorschläge für Fragestellungen generiert.

## Beschreibung

Die Formulierung einer Fragestellung ist einer der ersten grundlegenden Schritte bei der wissenschaftlichen Arbeitsweise. Sie konkretisiert ein Forschungsinteresse in eine Aufgabe, die es mit deiner Untersuchung zu beantworten gilt.

In der ersten Phase deiner wissenschaftlichen Arbeit kannst du KI-Werkzeuge nutzen, um Vorschläge für mögliche Fragestellungen einzuholen. Nutze die KI, um Ideen oder einen ersten Entwurf zu generieren oder zum Brainstorming. Die Ergebnisse können als Inspiration bei der Formulierung der eigentlichen Forschungsfrage dienen. Wichtig: Prüfe, dass es eine Forschungsfrage ist, die noch nicht beantwortet wurde.

---


## Tools für diesen Anwendungsfall

```yaml
condition: or
entityType: usecase
rules:
- condition: contains
  property: id
  value: fragestellungengenerieren-chatgpt
- condition: contains
  property: id
  value: fragestellungengenerieren-elicit
```

---

## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: equals
  property: id
  value: bias-diskriminierung
- condition: equals
  property: id
  value: halluzinationen
- condition: equals
  property: id
  value: nachvollziehbarkeit
```

---

## Chancen

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: kompetenzerwerb-durch-ki
- condition: contains
  property: id
  value: zweitmeinung
```

