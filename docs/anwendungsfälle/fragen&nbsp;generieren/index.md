---
id: fragengenerieren
description: "KI kann bei der Erstellung von Fragen helfen, indem sie Vorschläge generiert."
image: "anwendungsfälle/images/selection.svg" 
tags:
- fragen
- studierende
- lehrende
title: Fragen generieren
type: usecase
---


# Fragen generieren

Künstliche Intelligenz (KI) kann genutzt werden, um Prüfungs- und Quizfragen zu generieren. 


## Beschreibung

Lehrende können KI, einschliesslich spezialisierter Quiz-Generatoren und Chatbots wie ChatGPT, effizient zur Optimierung der Erstellung von Prüfungs- und Quizfragen nutzen, wobei die erzielten Ergebnisse als solide Grundlage für die Ausarbeitung von Prüfungen und Quizzen dienen können.


---


## Tools für diesen Anwendungsfall

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: fragengenerieren-chatgpt
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
- condition: contains
  property: id
  value: zweitmeinung
```

