using System;
class Numberguess
{
    static void Main(string[] args)
    {
        Random  rand = new Random();
        int number = rand.Next(1,11);
        int trials = 4;
        Console.Write("Guess a number between 1 and 10: ");
        int guess = Convert.ToInt32(Console.ReadLine());
        while (trials > 0)
        {
            if (guess == number)
            {
                Console.WriteLine($"You`ve guessed it\n{guess} was the number");
                break;
            }
            else 
            {
                trials--;
                if (trials == 0)
                {
                    Console.WriteLine($"Wrong\n{guess} is not the number");
                    Console.WriteLine("You have used up all your attempts");
                    break;
                }
                else
                {
                    Console.WriteLine($"Wrong\n{guess} is not the number\nYou have {trials} trials left");
                    guess = Convert.ToInt16(Console.ReadLine());
                }
            }
        }    
    }
}