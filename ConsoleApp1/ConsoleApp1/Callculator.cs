using System;
class Calculator
{
    static void Main(string[] args)
    {
        Console.WriteLine("First number: ");
        double num_1 = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Which operation(*,/,+,-) ");
        string operation = Console.ReadLine();
        Console.WriteLine("Second number: ");
        double num_2 = Convert.ToDouble(Console.ReadLine());
        if (operation == "*")
        {
            Console.WriteLine($"{num_1} * {num_2} = {num_1 * num_2}");
        }
        else if (operation == "/")
        {
            Console.WriteLine($"{num_1} / {num_2} = {num_1 / num_2}");
        }
        else if (operation == "+")
        {
            Console.WriteLine($"{num_1} + {num_2} = {num_1 + num_2}");
        }
        else if (operation == "-")
        {
            Console.WriteLine($"{num_1} - {num_2} = {num_1 - num_2}");
        }
        else
        {
            Console.WriteLine("Choose one of the operations: +,-,/,*");
        }
    }
}