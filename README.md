# Project weather "rainbow:

## :sparkle: Team :sparkle:
### Poznaj nas!
- Bartosz Bukański
- Malwina Koziarska
- Kornelia Neugebauer
- Jan Zdaniewicz

## :scroll: Wstęp do problematyki :scroll:
Projekt składa się z pozyskanych danych z serwisu udostępniającego API meteorologiczne WorldWeatherOnilne. Chcemy, żeby nasz projekt działał offline. 

## :dart: Cel projektu :dart:
Jak wiemy pogoda jest trudna do przewidzenia, jest w stanie zmienić się w ułamku sekundy, co jest szczególnie widoczne w ostatnich latach. Pomimo tego chcemy stworzyć aplikację przewidywania pogody. Posiadając dane historyczne chcemy, by nasza aplikacja “przewidywała” - bardziej odpowiednie byłoby użycie słowa “wydedukowała”, jak najbardziej prawdopodobną prognozę pogody w określonym przedziale czasowym. 

## :closed_umbrella: Metodologia :open_umbrella:
### Sposób pozyskania danych
By posiadać aktualne dane wykorzystujemy pętlę for, która dostarcza nam danych ze wskazanego przedziału czasu. Dane pozyskane w ten sposób składają się z wielu zmiennych, między innymi: zaśnieżenie, widoczność oraz średnie parametrów mierzonych o wschodzi i zachodzie słońca lub o innych określonych godzinach. Na potrzeby naszego projektu, zdecydowaliśmy się zmniejszyć liczbę zmiennych do 5.  

Z pobranych danych z wybranego API wybieramy poniższe zmienne: 

Temperatura – brana pod uwagę średnia z danego dnia, wyrażana w jednostce miary stopni Celsjusza (°C); dodatkowo jest brana pod uwagę najniższa temperatura w ciągu dnia – noc oraz maksymalna temperatura - dzień. 

Zachmurzenie - średnie pokrycie nieba chmurami w ciągu wyznaczonego dnia, wyrażana jest w procentach (%), gdzie 0% oznacza bezchmurne niebo, a 100% – całkowite zachmurzenie. 

Czas solarny - jest to okres czasu, przez który Słońce znajduje się nad horyzontem w ciągu dnia, wyrażana w jednostce godzinowej (h). 

Wilgotność -mierzy ilości pary wodnej zawartej w powietrzu, wyrażana jest jako wilgotność względna w procentach (%), która wskazuje na stosunek aktualnej zawartości pary wodnej do maksymalnej możliwej zawartości w danych warunkach temperatury. 

Ciśnienie - to siła, jaką wywiera powietrze na jednostkę powierzchni, mierzona jest w hektopaskalach (hPa). 

### Wykorzystanie metody


## Aplikacja


### Wyniki


### Opis działania API


## Dyskusja


## Wnioski
