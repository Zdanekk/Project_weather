# Project weather :rainbow:

## Team :sparkle:
### Poznaj nas!
- Bartosz Bukański
- Malwina Koziarska
- Kornelia Neugebauer
- Jan Zdaniewicz

## Wstęp do problematyki :scroll:
Projekt składa się z pozyskanych danych z serwisu udostępniającego API meteorologiczne WorldWeatherOnilne. Chcemy, żeby nasz projekt działał offline. 

## Cel projektu :dart:
Jak wiemy pogoda jest trudna do przewidzenia, jest w stanie zmienić się w ułamku sekundy, co jest szczególnie widoczne w ostatnich latach. Pomimo tego chcemy stworzyć aplikację przewidywania pogody. Posiadając dane historyczne chcemy, by nasza aplikacja “przewidywała” - bardziej odpowiednie byłoby użycie słowa “wydedukowała”, jak najbardziej prawdopodobną prognozę pogody w określonym przedziale czasowym. 

## Metodologia :open_umbrella:
### Sposób pozyskania danych :page_with_curl:
By posiadać aktualne dane wykorzystujemy pętlę for, która dostarcza nam danych ze wskazanego przedziału czasu. Dane pozyskane w ten sposób składają się z wielu zmiennych, między innymi: zaśnieżenie, widoczność oraz średnie parametrów mierzonych o wschodzi i zachodzie słońca lub o innych określonych godzinach. Na potrzeby naszego projektu, zdecydowaliśmy się zmniejszyć pobieraną liczbę zmiennych do 5.  

Z pobranych danych z wybranego API wybieramy poniższe zmienne: 

* Temperatura – brana pod uwagę średnia z danego dnia, wyrażana w jednostce miary stopni Celsjusza (°C). 

* Zachmurzenie - średnie pokrycie nieba chmurami w ciągu wyznaczonego dnia, wyrażana jest w procentach (%), gdzie 0% oznacza bezchmurne niebo, a 100% – całkowite zachmurzenie. 

* Czas solarny - jest to okres czasu, przez który Słońce znajduje się nad horyzontem w ciągu dnia, wyrażana w jednostce godzinowej (h). 

* Wilgotność -mierzy ilości pary wodnej zawartej w powietrzu, wyrażana jest jako wilgotność względna w procentach (%), która wskazuje na stosunek aktualnej zawartości pary wodnej do maksymalnej możliwej zawartości w danych warunkach temperatury. 

* Ciśnienie - to siła, jaką wywiera powietrze na jednostkę powierzchni, mierzona jest w hektopaskalach (hPa). 

Postanowiliśmy skupić się na jednej zmiennej, która wydaje nam się być najbardziej istotną, czyli temperaturę.

### Wykorzystane metody :speech_balloon:
W trakcie tworzenia naszego projektu wykorzystaliśmy model statystyczny ARIMA -  AutoRegressive Integrated Moving Average. Pozwolił on nam na przeanalizowanie danych historycznych i na ich podstawie sprognozował pogode na wyznaczony przez nas okres czasu. 

Konkretniej model ARIMA prognozuje szeregi czasowe, które sa danymi rejestrowanymi, obserwowanymi lub mierzonymi w równych odstępach czasu (sezonowość). W naszym przypadku jest to rejestracja średniej temperatury w ciągu dnia, która następnie jest uśredniana dla danego miesiąca od 2018 do 2023 roku.

W celu analizy naszych danych wykorzystujemy bibliotekę "pmdarima" i zawartą w niej funkcję "pm.auto_arima()", gdzie zmienna m przyjmuje stałą wartość równą 12. Co wskazuje na nasz zamiar prognozowania pogody po miesiącach.

## Aplikacja :iphone:
### Wyniki :1st_place_medal:


### Opis działania API :lab_coat:


## Dyskusja :lips:


## Wnioski :fireworks:
