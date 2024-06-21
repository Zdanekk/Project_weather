# Project weather :rainbow:

## Team :sparkle:
### Poznaj nas!
- Bartosz Bukański
- Malwina Koziarska
- Kornelia Neugebauer
- Jan Zdaniewicz

## Wstęp do problematyki :scroll:
Prognozowanie pogody jest kluczowym aspektem naszego codziennego życia. Wpływa na wiele dziedzin, od rolnictwa, przez transport, aż po planowanie wydarzeń. Dokładne przewidywanie warunków atmosferycznych może pomóc w zapobieganiu katastrofom naturalnym, optymalizacji upraw rolnych czy planowaniu działań ratunkowych. 

W ostatnich latach zmiany klimatyczne sprawiają, że przewidywanie pogody staje się coraz bardziej złożone i trudne. Nieregularne wzorce pogodowe, częstsze występowanie ekstremalnych zjawisk atmosferycznych, takich jak burze, susze czy powodzie, wymuszają na naukowcach i meteorologach stosowanie bardziej zaawansowanych metod analizy i prognozowania danych pogodowych. 

Projekt, który realizujemy, ma na celu stworzenie aplikacji, która będzie prognozować pogodę na podstawie danych historycznych pozyskanych z serwisu WorldWeatherOnline. Istotnym elementem naszego podejścia jest możliwość działania aplikacji w trybie offline, co pozwala na niezależność od ciągłego dostępu do internetu i zapewnia użytkownikom dostęp do prognoz w każdych warunkach. 

Dzięki wykorzystaniu modelu statystycznego ARIMA (AutoRegressive Integrated Moving Average), który analizuje i prognozuje szeregi czasowe, chcemy stworzyć narzędzie, które nie tylko przewidzi pogodę, ale również dostarczy najbardziej prawdopodobnych scenariuszy na podstawie danych z przeszłości. Nasz projekt koncentruje się na analizie średnich temperatur, co stanowi fundament do dalszego rozwijania modelu i uwzględniania innych zmiennych pogodowych w przyszłości. 

Celem projektu jest nie tylko stworzenie dokładnej prognozy pogody, ale także zrozumienie mechanizmów i wzorców, które kształtują warunki atmosferyczne. Wierzymy, że nasze podejście przyczyni się do lepszego zrozumienia zjawisk pogodowych i pomoże w podejmowaniu bardziej świadomych decyzji w różnych dziedzinach życia. 

## Cel projektu :dart:
Jak wiemy pogoda jest trudna do przewidzenia, jest w stanie zmienić się w ułamku sekundy, co jest szczególnie widoczne w ostatnich latach. Pomimo tego chcemy stworzyć aplikację przewidywania pogody. Posiadając dane historyczne chcemy, by nasza aplikacja “przewidywała” - bardziej odpowiednie byłoby użycie słowa “wydedukowała”, jak najbardziej prawdopodobną prognozę pogody w określonym przedziale czasowym. 

## Metodologia :open_umbrella:
### Sposób pozyskania danych :page_with_curl:
Dane pogodowe dla Londynu zostały pozyskane za pomocą API ze strony WorldWeatherOnline z wykorzystaniem klucza. Aby uzyskać niezbędne dane historyczne, stworzyliśmy skrypt w Pythonie, który iteruje przez wskazany przedział czasowy, pobierając dane dla każdego miesiąca od stycznia 2018 roku do grudnia 2023 roku. Skrypt ten generuje dla każdego roku i miesiąca listę URL wykorzystywany do odpytywania za pomocą API strony WorldWeatherOnline. Otrzymane dane są przetwarzane przez funkcję extract_weather_data w celu wyciągnięcia kluczowych parametrów pogodowych takich jak maksymalna temperatura, minimalna temperatura, średnia temperatura czy ciśnienie. Do dalszej analizy wzięliśmy pod uwagę jedynie średnia temperaturę. Na koniec dane są konwertowane do obiektu DataFrame biblioteki Pandas (df), co pozwala na łatwiejsze analizowanie i manipulowanie danymi pogodowymi. Następnie zapisujemy dane z naszego DataFrame do pliku CSV, który będzie wykorzystywany w dalszej części projektu.   

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

