using System;
using System.Runtime.InteropServices;
using System.Xml.Serialization;
class numberguess
{
    static void Main(string[] args)
    {
        int high_score = 0;
        bool play_again = true;
        while (play_again)
        {
            void playagain()
                            {
                            bool repeat = true;
                            while (repeat)
                            {
                            Console.Write("Would you like to play again\n1. Yes\n2. No\n");
                            string decision = Console.ReadLine();
                            if (decision == "1")
                            {
                                play_again = true;
                                repeat = false;
                            }
                            else if (decision == "2")
                            {
                                play_again = false;
                                repeat = false;
                                
                            }
                            else
                            {
                                Console.Write("Choose between the options 1 and 2 below: ");
                                repeat = true;
                            }
                            }
                            }
            void guesslogic(int trials,int level,int hint_trial)
                {
                Random rand = new Random();
                int number = rand.Next(1,21);
                Console.WriteLine($"You have {trials} trials to guess a number between 1 and 20");
                Console.Write("What is the number: ");
                try
                {
                    int guess = Convert.ToInt16(Console.ReadLine());
                    while (trials > 0)
                    {
                        if (number == guess)
                        {
                            Console.WriteLine($"You`ve guessed it\n{guess} was the number");
                            int score = (1000 + (100 * trials))*level;
                            Console.WriteLine($"Your score is {score}");
                            if (score > high_score)
                            {
                                high_score = score;
                                Console.WriteLine("NEW HIGH SCORE!!");
                            }
                            playagain();
                            return;
                        }
                        else
                        {
                            trials--;
                            Console.WriteLine($"Wrong\n{guess} is not the number");
                            if (trials > 0)
                            {
                                if (trials == hint_trial)
                                {
                                    if (number % 2 == 0)
                                    {
                                        Console.WriteLine("Hint: The number is even");
                                    }
                                    else
                                    {
                                        Console.WriteLine("Hint: The number is odd");
                                    }
                                }
                                int difference = Math.Abs(guess - number);
                                if (difference <= 5)
                                {
                                    Console.WriteLine("Very hot(Within 5)");
                                }
                                else if (difference <= 10)
                                {
                                    Console.WriteLine("Warm(Within 10)");
                                }
                                else if (difference <= 15)
                                {
                                    Console.WriteLine("Cold(within 15)");
                                }
                                else
                                {
                                    Console.WriteLine("Freezing(More than 15 away)");
                                }
                                Console.Write($"You have {trials} attempts left\nWhat is the number: ");
                                guess = Convert.ToInt16(Console.ReadLine());
                            }
                            else
                            {
                                Console.WriteLine("YOU LOSE\nYou`ve used up all your attempts");
                                playagain();
                                return;
                            }
                        }
                    }
                }
                catch (FormatException ex)
                {
                    Console.WriteLine("Invalid input type");
                }
                }
            Console.WriteLine("What level would you like to play:\n1. Easy\n2. Medium\n3. Difficult");
            string choice = Console.ReadLine();
            if (choice == "1")
            {
                guesslogic(10,1,5);
            }
            else if (choice == "2")
            {
                guesslogic(7,2,3);
            }
            else if (choice == "3")
            {
                guesslogic(4,3,2);
            }
            else
            {
                Console.WriteLine("Choose between the options 1,2 and 3 below ");
            }
        }
 }  
}