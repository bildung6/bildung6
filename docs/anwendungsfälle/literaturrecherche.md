---
description: "KI kann bei der Literaturrecherche unterst\xFCtzend wirken, indem sie\
  \ relevante Artikel und Studien identifiziert und vorschl\xE4gt."
id: literaturrecherche
image: "anwendungsf\xE4lle/images/filesearching.svg"
tags:
- literaturrecherche
- studierende
title: Literaturrecherche
type: usecase
---


# Literaturrecherche

## Beschreibung

Eine Literaturrecherche ist der systematische Prozess der Identifizierung wissenschaftlicher Quellen zu einem bestimmten Thema. Sie dient dazu, den aktuellen Stand der Forschung zu erkennen und die eigene Arbeit in einen Kontext zu stellen. Sie hilft, das vorhandene Wissen zu verstehen und die Relevanz der eigenen Fragestellung zu begründen.

KI-basierte Werkzeuge haben das Potenzial, dich bei der Suche und Auswahl geeigneter Literatur zu unterstützen.

---

## Tools für diesen Anwendungsfall

- Elitc: verwaltung, summarize, entdecken
- Research Rabbit: entdecken und relevanz erkennen
- consesus.app: argumente finden, ggf. fragestellung
- Scholarcy eher summarize: checken

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: literaturrecherche-elicit 
```

---

## Tools

```yaml
condition: or
entityType: tool
rules:
- condition: contains
  property: id
  value: composeai
- condition: contains
  property: id
  value: bingchatbot
```

---

## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: contains
  property: id
  value: datenschutz
- condition: contains
  property: id
  value: monopolbildung
```

---

## Chance

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: effizienz-steigerung
```

---

## Links

---

## Quellen