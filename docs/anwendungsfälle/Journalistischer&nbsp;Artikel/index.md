---
description: "Generiere Feedback zu deinem (wissenschafts-) journalistischen Artikel."
id:  journalistischerartikelfeedback
image: "anwendungsfälle/images/onlinearticles.svg" 
tags:
- journalistischerartikel
- studierende
title: Feedback zum journalistischen Artikel
type: usecase
---



# Feedback zum journalistischen Artikel
Um deinen wissenschaftsjournalistischen Artikel zu optimieren, kannst du KI-basierte Werkzeuge wie Chatbots nutzen, um Feedback und Verbesserungsvorschläge einzuholen.


## Beschreibung

Das Verfassen von wissenschaftsjournalistischen Beiträgen kann eine Aufgabe sein, die du im Rahmen deines Studiums als Leistungsnachweis erbringen musst. Beispielsweise kann von dir verlangt werden, dass du deine Seminararbeit im wissenschaftsjournalistischen Stil zusammenfasst. Im Gegensatz zu einem wissenschaftlichen Bericht richtet sich ein wissenschaftsjournalistischer Artikel an ein breiteres Publikum. Das hat Auswirkungen auf Stil und Form deines Textes.


---


## Tools für diesen Anwendungsfall

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: journalistischerartikelfeedback-chatgpt
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


