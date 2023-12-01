---
description: "KI kann zur Übersetzung von Texten oder Textdokumenten eingesetzt werden."
id: unterlagenuebersetzen
image: "anwendungsfälle/images/sharingknowledge.svg"
tags:
- unterlagenuebersetzen
- studierende
- lehrende
title: Unterlagen übersetzen
type: usecase
---


# Unterlagen übersetzen

KI kann zur Übersetzung von Texten oder Textdokumenten eingesetzt werden.


## Beschreibung

Nutzer:innen können Künstliche Intelligenz (KI) als Werkzeug nutzen, um Texte und Dokumente schnell und präzise zu übersetzen, wodurch sie in der Lage sind, Sprachbarrieren zu überwinden und einen international ausgerichteten Unterricht zu gewährleisten. 


---


## Tools für diesen Anwendungsfall


```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: unterlagenuebersetzen-deepltranslator
```


---



## Risiken

```yaml
condition: or
entityType: risk
rules:
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
- condition: equals
  property: id
  value: kompetenzerwerb-durch-ki
- condition: equals
  property: id
  value: sprachliche-barrieren-aufloesen
```

