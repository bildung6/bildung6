---
description: KI kann administrative Fragen von Studierenden und Lehrenden beantworten.
id: administrativefragenbeantworten
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- administrativefragen
- studierende
- lehrende
title: Administrative Fragen beantworten
type: usecase
---


# Administrative Fragen beantworten

## Beschreibung

KI kann administrative Fragen von Studierenden und Lehrenden beantworten.

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
  value: papago
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
  value: zeitersparnis
```

