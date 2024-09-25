---
description: "Nutze ChatGPT, um einen Draft für eine PESTEL-Analyse zu erstellen."
id: pestel-chatgpt
image: "anwendungsfälle/images/processing_thoughts_pestel.svg"
tags:
- studierende
title: PESTEL-Analyse generieren mit ChatGPT
type: usecase
---


# PESTEL generieren mit ChatGPT

V. Bilgram et al. untersuchten den Einsatz von KI in frühen Innovationsphasen, um neue Perspektiven zu eröffnen und die Ideenvielfalt zu erhöhen. Dabei nutzten sie unter anderem die PESTEL-Analyse im Automobilmarkt (1).

*PESTEL-Analyse: Dieses Tool hilft, externe Einflussfaktoren zu identifizieren, darunter politische, wirtschaftliche, soziale, technologische, ökologische und rechtliche Aspekte. Bilgram und Laarmann setzten PESTEL ein, um systematisch externe Faktoren im Automobilmarkt zu analysieren.*

Nutze den untenstehenden Prompt, um dir einen Ausgangsentwurf für deine PESTEL-Analyse zu erstellen. Gerne kannst du das originale Papier nachschlagen (siehe die Quellenangabe unten). Die Autoren verwendeten den Chatbot auch für andere Anwendungsfälle wie "Bedarfsermittlung", "Personas erstellen" und "Ideenfindung".


## Beispiel

<table >
  <tr>
    <th>Beispiel</th>
  </tr>
  <tr>
    <td bgcolor="5D6CC0"><p style="color:white"><i>Input:</i></p></td>
  </tr>
  <tr>
    <td bgcolor="5D6CC0">
      <p style="color:white"><strong>
      Führe eine PESTEL-Analyse des Automobilmarktes durch. Erstelle eine Tabelle.<strong>
    </td>
  </tr>
  <tr>
    <td bgcolor="white"><i>Output:</i></td>
  </tr>
  <tr>
    <td bgcolor="white">

      Natürlich! Die PESTEL-Analyse untersucht die politischen, wirtschaftlichen, sozialen, technologischen, ökologischen und rechtlichen Faktoren, die Einfluss auf ein bestimmtes Marktumfeld haben. Hier ist eine Tabelle, die die PESTEL-Faktoren für den Automobilmarkt darstellt:<br>

      <h3>PESTEL-Analyse des Automobilmarktes</h1>
      <table>
          <thead>
              <tr>
                  <th>Faktor</th>
                  <th>Beschreibung</th>
              </tr>
          </thead>
          <tbody>
              <tr>
                  <td>Politisch</td>
                  <td>
                      <ul>
                          <li><strong>Regulierungen:</strong> Verschärfte Abgasnormen, Emissionsvorschriften und Sicherheitsstandards.</li>
                          <li><strong>Subventionen:</strong> Staatliche Förderungen für Elektrofahrzeuge und andere umweltfreundliche Technologien.</li>
                          <li><strong>Handelsabkommen:</strong> Einfluss von Handelsabkommen auf Import- und Exportzölle.</li>
                      </ul>
                  </td>
              </tr>
              <tr>
                  <td>Wirtschaftlich</td>
                  <td>
                      <ul>
                          <li><strong>Konjunkturzyklen:</strong> Wirtschaftliche Abschwünge oder Booms beeinflussen die Nachfrage nach Autos.</li>
                          <li><strong>Rohstoffpreise:</strong> Preisschwankungen bei Rohstoffen wie Stahl und Lithium.</li>
                          <li><strong>Wechselkurse:</strong> Auswirkungen von Wechselkursen auf die Kosten und Preise für importierte Komponenten.</li>
                      </ul>
                  </td>
              </tr>
              <tr>
                  <td>Sozial</td>
                  <td>
                      <ul>
                          <li><strong>Veränderungen im Konsumverhalten:</strong> Wachsende Präferenz für umweltfreundliche und vernetzte Fahrzeuge.</li>
                          <li><strong>Demografische Veränderungen:</strong> Alternde Bevölkerung und unterschiedliche Mobilitätsbedürfnisse.</li>
                          <li><strong>Urbanisierung:</strong> Wachsende Städte und deren Einfluss auf den Bedarf an verschiedenen Fahrzeugtypen.</li>
                      </ul>
                  </td>
              </tr>
              <tr>
                  <td>Technologisch</td>
                  <td>
                      <ul>
                          <li><strong>Innovation:</strong> Fortschritte in der Elektromobilität, autonomem Fahren und vernetzter Fahrzeugtechnologie.</li>
                          <li><strong>Forschung & Entwicklung:</strong> Investitionen in neue Technologien und Verbesserungen bestehender Systeme.</li>
                          <li><strong>Digitalisierung:</strong> Integration von IT-Lösungen und digitalen Plattformen in Fahrzeugen.</li>
                      </ul>
                  </td>
              </tr>
              <tr>
                  <td>Ökologisch</td>
                  <td>
                      <ul>
                          <li><strong>Umweltvorschriften:</strong> Strengere Emissionsvorschriften und Anforderungen an die Energieeffizienz.</li>
                          <li><strong>Nachhaltigkeit:</strong> Steigender Druck zur Reduktion von CO₂-Emissionen und Verbesserung der ökologischen Bilanz.</li>
                          <li><strong>Ressourcenschonung:</strong> Fokus auf Recycling und nachhaltige Nutzung von Rohstoffen.</li>
                      </ul>
                  </td>
              </tr>
              <tr>
                  <td>Rechtlich</td>
                  <td>
                      <ul>
                          <li><strong>Gesetzgebung:</strong> Änderungen in Gesetzen und Vorschriften bezüglich Sicherheit, Umwelt und Haftung.</li>
                          <li><strong>Produkthaftung:</strong> Anforderungen an die Sicherheit und Haftung für Fahrzeugfehler oder -mängel.</li>
                          <li><strong>Datenschutz:</strong> Regelungen zum Schutz von Nutzerdaten, insbesondere bei vernetzten Fahrzeugen.</li>
                      </ul>
                  </td>
              </tr>
          </tbody>
      </table>
  </tr>
  <tr>
    <td  bgcolor="f1f1f1"><i>Chatverlauf: Mit ChatGPT PESTEL generieren. Nutze diesen <a href="https://chatgpt.com/share/d9201785-d505-447b-85c1-3d0fc2956a80"> Link,</a>um den Chatverlauf (ChatGPT 4o mini) zu diesem Beispiel anzuschauen. Ursprünglicher englischer Prompt wurde von V. Bilgram et al. erstellt.</a></i>
    </td>
  </tr>
</table>



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
- condition: contains
  property: id
  value: bias-diskriminierung
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

## Über diesen Beitrag

Beim Verfassen dieses Beitrags haben die Autor:innen ChatGPT 4o (Ver. 02.09.2024) verwendet, um die sprachliche Darstellung ihrer Gedanken zu verbessern. Die volle Verantwortung für den Inhalt liegt bei den Autor:innen. 


---


## Links

OpenAI, ChatGPT-Entwicklerseite:

- https://openai.com/


Chatverlauf:

- https://chatgpt.com/share/d9201785-d505-447b-85c1-3d0fc2956a80


---


## Quelle

1. Bilgram V, Laarmann F. Accelerating Innovation With Generative AI: AI-Augmented Digital Prototyping and Innovation Methods. IEEE Eng Manag Rev. 2023;51(2):18–25. 


