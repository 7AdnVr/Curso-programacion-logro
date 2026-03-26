# Juego: El Camino del Valhalla 🛡️
print("\n" + "="*30)
print(" ⚔️  El Camino del Valhalla 🛡️")
print("="*30 + "\n")
print(f"Eres un joven guerrero vikingo que despierta en una aldea destruida tras un ataque enemigo🔥.")
print("No recuerdas bien qué ocurrió, pero sabes que debes sobrevivir… y descubrir quién atacó tu hogar⚔️ .")

decision1 = input("¿Qué eliges para comenzar tu viaje? HACHA 🪓 o ESCUDO 🛡️  >").lower()

# Ruta del Hacha Nivel 2
if decision1 == "hacha":

    print("\nAprietas el hacha y te adentras en el bosque oscuro...\nUn ruido rompe el silencio entre los árboles.\n")
    decision2 = input("¿Qué haces? INVESTIGAR 🔍 , HUIR 🏃‍♂️  y HACER UNA EMBOSCADA ⚔️ ? >").lower()

 # Ruta de investigar Nivel 3
    if decision2 == "investigar":

        print("\nTe acercas lentamente... y descubres a un guerrero herido. Te mira con desconfianza.\n")
        decision3 = input('¿Qué decides hacer? IGNORAR 🚶 o INTERROGAR ❓? >').lower()

 # Ruta de Ignorar Nivel 4
        if decision3 == "interrogar":

            print('\nEl guerrero respira con dificultad... te entrega información sobre los atacantes. Ahora tienes una decisión difícil')
            decision4 = input('Qué haces? MATARLO ⚔️  o PERDONARLO 🤝 ? >').lower()

            if decision4 == "matarlo":
                 
                  print('\nSin dudarlo, acabas con su vida.')
                  print('Con el mapa en tus manos, sigues el camino hacia el norte... \nTras horas de viaje, finalmente ves humo en la distancia. \nHas encontrado el campamento enemigo. 🔥 Debes actuar con cuidado.\n')
                  decision5 = input('¿Qué haces? INFILTRARSE 🕶️ , ATACAR ⚔️  o OBSERVAR 👀 ? >').lower()

                  if decision5 == "atacar":
                        print('\nLleno de ira, corres hacia el campamento sin pensar... Los enemigos te rodean rápidamente. \nLuchas con valentía, pero estás en desventaja. Caes en combate. \nTu venganza nunca se cumple. 😔')

                  elif decision5 == "infiltrarse":
                   print('\nTe mueves en silencio entre las sombras... Encuentras al líder enemigo descansando. \nSin hacer ruido, levantas tu hacha... Y acabas con él de un solo golpe. \nHas vengado tu aldea. El Camino al Valhalla te espera. 🛡️')

                  elif decision5 == "observar":
                   print('\nDecides observar antes de actuar... Escuchas que el líder no actuó solo. \nEsto es parte de algo más grande. Te retiras en silencio. \nTu venganza no ha terminado… apenas comienza.')

        elif decision3 == "ignorar":
       
             print('\nTe ataca por detrás, y terminas muerto. Tu venganza nunca se cumple. 😔')   

    elif decision2 == "huir":
        print("\nEl miedo se apodera de ti... decides huir y abandonar tu venganza. \nTe alejas de tu aldea sin mirar atrás. \nEl honor de un vikingo se pierde... Tu historia termina aquí.\n")

    elif decision2 == "hacer una emboscada":
        print("\nSientes la presencia de enemigos cerca... \nEn vez de huir o investigar, decides preparar una emboscada. \nTe ocultas y esperas el momento perfecto para atacar. \n")
        decision22 = input('¿Qué haces? ATACAR AHORA ⚔️, ESPERAR ⏳ o RETIRARTE 🔙?').lower()
         
        if decision22 == "atacar ahora":
         print('\nSaltas de tu escondite con furia... \nTomas a los enemigos por sorpresa, pero son más de los que pensabas. \nTe rodean rápidamente. \nLuchas con honor, pero caes en combate. \nTu venganza termina aquí."')

        elif decision22 == "esperar":
         print('\nDecides esperar pacientemente... \nLos enemigos se dispersan, y logras eliminar a varios de ellos sin ser detectado. \nFinalmente, encuentras al líder enemigo solo. \nCon un golpe certero, lo derrotas. \nHas vengado tu aldea. El Camino al Valhalla te espera. 🛡️')

        elif decision22 == "retirarte":
         print('\nDecides que no es el momento adecuado... \nTe retiras sin hacer ruido. \nPero la oportunidad se pierde. \nLa duda te acompañará siempre. \nNunca completaste tu venganza. 😔')

