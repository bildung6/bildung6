---
description: "KI kann Feedback-Bausteine erstellen, die Lehrkr\xE4fte bei der Bewertung\
  \ von Arbeiten oder der Erstellung von R\xFCckmeldungen verwenden k\xF6nnen."
id: feedbackbausteine
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- feedback
- lehrende
title: Feedback-Bausteine
type: usecase
---


# Feedback-Bausteine

## Beschreibung

KI kann Feedback-Bausteine erstellen, die Lehrkräfte bei der Bewertung von Arbeiten oder der Erstellung von Rückmeldungen verwenden können.

## AnwenderInnen

```yaml
condition: or
entityType: user
rules:
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
  value: ai-text-classifier
- condition: contains
  property: id
  value: composeai
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

