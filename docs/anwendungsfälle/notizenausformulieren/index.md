---
description: "Generiere aus Notzien einen Text."
id:  notizenausformulieren
image: "anwendungsfälle/images/writer.svg" 
tags:
- notizenausformulieren
- lehrende
title: Notizen ausformulieren
type: usecase
---



# Notizen ausformulieren 
Künstliche Intelligenz (KI) ermöglicht die effiziente Umwandlung knapper Notizen in strukturierte Texte in verschiedenen Kontexten.

## Beschreibung

KI und speziell Language Models (LLMs) sind effektive Werkzeuge zur Generierung strukturierter Texte aus knappen Notizen oder Stichwörtern. So kann eine Lehrkraft mithilfe von KI detailliertes und konstruktives Feedback für studentische Präsentationen aus einfachen Notizen erstellen. Ähnlich kann in einem geschäftlichen Umfeld KI dazu verwendet werden, um aus stichpunktartigen Notizen, die während eines Meetings angefertigt wurden, einen klaren und verständlichen Bericht zu erstellen. In beiden Kontexten fördert die Verwendung von KI eine effiziente und qualitative Informationsaufbereitung, die zur Verbesserung von Kommunikation und Verständnis beiträgt.



---


## Tools für diesen Anwendungsfall

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: notizenausformulieren-chatgpt
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
- condition: equals
  property: id
  value: kompetenzerwerb-durch-ki
- condition: equals
  property: id
  value: sprachliche-barrieren-aufloesen
- condition: equals
  property: id
  value: zweitmeinung
```


