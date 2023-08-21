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
- condition: equals
  property: id
  value: elicit
```

## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: contains
  property: id
  value: abhängikeit
- condition: contains
  property: id
  value: bias-diskriminierung
- condition: contains
  property: id
  value: faehigkeit-komplexe-aufgaben-loesen-nimmt-ab
- condition: contains
  property: id
  value: gesellschaftlicher-bias
- condition: contains
  property: id
  value: kompetenzverlust
- condition: contains
  property: id
  value: nachvollziebarkeit
- condition: contains
  property: id
  value: verlust-kreativität
```

---

## Chancen

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: effizienzsteigerung
```

---

## Links

---

## Quellen