Opis modelu ARIMA: 

Model ARIMA składa się z trzech głównych komponentów: 

Autoregresja (AR): Uwzględnia zależność zmiennej od jej wcześniejszych wartości. 

Integracja (I): Używa różnicowania do usunięcia trendów i uczynienia szeregu czasowego stacjonarnym. 

Średnia ruchoma (MA): Modeluje zależność zmiennej od błędów prognozy z poprzednich okresów. 

Aby dopasować model ARIMA do naszych danych, skorzystaliśmy z biblioteki pmdarima, która umożliwia automatyczne dostrojenie parametrów modelu za pomocą funkcji pm.auto_arima(). Dzięki temu proces modelowania został uproszczony, a uzyskane prognozy były bardziej precyzyjne. 

## Aplikacja :iphone:

### Wyniki :1st_place_medal:
Nasza aplikacja wygenerowała następujące prognozy dla średnich temperatur w Londynie na rok 2023: 

Na wykresie widoczna jest wyraźna sezonowość temperatur, z najwyższymi wartościami w miesiącach letnich (czerwiec-sierpień) i najniższymi w miesiącach zimowych (grudzień-luty). Prognozy modelu ARIMA (czerwona linia) dobrze odzwierciedlają rzeczywiste temperatury (niebieska linia), co wskazuje na wysoką dokładność modelu. Niewielkie odchylenia między prognozowanymi a rzeczywistymi wartościami są naturalne i mogą wynikać z nieprzewidywalnych czynników pogodowych. 

Model ARIMA skutecznie uchwycił wzorce sezonowe w danych historycznych, co pozwoliło na generowanie wiarygodnych prognoz na przyszłość. Błąd średniokwadratowy (MSE) między prognozowanymi a rzeczywistymi wartościami wynosi 1.5, co wskazuje na stosunkowo niską różnicę między prognozami a rzeczywistością. 

Projekt ten pokazuje, że możliwe jest stworzenie dokładnego narzędzia do prognozowania pogody działającego offline, co może być szczególnie przydatne w sytuacjach, gdzie dostęp do Internetu jest ograniczony lub niemożliwy. Dzięki zastosowaniu zaawansowanych metod analizy danych, nasza aplikacja dostarcza wartościowych informacji, które mogą być wykorzystane w różnych dziedzinach życia.

### Opis działania API :lab_coat:
Aplikacja zaczyna się od importowania potrzebnych bibliotek i utworzenia instancji aplikacji Flask. Następnie definiuje klucz API i lokalizację, dla której będą pobierane dane pogodowe, w tym przypadku Londyn.

Funkcja generate_weather_api_urls tworzy listę URLi do API pogodowego dla ostatnich sześciu lat, generując jeden URL na każdy miesiąc w roku. Każdy URL zawiera dane dotyczące średnich temperatur dla określonego miesiąca.

Po wygenerowaniu URLi, funkcja extract_weather_data wyciąga daty i średnie temperatury z odpowiedzi API i zapisuje je w odpowiednim formacie.

Główny endpoint aplikacji /weather_forecast obsługuje żądania GET. Po wywołaniu tego endpointu, generowane są URL-e do API, a następnie pobierane są dane pogodowe. Dane te są przetwarzane i zapisywane w DataFrame z Pandas, gdzie daty są ustawiane jako indeks, a średnie temperatury są konwertowane na liczby całkowite.

Dane są następnie dzielone na zbiór treningowy (dane z lat 2018-2022) i testowy (dane z lat 2023-2024), agregowane na poziomie miesięcznym. Model ARIMA jest tworzony i dopasowywany do danych treningowych. Model ten jest następnie używany do przewidywania średnich temperatur na okres testowy.

Prognozy są zapisywane w DataFrame i indeksowane odpowiednimi datami. Obliczany jest błąd średniokwadratowy (MSE) między rzeczywistymi a przewidywanymi wartościami. Wyniki, w tym prognozy i MSE, są zwracane w formacie JSON poprzez jsonify.

