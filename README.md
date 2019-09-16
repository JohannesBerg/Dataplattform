# Dataplattform

[Wiki](https://github.com/knowit/Dataplattform/wiki/)

[Board](https://github.com/knowit/Dataplattform/projects/1) med backlog etter sommeren

## Hente ut data fra dataplattformen

[Swagger](https://knowit.github.io/Dataplattform/)

## Sende inn data

[Sende inn data](https://github.com/knowit/Dataplattform/wiki/Legge-til-en-ny-datatype-(datakilde\) )

[Eksempel av innsending](https://github.com/knowit/Dataplattform/wiki/Eksempel:-sende-inn-data-til-dataplattformen)

## Mappestruktur
  * ```hardware-code/```
      * Her er alle de forskjellige programmene skrevet for bruk til fysiske bokser.
  * ```services/```
      * Denne inneholder alle `serverless` services som deployes til AWS.


## Oppsett
Se ```services/README.md``` for deploying til AWS og oppsett av QuickSight.
Spør i `#dataplattform` på Slack for nøkler, tilgang, osv.


## Disse datakildene kan inneholde persondata:
  * github
      * Github har potensielt sensitiv informasjon, her blir det lagret både navn, e-post addresse
      og commit-melding, men vi filtrerer ut alt som ikke kommer fra offentlige repoer. Se
      ```services/ingest/ingest/filters.py```.
  * slack
      * Slack webhooks kan inneholde alt, avhengig av hvordan integrasjons-appen er konfigurert.
      Vi tar bare vare på tidspunkt og kanal for meldinger skrevet i offentlige kanaler.
      Se ```services/ingest/ingest/filters.py```.
      For reactions til meldinger lagrer vi kanal, tidspunkt og hvilken emoticon som ble brukt.
  * knowitlabs (blogg)
      * Vi scraper knowitlabs.no og lagrer litt offentlig informasjon om hvert blogginnlegg, som
        tittel, undertittel, forfatter og tidspunkt.