elif decision1 == "escudo":
   
   print('\nLevantas tu escudo y avanzas con cautela... \nPrefieres defenderte antes que atacar.\nEl camino te lleva hasta un enfrentamiento directo con un enemigo.')
   decision11 = input('¿Qué haces? DEFENDER 🛡️ , CONTRAATACAR ⚔️  o HUIR 🏃‍♂️ ? >').lower()

   if decision11 == "contraatacar":
          
          print('\nAprovechas una apertura en la defensa del enemigo... \nContraatacas con fuerza, sorprendiendo a tu oponente. \nLogras derrotarlo, pero sabes que esto es solo el comienzo de tu venganza. \nSigues adelante, decidido a encontrar al líder enemigo.')
          print('\nMientras recuperas el aliento, revisas el cuerpo del enemigo...\nEntre sus pertenencias encuentras un mapa antiguo. 🗺️\nHay una marca clara en el norte.\nEse debe ser el lugar donde se oculta el líder.\n\nSientes el peso de tu misión...')
          decision111 = input('¿Qué decides hacer? SEGUIR EL MAPA 🧭 o RENUNCIAR ❌ a tu venganza? >').lower()

          if decision111 == "seguir el mapa":
                
                print('\nSigues el mapa con determinación... \nDespués de días de viaje, finalmente llegas a una fortaleza oculta en las montañas. 🏰\nSabes que el líder enemigo está dentro. \nTe preparas para la batalla final...')
                decision1111 = input('¿Qué haces? ASALTAR LA FORTALEZA ⚔️ , ESPERAR PACIENTEMENTE ⏳ o BUSCAR UNA ENTRADA SECRETA 🕵️ ? >').lower()

                if decision1111 == "asaltar la fortaleza":
                   print('\nCon un grito de guerra, corres hacia la fortaleza sin dudar... \nLos guardias te ven y suenan las alarmas. 🔔 \nLuchas con toda tu fuerza, derribando a varios enemigos... \npero son demasiados. \nRodeado y herido, caes de rodillas. \nAun así, sonríes... luchaste con honor. \nTu historia termina en batalla. \nEl Valhalla te recibe. 🛡️\n')

                elif decision1111 == "esperar pacientemente":
                    print("\nDecides observar desde la distancia... \nHoras pasan, y notas un cambio de guardia. \nEl cansancio debilita la defensa del lugar. \nAprovechas el momento perfecto y entras sin ser visto. \nEncuentras al líder enemigo descansando. \nSin hacer ruido, te acercas lentamente... \nCon un golpe preciso, acabas con él. \nTu venganza está completa. \nEl honor de tu aldea ha sido restaurado. \nTu nombre vivirá por siempre en el Valhalla. 🛡️🔥 \n")

                elif decision1111 == "buscar una entrada secreta":
                    print("\nRodeas la fortaleza en silencio... \nTras explorar un poco, descubres una entrada oculta bajo unas rocas. \nTe adentras en la oscuridad... \npero es una trampa. \nEl suelo cede bajo tus pies. \nCaes en un pozo profundo. \nNadie escucha tu caída. \nTu historia termina en la oscuridad. 😔\n")