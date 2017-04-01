import sqlite3

def store_pontos(jogador_id, pontos):
    conn=sqlite3.connect('/home/pi/genius-pi/db.sqlite3')
    curs=conn.cursor()
    curs.execute('''update play_jogador set
                        pontos = ?,
                        pontos_rodada = ?,
                        num_jogadas = num_jogadas + 1
                        where id = ?''', (pontos, pontos, jogador_id))
    conn.commit()
    conn.close()

def store_pontos_tempo(jogador_id, pontos, tempo):
    conn=sqlite3.connect('/home/pi/genius-pi/db.sqlite3')
    curs=conn.cursor()
    curs.execute('''update play_jogador set
                        pontos = pontos + ?,
                        pontos_rodada = ?,
                        tempo = tempo + ?,
                        num_jogadas = num_jogadas + 1
                        where id = ?''', (pontos, pontos, tempo, jogador_id))

    curs.execute('''update play_jogador set
                        menor_tempo = ?
                        where (menor_tempo > ? OR menor_tempo = 0) AND id = ?''', (tempo, tempo, jogador_id))
    conn.commit()
    conn.close()
