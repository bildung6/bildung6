---
description: "KI Tutoring kann Studierenden bei der Bew\xE4ltigung von Lerninhalten\
  \ und dem Erreichen ihrer Lernziele helfen, indem es personalisierte Unterst\xFC\
  tzung, Feedback und Ressourcen anbietet."
id: kitutoring
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- kitutoring
- studierende
title: KI Tutoring
type: usecase
---


# KI Tutoring

## Beschreibung

KI Tutoring kann Studierenden bei der Bewältigung von Lerninhalten und dem Erreichen ihrer Lernziele helfen, indem es personalisierte Unterstützung, Feedback und Ressourcen anbietet.

## AnwenderInnen

```yaml
condition: or
entityType: user
rules:
- condition: contains
  property: id
  value: studierende
```



## Tools

```yaml
condition: or
entityType: tool
rules:
- condition: contains
  property: id
  value: chatgpt
- condition: contains
  property: id
  value: bard
```



## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: contains
  property: id
  value: kompetenzverlust
- condition: contains
  property: id
  value: datenschutz
```



## Chance

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: kreative-anstoesse
```

