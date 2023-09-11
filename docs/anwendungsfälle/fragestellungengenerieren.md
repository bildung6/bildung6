---
description: "KI kann bei der Erstellung von Fragestellungen helfen, indem sie Vorschl\xE4\
  ge f\xFCr Fragestellungen generiert."
id: fragestellungengenerieren
image: "anwendungsf\xE4lle/images/fragestellung.svg" 
tags:
- fragestellungen
- studierende
title: Fragestellungen generieren
type: usecase
---



# Fragestellungen generieren

## Beschreibung

KI kann dir bei der Formulierung von Forschungfragen helfen, indem sie Vorschläge für Fragestellungen generiert.

Die Formulierung einer Fragestellung ist einer der ersten grundlegenden Schritte bei der wissenschaftlichen Arbeitsweise. Sie konkretisiert ein Forschungsinteresse in eine Aufgabe, die es mit deiner Untersuchung zu beantworten gilt.

In der ersten Phase deiner wissenschaftlichen Arbeit kannst du KI-Werkzeuge nutzen, um Vorschläge für mögliche Fragestellungen einzuholen. Nutze die KI, um Ideen oder einen ersten Entwurf zu generieren oder zum Brainstorming. Die Ergebnisse können als Inspiration bei der Formulierung der eigentlichen Forschungsfrage dienen. Wichtig: Prüfe, dass es eine Forschungsfrage ist, die noch nicht beantwortet wurde.

---
<!--

## Anwender:innen

```yaml
condition: or
entityType: user
rules:
- condition: contains
  property: id
  value: studierende
```
-->
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
  value: abhaengigkeit
- condition: equals
  property: id
  value: abnahme-reflexionsfaehigkeit
- condition: equals
  property: id
  value: blindes-folgen
- condition: equals
  property: id
  value: faehigkeit-komplexe-aufgaben-loesen-nimmt-ab
- condition: equals
  property: id
  value: fehlende-transparenz
- condition: equals
  property: id
  value: gesellschaftlicher-bias
- condition: equals
  property: id
  value: kompetenzverlust
- condition: equals
  property: id
  value: meinungsverlust
- condition: equals
  property: id
  value: monopolbildung
- condition: equals
  property: id
  value: nachvollziehbarkeit
- condition: equals
  property: id
  value: plagiate
- condition: equals
  property: id
  value: verlust-kreativitaet
- condition: equals
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
  value: kompetenzerwerb-durch-ki
- condition: contains
  property: id
  value: zweitmeinung
```

