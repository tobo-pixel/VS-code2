using System;
namespace Anapp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("What is your score: ");
            double score = Convert.ToDouble(Console.ReadLine());
            if (score >= 70 && score <= 100)
            {
                Console.WriteLine($"{score} is an A");
            }
            else if (score >= 60)
            {
                Console.WriteLine($"{score} is a B");
            }
            else if (score >= 50)
            {
                Console.WriteLine($"{score} is a C");
            }
            else if (score >= 45)
            {
                Console.WriteLine($"{score} is a D");
            }
            else if (score >= 40)
            {
                Console.WriteLine($"{score} is an E");
            }
            else if (score >= 0)
            {
                Console.WriteLine($"{score} is a Fail");
            }
            else
            {
                Console.WriteLine("Score must fall within 0-100 range");
            }
        }
    }
}
