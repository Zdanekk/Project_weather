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
By posiadać aktualne dane wykorzystujemy pętlę for, która dostarcza nam danych ze wskazanego przedziału czasu. Dane pozyskane w ten sposób składają się z wielu zmiennych, między innymi: zaśnieżenie, widoczność oraz średnie parametrów mierzonych o wschodzi i zachodzie słońca lub o innych określonych godzinach. Na potrzeby naszego projektu, zdecydowaliśmy się zmniejszyć liczbę zmiennych do 5.  

Z pobranych danych z wybranego API wybieramy poniższe zmienne: 

* Temperatura – brana pod uwagę średnia z danego dnia, wyrażana w jednostce miary stopni Celsjusza (°C). 

* Zachmurzenie - średnie pokrycie nieba chmurami w ciągu wyznaczonego dnia, wyrażana jest w procentach (%), gdzie 0% oznacza bezchmurne niebo, a 100% – całkowite zachmurzenie. 

* Czas solarny - jest to okres czasu, przez który Słońce znajduje się nad horyzontem w ciągu dnia, wyrażana w jednostce godzinowej (h). 

* Wilgotność -mierzy ilości pary wodnej zawartej w powietrzu, wyrażana jest jako wilgotność względna w procentach (%), która wskazuje na stosunek aktualnej zawartości pary wodnej do maksymalnej możliwej zawartości w danych warunkach temperatury. 

* Ciśnienie - to siła, jaką wywiera powietrze na jednostkę powierzchni, mierzona jest w hektopaskalach (hPa). 

### Wykorzystane metody :speech_balloon:


## Aplikacja :iphone:
ARIMA (Autoregressive Integrated Moving Average) to jeden z najbardziej popularnych modeli statystycznych stosowanych do analizy 
i prognozowania szeregów czasowych. Model ARIMA łączy trzy kluczowe komponenty:

* Autoregressive (AR): Część autoregresyjna modelu opisuje, jak bieżące wartości serii czasowej zależą od jej przeszłych wartości. Parametr 𝑝 oznacza liczbę poprzednich wartości, które są brane pod uwagę.

* Integrated (I): Część zintegrowana modelu odnosi się do różnicowania danych w celu uczynienia serii czasowej stacjonarną. Parametr 
𝑑 wskazuje, ile razy dane muszą być zróżnicowane, aby osiągnąć stacjonarność.

* Moving Average (MA): Część średniej ruchomej modelu opisuje, jak bieżące wartości serii czasowej są związane z błędami prognozowania (residuals) z przeszłości. Parametr q oznacza liczbę wcześniejszych błędów prognozy, które są brane pod uwagę.

Model ARIMA jest często oznaczany jako ARIMA(p,d,q), gdzie 𝑝, 𝑑 i 𝑞 są wyżej wymienionymi parametrami.

### Wyniki :1st_place_medal:


### Opis działania API :lab_coat:


## Dyskusja :lips:


## Wnioski :fireworks:
