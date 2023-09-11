---
description: "KI kann verwendet werden, um die sprachliche Korrektur von Studierenden\
  \ zu unterst\xFCtzen. Dies kann in Form von automatischen Korrekturen oder als Feedback\
  \ f\xFCr Studierende erfolgen."
id: sprachlichekorrektur
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- sprachlichekorrektur
- studierende
title: Sprachliche Korrektur
type: usecase
---


# Sprachliche Korrektur

## Beschreibung

KI-basierte Werkzeuge können verwendet werden, um Studierende in der sprachlichen Korrektur von ihnen verfasster Texte zu unterstützen. Dies kann in Form von automatischen Korrekturen oder als Feedback für Studierende erfolgen.


---

<!--
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


---
-->

## Tools für diesen Anwendungsfall


```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: sprachlichekorrektur-deeplwrite
```


---


## Quiz

<!--
!!! question "Aufgabe 1"
    Was könnten Risiken bei der Verwendung von KI zur sprachlichen Korrektur sein?

    ??? success "Lösung anzeigen"
    
        Bei der Verwendung von KI zur sprachlichen Korrektur können folgende Risiken auftreten:

        - Datenschutz und Datensicherheit
        - Fehlende Transparenz
        - Abhängigkeit



```yaml
question: "Wie kann KI bei der Bewertung von Schülerarbeiten helfen?"
type: "single-choice"
answers:
- [True, "KI kann automatisierte Bewertungssysteme für objektive Tests bereitstellen"]
- [False, "KI kann keine Schülerarbeiten bewerten", "KI kann automatisierte Bewertungssysteme für objektive Tests bereitstellen"]
- [False, "KI kann nur die Arbeiten von Hochschulstudenten bewerten",]
- [False, "KI kann nur Multiple-Choice-Fragen bewerten"]
```

```yaml
question: "Welche Rolle spielt KI bei der Personalisierung des Lernens?"
type: "single-choice"
answers:
- [True, "KI kann Lerninhalte an den individuellen Fortschritt und Stil eines Lernenden anpassen"]
- [False, "KI hat keinen Einfluss auf die Personalisierung des Lernens"]
- [False, "KI kann nur die Lerninhalte für eine ganze Klasse anpassen, nicht für einzelne Lernende"]
- [False, "KI ist nur für die Verwaltung von Bildungsdaten verantwortlich"]
```

```yaml
question: "Welche Anwendungen von KI können in der Bildung eingesetzt werden?"
type: "multiple-choice"
answers:
- [True, "Chatbots für den Kundendienst"]
- [True, "Automatisierte Bewertungssysteme", "Dies ist eine Anwendung von KI in der Bildung"]
- [True, "Personalisierte Lernpfade", "Dies ist eine Anwendung von KI in der Bildung"]
- [False, "Automatisierte Klassenzimmerreinigung", "Dies ist keine Anwendung von KI in der Bildung"]
```

```yaml
question: "Welche Vorteile bietet KI in der Bildung?"
type: "multiple-choice"
answers:
- [True, "Effizienzsteigerung durch Automatisierung von Routineaufgaben"]
- [True, "Personalisierung des Lernens durch Anpassung an den individuellen Lernstil"]
- [True, "Erkennung von Lernschwierigkeiten durch Analyse von Leistungsdaten"]
- [False, "Ersetzung aller Lehrer durch KI", "Dies ist kein Vorteil von KI in der Bildung"]
```


```yaml
question: "Welche Herausforderungen können bei der Implementierung von KI in der Bildung auftreten?"
type: "multiple-choice"
answers:
- [True, "Datenschutz und Datensicherheit"]
- [True, "Mangel an technischer Infrastruktur in einigen Schulen"]
- [True, "Notwendigkeit der Schulung von Lehrern und Schülern im Umgang mit KI"]
- [False, "Mangel an verfügbaren KI-Technologien für die Bildung", "Dies ist keine Herausforderung bei der Implementierung von KI in der Bildung"]
```
-->

---


## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: contains
  property: id
  value: fehlende-transparenz
```


---


## Chancen

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: effizienzsteigerung
- condition: contains
  property: id
  value: sprachliche-barrieren-aufloesen
```


---


## Links


---


## Quellen
