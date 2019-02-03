Celem projektu jest napisanie bota grającego w Light Riders (gra dostępna na: https://playground.riddles.io/competitions/light-riders).  

Głównym plikiem projektu jest plik: main.py. Wywołuje się w nim funkcję z główną pętlą programu z klasy Game.  

Aby uruchomić bota na serwerze, należy cały projekt spakować zipem i przesłać na serwer. Tam zostanie on skompilowany, 
a następnie przeprowadzony zostanie przykładowy mecz. Jeśli kompilacja się powiedzieć bot może zostać aktywowany i piąć się w rankingu.

API gry na początku meczu przesyła niezbędne informacje takie jak: wymiary planszy, id gracza, czas na wykonanie ruchu, jak 
i reprezentacje planszy w postaci stringa. Następnie po każdym ruchu przesyła aktualny stan planszy również w stringu, a jako odpowiedzi oczekuje wyłącznie kierunku 
w którym ma udać się nasz bot.  
