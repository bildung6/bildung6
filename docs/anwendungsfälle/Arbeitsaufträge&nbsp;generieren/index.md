---
id: arbeitsauftraege
description: "Lehrende können KI für eine effiziente Erstellung von studentischen Arbeitsaufträgen einsetzen, um umgehend Vorschläge zu generieren."
image: "anwendungsfälle/images/focus.svg" 
tags:
- arbeitsaufträge
- lehrende
title: Arbeitsaufträge generieren
type: usecase
---


# Arbeitsaufträge generieren

Lehrende können künstliche Intelligenz (KI) für eine effiziente Erstellung von studentischen Arbeitsaufträgen einsetzen, um umgehend Vorschläge zu generieren.


## Beschreibung

Die Anwendung von KI im Bildungsbereich, etwa zur automatisierten Erstellung studentischer Arbeitsaufträge, könnte Lehrenden eine effiziente und individualisierte Aufgabenkonzeption ermöglichen. Mithilfe von KI-Systemen, wie beispielsweise OpenAI's ChatGPT, können Dozierende nicht nur Vorschläge für massgeschneiderte und herausfordernde Arbeitsaufträge erstellen, sondern auch innovative Ansätze zur Unterrichtsgestaltung erkunden. 


---


## Tools für diesen Anwendungsfall


```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: arbeitsauftraege-chatgpt
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




