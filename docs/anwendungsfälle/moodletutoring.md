---
description: "KI kann in Tools wie Moodle integriert werden, um den Lernprozess zu\
  \ unterst\xFCtzen und zu optimieren, indem sie zum Beispiel automatisierte Bewertungen,\
  \ personalisierte Empfehlungen oder Chatbot-Funktionen anbietet."
id: moodletutoring
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- moodle
- tutoring
- lehrende
- studierende
title: Einbindung in Tools wie Moodle
type: usecase
---


# Einbindung in Tools wie Moodle

## Beschreibung

KI kann in Tools wie Moodle integriert werden, um den Lernprozess zu unterstützen und zu optimieren, indem sie zum Beispiel automatisierte Bewertungen, personalisierte Empfehlungen oder Chatbot-Funktionen anbietet.

## AnwenderInnen

```yaml
condition: or
entityType: user
rules:
- condition: contains
  property: id
  value: lehrende
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
  value: datenschutz
- condition: contains
  property: id
  value: monopolbildung
```



## Chance

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: personalisiertes-lernen
```

