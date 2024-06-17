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
Aplikacja zaczyna się od importowania potrzebnych bibliotek i utworzenia instancji aplikacji Flask. Następnie definiuje klucz API i lokalizację, dla której będą pobierane dane pogodowe, w tym przypadku Londyn.

Funkcja generate_weather_api_urls tworzy listę URLi do API pogodowego dla ostatnich sześciu lat, generując jeden URL na każdy miesiąc w roku. Każdy URL zawiera dane dotyczące średnich temperatur dla określonego miesiąca.

Po wygenerowaniu URLi, funkcja extract_weather_data wyciąga daty i średnie temperatury z odpowiedzi API i zapisuje je w odpowiednim formacie.

Główny endpoint aplikacji /weather_forecast obsługuje żądania GET. Po wywołaniu tego endpointu, generowane są URL-e do API, a następnie pobierane są dane pogodowe. Dane te są przetwarzane i zapisywane w DataFrame z Pandas, gdzie daty są ustawiane jako indeks, a średnie temperatury są konwertowane na liczby całkowite.

Dane są następnie dzielone na zbiór treningowy (dane z lat 2018-2022) i testowy (dane z lat 2023-2024), agregowane na poziomie miesięcznym. Model ARIMA jest tworzony i dopasowywany do danych treningowych. Model ten jest następnie używany do przewidywania średnich temperatur na okres testowy.

Prognozy są zapisywane w DataFrame i indeksowane odpowiednimi datami. Obliczany jest błąd średniokwadratowy (MSE) między rzeczywistymi a przewidywanymi wartościami. Wyniki, w tym prognozy i MSE, są zwracane w formacie JSON poprzez jsonify.

Aplikacja jest uruchamiana na serwerze Flask na porcie 5001 w trybie debugowania, co umożliwia łatwe testowanie i rozwijanie kodu. W ten sposób, kod ten pobiera dane pogodowe, przetwarza je, buduje model prognostyczny i zwraca wyniki jako JSON poprzez endpoint /weather_forecast.

## Dyskusja :lips:


## Wnioski :fireworks:
