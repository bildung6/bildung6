---
id: leistungsbewertung
description: "KI als Assistent bei der Notenvergabe."
image: "anwendungsfälle/images/online_test.svg" 
tags:
- lehrende
title: Leistungsbewertung
type: usecase
---


## Beschreibung

Künstliche Intelligenz (KI) hat das Potenzial, in der Bewertung von Prüfungsleistungen eingesetzt zu werden. Insbesondere durch die Analyse von Texten und die Abgabe von Vorschlägen für Verbesserungen oder Noten könnte KI nützlich sein. Es wird auch darauf hingewiesen, dass KI-Systeme in manchen Fällen ähnliche Noten wie menschliche Prüfer vergeben (1).

Allerdings sind gängige KI-Modelle wie ChatGPT nicht speziell für diesen Zweck entwickelt worden und sollten daher mit Vorsicht verwendet werden. In Zukunft werden wohl spezialisierte Systeme entwickelt, die auf Basis der noch kommenden KI-Gesetze und Regularien zugelassen sind.

Bei der Nutzung von nicht bildungsspezifischen KI-Systemen wie ChatGPT müssen Lehrende die damit verbundenen Risiken im Auge behalten. Grundlegende Prinzipien im Umgang mit Datenschutz, Informationssicherheit und Urheberrecht gelten auch hier. Besonders sensibel ist der Umgang mit Personendaten und schützenswerten Informationen der Studierenden. 
Es gilt zu vermeiden, sensible Daten in die Systeme hochzuladen, da die Transparenz hinsichtlich der Datenverarbeitung durch Anbieter wie OpenAI derzeit nicht vollständig gegeben ist. Dies ist besonders wichtig, da solche Systeme mit grossen Datenmengen (darunter auch Chatverläufe) trainiert werden, und durch Angriffe könnten sensible Informationen preisgegeben werden (2–4).


## Nutzung von nicht bildungsspezifischen KI-Systemen

Generell sollten Chatbots wie ChatGPT eher als Unterstützung für Lehrende dienen, anstatt vollständig die Bewertung von Prüfungen zu übernehmen. Sie können beispielsweise verwendet werden, um nach der Benotung auf Aspekte hinzuweisen, die den menschlichen Bewertern entgangen sind, oder um Unterstützung bei der Formulierung von konstruktivem Feedback zu leisten.


**Einige KI-Anwendungsfälle bei der Bewertung von Prüfungsleistungen:**

- Schnellere Feedback-Generierung

- KI kann Aspekte entdecken, die menschlichen Bewertern entgehen könnten

- Unterstützung bei der Formulierung von konstruktivem Feedback


Chatbots sollten höchstens als Assistenzsysteme verwendet werden, und es ist fraglich, ob vollständig autonome KI-Systeme für die Notenvergabe entwickelt werden. Dies widerspiegelt sich in einem der zentralen Punkte des EU-AI Acts, der besagt, dass in kritischen Bereichen der Mensch die endgültige Entscheidungsgewalt behalten muss. Bei der Bewertung von Prüfungsleistungen bleibt also der Mensch als Entscheidungsträger unverzichtbar.


## Regulation 

Im Jahr 2024 verabschiedete die EU ein Gesetz zur umfassenden Regulierung von Künstlicher Intelligenz, den sogenannten „AI Act“. Dieses Gesetz verfolgt einen risikobasierten Ansatz: Bereiche der Gesellschaft werden nach ihrem Risikopotenzial eingestuft, und je höher das Risiko, desto strenger die Anforderungen bei der Entwicklung und Anwendung von KI-Systemen. 
Der Bildungssektor wurde dabei als Hochrisikoanwendung eingestuft, was bedeutet, dass strenge Anforderungen erfüllt werden müssen, bevor KI in Prüfungen oder zur Bewertung eingesetzt werden darf. Dies betrifft sowohl die Entwicklung als auch die Verwendung solcher Systeme im Bildungssektor. Bildungseinrichtungen und Lehrkräfte in der EU werden vermutlich verpflichtet, die Verwendung von KI transparent zu gestalten und sicherzustellen, dass sowohl das Personal als auch die Studierenden ausreichend im Umgang mit KI geschult sind. 

Wahrscheinlich werden in der Schweiz in absehbarer Zeit ähnliche Regulierungen eingeführt, da bereits eine Prüfung der EU-Regularien durch den Bundesrat in Auftrag gegeben wurde (5).



---


## Tools für diesen Anwendungsfall

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: leistungsbewertung-chatgpt
```

---


## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: equals
  property: id
  value: halluzinationen
- condition: equals
  property: id
  value: geschuetzte-daten
- condition: equals
  property: id
  value: nachvollziehbarkeit
```


---


## Chancen

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: entlastung-durch-automatisierung
- condition: contains
  property: id
  value: zweitmeinung
```


---


## Quellen

1.	Schwartmann R. Was es beim Einsatz von KI rechtlich zu beachten gibt. 2024 [cited 2024 Sep 27]. Was es beim Einsatz von KI rechtlich zu beachten gibt. Available from: https://www.forschung-und-lehre.de/lehre/autonom-wie-ein-tier-6415

2.	Campbell M, Jovanović M. Disinfecting AI: Mitigating Generative AI’s Top Risks. Computer. 2024 May;57(5):111–6. 

3.	Wang Y, Pan Y, Yan M, Su Z, Luan TH. A Survey on ChatGPT: AI–Generated Contents, Challenges, and Solutions. IEEE Open Journal of the Computer Society. 2023 Jan 1;4(01):280–302. 

4.	Kucharavy A, Plancherel O, Mulder V, Mermoud A, Lenders V, editors. Large Language Models in Cybersecurity: Threats, Exposure and Mitigation [Internet]. Cham: Springer Nature Switzerland; 2024 [cited 2024 Aug 27]. Available from: https://link.springer.com/10.1007/978-3-031-54827-7

5.	BAKOM. Künstliche Intelligenz und Recht [Internet]. BAKOM; 2023 [cited 2024 Aug 27]. Available from: https://www.admin.ch/gov/de/start/dokumentation/medienmitteilungen.msg-id-100501.html



---


## Links

Gesetzliches:

-	https://artificialintelligenceact.eu/

-	https://artificialintelligenceact.eu/high-level-summary/

-	https://artificialintelligenceact.eu/assessment/eu-ai-act-compliance-checker/

-	https://digilaw.ch/

Bildung:

-	https://www.forschung-und-lehre.de/schwerpunkt/kuenstliche-intelligenz

-	https://ki-campus.org/

-	https://ki-campus.org/sites/default/files/2023-04/2023-03_Diskussionspapier_KI_Bildung_Zukunftsszenarien_Handlungsfelder_KI-Campus.pdf

-	https://www.lch.ch/fileadmin/user_upload_lch/Politik/Positionspapiere/240429_Positionspapier_KI_in_der_Schule_Kurzversion.pdf

-	https://www.swissuniversities.ch/fileadmin/swissuniversities/Dokumente/Lehre/Themen/Digitalisierung/240305_Positionspapier_KI_swissuniversities_de.pdf

-	https://ethz.ch/de/die-eth-zuerich/lehre/ai-in-education.html


---

---

## Über diesen Beitrag

Beim Verfassen dieses Beitrags haben die Autor:innen ChatGPT-4o (Ver. 27.09.2024) verwendet, um die sprachliche Darstellung ihrer Gedanken zu verbessern. Die volle Verantwortung für den Inhalt liegt bei den Autor:innen. 


---