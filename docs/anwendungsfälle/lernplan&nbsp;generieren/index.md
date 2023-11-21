---
id: lernplangenerieren
description: "Nutze KI, um einen Vorschlag für einen individuellen Lernplan zu erstellen."
image: "anwendungsfälle/images/events.svg" 
tags:
- studierende
title: Lernplan generieren
type: usecase
---


# Fragen generieren

Durch den Einsatz von künstlicher Intelligenz (KI) lässt sich ein massgeschneiderter Lernplan erstellen, der gezielt auf die persönlichen Bedürfnisse der Nutzer:in eingeht.


## Beschreibung

KI ermöglicht die schnelle Erstellung von personalisierten Lernplänen, die auf die individuellen Anforderungen und Lernziele der Nutzer:in abgestimmt sind. Durch ihre Fähigkeit, gezielt auf Bedürfnisse einzugehen und wichtige Schwerpunkte hervorzuheben, kann die KI effektive Vorschläge generieren. Das generierte Ergebnis dient als Grundlage, die individuell angepasst und mit eigenen Zielen oder thematischen Schwerpunkten vervollständigt werden kann.


---


## Tools für diesen Anwendungsfall

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: lernplangenerieren-chatgpt
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
  value: entlastung-durch-automatisierung
```

