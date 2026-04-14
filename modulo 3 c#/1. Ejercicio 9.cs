using System;

namespace Combinado
{
    class Numero
    {
        static void Main()
        {
            NumeroY();
            NumeroX();
        }

        public static void NumeroY()
        {
            for (int numero = 1; numero <= 50; numero++)
            {
                if (numero % 2 == 0)
                {
                    Console.WriteLine(numero);
                }
            }
        }

        public static void NumeroX()
        {
            int numero = 10;

            while (numero >= 1)
            {
                Console.WriteLine(numero);
                numero--;
            }

            Console.WriteLine("¡Despegue!");
        }
    }
}