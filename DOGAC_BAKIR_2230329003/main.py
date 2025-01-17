"""
Bir "Catch The Turtle" adlı oyunu oluşturur.
Turtle ekranda rastgele konumlarda belirip kaybolur
ve kullanıcı tıklayarak puan kazanmaya çalışır.
Belirli bir süre sonunda oyun biter.
"""

import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")

FONT = ('Arial', 30, 'normal')
score = 0
game_over = False

# turtle list
turtle_list = []

# score turtle
score_turtle = turtle.Turtle()

# countdown turtle
countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    """
    Skoru gösterecek 'score_turtle' nesnesinin temel ayarlarını yapar:
      - Rengi, pozisyonu, font ayarları vb.
    """
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height()
    y = top_height * 0.91

    score_turtle.setpos(0, 300)
    score_turtle.write(arg="score: 0", move=False, align="center", font=FONT)

grid_size = 15

def make_turtle(x, y):
    """
    Verilen x ve y koordinatlarına göre bir turtle nesnesi oluşturur.
    - Tıklanınca skoru artıracak onclick fonksiyonu tanımlar.
    - Turtle görünüm, renk, boyut, ve konum ayarlarını yapar.
    - turtle_list listesine ekler.
    """
    t = turtle.Turtle()

    def handle_click(x_click, y_click):
        """
        Turtle'a tıklandığında skor artırma işlevini yapar,
        ardından ekrana yeni skoru yazar.
        """
        global score
        if not game_over:
            score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(1.5, 1.5)
    t.color("dark green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)

# Örnek x ve y koordinatları listeleri
x_coordinates = [-15, -10, 0, 10, 10]
y_coordinates = [15, 10, 0, -10]

def setup_turtles():
    """
    x_coordinates ve y_coordinates listelerini kullanarak
    ekrana çoklu turtle nesneleri yerleştirir.
    """
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    """
    Tüm turtle nesnelerini (turtle_list) gizler (hideturtle).
    """
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    """
    Oyun bitmediyse:
      1) Tüm turtle'ları gizler.
      2) Rastgele birini görünür hâle getirir (showturtle).
      3) 500 ms sonra yeniden aynı fonksiyonu çağırır (rekürsif).
    """
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    """
    Geri sayım sayacını yönetir.
    time > 0 olduğu sürece ekranda zamanı gösterir
    ve 1 saniye sonra countdown fonksiyonunu yeniden çağırır.
    time == 0 olduğunda game_over değişkenini True yapar,
    tüm turtle'ları gizler ve 'Game Over' mesajını yazar.
    """
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()

    top_height = screen.window_height()
    y = top_height * 0.91

    countdown_turtle.setpos(0, 240)

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)

def start_game_up():
    """
    Oyunu başlatan ana fonksiyon:
    - Ekran animasyonunu kapatır (tracer(0)).
    - Skor turtle'ını, turtle objelerini ve geri sayımı ayarlar.
    - Ardından tracer(1) ile animasyonu yeniden başlatır.
    """
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(20)
    turtle.tracer(1)

start_game_up()
turtle.mainloop()