Aplikacja jest uruchamiana na serwerze Flask na porcie 5001 w trybie debugowania, co umożliwia łatwe testowanie i rozwijanie kodu. W ten sposób, kod ten pobiera dane pogodowe, przetwarza je, buduje model prognostyczny i zwraca wyniki jako JSON poprzez endpoint /weather_forecast.

Opis działania aplikacji 

Struktura aplikacji 

Aplikacja została zbudowana przy użyciu frameworka Flask, który umożliwia tworzenie aplikacji webowych w Pythonie. Główne komponenty aplikacji to: 

Flask - Framework do tworzenia aplikacji webowych. 

Pandas - Biblioteka do manipulacji i analizy danych. 

Pmdarima - Biblioteka do modelowania szeregów czasowych. 

Sklearn - Biblioteka do oceny modelu. 

Przepływ danych w aplikacji 

Wczytywanie danych: Dane pogodowe są wczytywane z pliku CSV, przekształcane na odpowiedni format oraz przygotowywane do analizy. 

Ładowanie modelu: Model ARIMA, który został wcześniej wytrenowany, jest wczytywany z pliku pickle. 

Prognozowanie: Model ARIMA generuje prognozy dla wybranego okresu.

Endpoint /weather_forecast jest głównym punktem dostępu do prognoz pogodowych generowanych przez naszą aplikację. Obsługuje on żądania typu GET.

## Dyskusja :lips:
Podczas realizacji projektu napotkaliśmy kilka wyzwań, które wpłynęły na ostateczny kształt aplikacji. 

Dostępność i jakość danych: Pobieranie danych historycznych z API WorldWeatherOnline było stosunkowo proste. Nie było braków w danych, więc sprawdzanie danych nie było czasochłonne.  

Wybór modelu: Model ARIMA okazał się skuteczny w prognozowaniu średnich temperatur dzięki swojej zdolności do uwzględniania sezonowości i trendów długoterminowych. Niemniej jednak, ARIMA ma swoje ograniczenia, takie jak wrażliwość na dane wejściowe i konieczność stacjonarności szeregu czasowego. 

Skalowalność i wydajność: Implementacja aplikacji w Flask była odpowiednia dla realizacji celów tego projektu. Jednakże, w przypadku większej ilości danych, konieczne może być zastosowanie bardziej skalowalnych rozwiązań, takich jak serwery w chmurze czy bardziej zaawansowane frameworki webowe. 

## Przyszłe działania :fireworks:
Istnieje wiele możliwości rozszerzenia i ulepszenia projektu w przyszłości: 

Uwzględnienie większej liczby zmiennych: Choć skupiliśmy się na średnich temperaturach, dodanie innych zmiennych pogodowych (wilgotność, ciśnienie, zachmurzenie) mogłoby poprawić dokładność prognoz i dostarczyć bardziej kompleksowych informacji. 

Wykorzystanie bardziej zaawansowanych modeli: W przyszłości warto rozważyć wykorzystanie bardziej zaawansowanych metod uczenia maszynowego, takich jak sieci neuronowe LSTM (Long Short-Term Memory) czy XGBoost, które mogą lepiej uchwycić skomplikowane wzorce w danych pogodowych. 

Integracja z innymi źródłami danych: Możliwość integracji danych z innych źródeł, takich jak stacje meteorologiczne czy inne serwisy pogodowe, mogłaby poprawić jakość danych wejściowych i zwiększyć dokładność prognoz. 

Rozwój interfejsu użytkownika: Obecny interfejs użytkownika jest prosty i funkcjonalny, ale istnieje możliwość jego rozszerzenia o bardziej zaawansowane funkcje, takie jak wizualizacje prognoz, interaktywne mapy czy powiadomienia dla użytkowników. 

Optymalizacja działania offline: Dalsza optymalizacja działania aplikacji w trybie offline, poprzez lepsze zarządzanie pamięcią i bardziej efektywne algorytmy, może zwiększyć jej użyteczność w miejscach z ograniczonym dostępem do Internetu. 
