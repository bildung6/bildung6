---
description: KI kann bei der Beantwortung von Fragen zum Modul helfen.
id: fragenbeantwortungzummodul
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- fragenbeantwortung
- lehrende
- studierende
title: Fragenbeantwortung zum Modul
type: usecase
---


# Fragenbeantwortung zum Modul

## Beschreibung

KI kann bei der Beantwortung von Fragen zum Modul helfen.

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
  value: papago
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
  value: zeitersparnis
```

