---
description: "Ein Chatbot f\xFCr Moodle Kurse kann verwendet werden, um automatisch\
  \ Fragen von Studierenden zu beantworten, Ressourcen bereitzustellen und den Lernenden\
  \ bei der Navigation durch den Kurs zu helfen."
id: chatbotfuermoodle
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- chatbot
- moodle
- studierende
- lehrende
title: "Chatbot f\xFCr Moodle Kurse"
type: usecase
---


# Chatbot für Moodle Kurse

## Beschreibung

Ein Chatbot für Moodle Kurse kann verwendet werden, um automatisch Fragen von Studierenden zu beantworten, Ressourcen bereitzustellen und den Lernenden bei der Navigation durch den Kurs zu helfen.

## AnwenderInnen

```yaml
condition: or
entityType: user
rules:
- condition: contains
  property: id
  value: studierende
- condition: contains
  property: id
  value: lehrende
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
  value: effizienzsteigerung
```

