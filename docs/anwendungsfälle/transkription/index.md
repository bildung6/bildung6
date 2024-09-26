---
id: transkription
description: "Nutze die KI für Speech-to-Text Aufgaben, indem du sie Gespräche in Text überführen lässt."
image: "anwendungsfälle/images/recording_transkription.svg" 
tags:
- studierende
title: Transkription 
type: usecase
---



# Transkription generieren

Generative KI-Modelle spielen eine zunehmend wichtige Rolle im Bereich der Speech-to-Text-Technologien. Diese Modelle sind darauf ausgelegt, gesprochene Sprache in Text zu transkribieren. Durch den Einsatz grosser Datenmengen und fortgeschrittener Architekturen, wie zum Beispiel Transformer- und Diffusionsmodelle, können sie komplexe Sprachmuster erkennen und in Text umwandeln.

Der Einsatz von generativer KI für Speech-to-Text basiert auf der Fähigkeit dieser Modelle, nicht nur vorhandene Muster in Daten zu erkennen, sondern auch neue Inhalte zu generieren, wenn die Eingabe unscharf oder unvollständig ist. Dies ist besonders nützlich in Szenarien, in denen die Audioqualität schlecht ist oder Hintergrundgeräusche die Verständlichkeit beeinträchtigen. Generative Modelle lernen aus grossen, vielfältigen Datensätzen und sind somit in der Lage, selbst komplexe und mehrsprachige Transkriptionen zu erstellen, ohne dass spezifisches Fine-Tuning für jede Sprache oder Aufgabe erforderlich ist (1).

Generative KI-Modelle wie OpenAI's Whisper bieten hohe Transkriptionsgenauigkeit und können flexibel in verschiedenen Sprachen und Aufgabenbereichen eingesetzt werden, ohne spezifische Anpassungen an neue Sprachen oder Dialekte zu benötigen, was ihre Vielseitigkeit erhöht (1). Ein Nachteil dieser Modelle ist jedoch das Auftreten von Halluzinationen, bei denen nicht vorhandene Inhalte generiert werden, was potenziell schädlich sein kann, besonders bei Sprechern mit Sprachstörungen wie Aphasie (2). Modelle wie Whisper setzen Massstäbe in der Spracherkennung, zeigen aber Schwächen bei bestimmten Sprechergruppen, während andere Ansätze wie Generative Spoken Language Modeling auf unüberwachtem Lernen basieren und Sprache direkt aus rohen Audioaufnahmen modellieren (3).



---



## Tools für diesen Anwendungsfall


```yaml
condition: or
entityType: usecase
rules:
- condition: contains
  property: id
  value: mac-whisper
```



---


## Chancen

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: sprachliche-barrieren-aufloesen
- condition: contains
  property: id
  value: entlastung-durch-automatisierung.md
```


---


## Über diesen Beitrag

Beim Verfassen dieses Beitrags haben die Autor:innen ChatGPT 4o (Ver. 09.09.2024) verwendet, um die sprachliche Darstellung ihrer Gedanken zu verbessern. Die volle Verantwortung für den Inhalt liegt bei den Autor:innen. 


---


## Quellen


1.	Radford A, Kim JW, Xu T, Brockman G, McLeavey C, Sutskever I. Robust speech recognition via large-scale weak supervision. In: Proceedings of the 40th International Conference on Machine Learning. Honolulu, Hawaii, USA: JMLR.org; 2023. p. 28492–518. (ICML’23; vol. 202). 


2.	Koenecke A, Choi ASG, Mei KX, Schellmann H, Sloane M. Careless Whisper: Speech-to-Text Hallucination Harms. In: Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency [Internet]. New York, NY, USA: Association for Computing Machinery; 2024 [cited 2024 Aug 23]. p. 1672–81. (FAccT ’24). Available from: https://dl.acm.org/doi/10.1145/3630106.3658996


3.	Lakhotia K, Kharitonov E, Hsu WN, Adi Y, Polyak A, Bolte B, et al. On Generative Spoken Language Modeling from Raw Audio. Roark B, Nenkova A, editors. Transactions of the Association for Computational Linguistics. 2021;9:1336–54. 




