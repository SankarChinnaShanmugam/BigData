using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.RegularExpressions;

namespace PatternMatch
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length == 0)
            {
                System.Console.WriteLine("Please enter a Input strings.");
                return;
            }
            else if (args.Length == 2)
            {
                Console.WriteLine("Welcome to Finding the Pattern Matching between two strings");
                Console.WriteLine("Program Started");
                string str_FirstString = string.Empty;
                string str_SecondString = string.Empty;
                Console.WriteLine("Enter the Values of Strings");
                Console.WriteLine("Enter the first string value");
                str_FirstString = args[0];
                str_FirstString = str_FirstString.Trim();
                Console.WriteLine("You have entered first string value as: " + str_FirstString);
                Console.WriteLine("Enter the second Value");
                str_SecondString = args[1];
                str_SecondString = str_SecondString.Trim();
                Console.WriteLine("You have entered second string value as: " + str_SecondString);
                Console.WriteLine("Validation are started");
                try
                {
                    Console.WriteLine("Method input_Validation started");
                    fun_Input_Validation(str_FirstString, str_SecondString);
                    Console.WriteLine("Method input_Validation Completed");

                    Console.WriteLine("Method fun_PM started");

                    bool PM = fun_PM(str_FirstString.ToLower(), str_SecondString.ToLower());
                    Console.WriteLine("The result of the PM: " + PM);

                    Console.WriteLine("Method fun_PM Completed");
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Something went wrong: " + ex.Message);
                }
                finally
                {
                    Console.WriteLine("Program completed ");
                }
            }
            else
            {
                Console.WriteLine("Program exited!. Please pass valid arguments to the program.");
            }
        }

        static private void fun_Input_Validation(string FirstString, string SecondString)
        {
            Console.WriteLine("Method input_Validation Entered");
            //logging.info("fun_Input_Validation Started")
            if (string.IsNullOrEmpty(FirstString))
            {
                Console.WriteLine("Input mandatory filed not passed");
                //logging.warning("Input one is empty")
                throw new Exception("Input values is mandatory");               
            }
            if (!Regex.IsMatch(FirstString,"^[A-Za-z]*$", RegexOptions.IgnoreCase))
            {
                Console.WriteLine("Error! Make sure you only use letters in first string");
                throw new Exception("Make sure you only use letters in first string");
            }

            if (string.IsNullOrEmpty(SecondString))
            {
                Console.WriteLine("Input mandatory filed not passed");
                //logging.warning("Input two is empty")
                throw new Exception("Input values is mandatory");
            }
            if (!Regex.IsMatch(SecondString, "^[A-Za-z.*]*$", RegexOptions.IgnoreCase))
            {
                Console.WriteLine("Error! Make sure you only use letters and special characters of *. in second string");
                throw new Exception("Make sure you only use letters and special characters of *. in second string");
            }

            //logging.info("fun_Input_Validation Completed")
            Console.WriteLine("Method input_Validation Exited");
        }

        static private bool fun_PM(string FirstString, string SecondString)
        {
            Console.WriteLine("fun_PM Started");
            StringBuilder patternString = new StringBuilder();
            //logging.info("fun_PM Started")
            string delimiter_Astric = "*";
            string delimiter_Dot = ".";
            char[] patternChar =new char[FirstString.Length];

            #region Second string  pattern direcly matches with first string  
            if (SecondString.ToString().Contains(FirstString))
                return true;
            #endregion

            #region S2 having single Characters
            if (SecondString.Length == 1 && SecondString.Contains(delimiter_Dot))
            {
                if (FirstString.Length == 1)
                {
                    return true;
                }
            }
            else if (SecondString.Length == 1 && SecondString.Contains(delimiter_Astric))
            {
                return false;
            }
            #endregion 

            List<string> pattenSplit = SecondString.Split(new[] { delimiter_Astric, delimiter_Dot },StringSplitOptions.RemoveEmptyEntries).ToList();

            #region  If S2 having only one splitter 
            if (pattenSplit?.Count == 1)
            {
                if (SecondString.Contains("."))
                {
                    foreach (char val in SecondString)
                    {
                        if (val.Equals('.'))
                        {
                            int indChar = SecondString.IndexOf(".");
                            char indValueOfFirstString = FirstString.Select((v, ind) => new { v, ind }).Where(a => a.ind.Equals(indChar)).First().v;
                            patternString.Append(indValueOfFirstString);
                        }
                        else
                        {
                            patternString.Append(val);
                        }
                    }
                    if (patternString.ToString().Contains(FirstString))
                        return true;
                }
                else if (SecondString.Contains("*"))
                {
                    for (int i = 0; i < FirstString.Length; i++)
                    {
                        bool isenterdSS = false;
                        int tempIndex = 0;
                        foreach (char val in SecondString)
                        {
                            if (val.Equals('*') && tempIndex == 0)
                            {
                                return false;
                            }
                            else if (val.Equals('*') && i != 0)
                            {
                                isenterdSS = true;
                                char indValueOfFirstString = SecondString.Select((v, ind) => new { v, ind }).Where(a => a.ind.Equals(tempIndex - 1)).First().v;
                                patternString.Append(indValueOfFirstString);
                                break;
                            }
                            tempIndex++;
                        }
                        if (!isenterdSS)
                            patternString.Append(FirstString[i]);
                    }
                    if (patternString.ToString().Contains(FirstString))
                        return true;
                    else
                        return false;
                }
                else if (FirstString.Equals(SecondString))
                    return true;
            }
            #endregion

            #region If S2 having multiple splitter 
            else if (pattenSplit?.Count > 1)
            {
                int tempIndex = 0;
                string lastValue = string.Empty;
                foreach (char val in SecondString)
                {
                    if (val.Equals('*'))
                    {
                        if (val.Equals('*') && tempIndex != 0)
                        {
                            try
                            {
                                //there are chances of index out of range values 
                                char indValueOfFirstString = SecondString.Select((v, ind) => new { v, ind }).Where(a => a.ind.Equals(tempIndex - 1)).First().v;
                                if (!indValueOfFirstString.Equals('*'))
                                {
                                    lastValue = indValueOfFirstString.ToString();
                                    patternString.Append(indValueOfFirstString);
                                }
                                else
                                {
                                    patternString.Append(lastValue);
                                }

                            }
                            catch
                            {
                                //There are chances of multiple number of * in continuously in last index
                                patternString.Append(lastValue);
                            }
                        }
                    }
                    else if (val.Equals('.'))
                    {
                        int indChar = SecondString.IndexOf(".");
                        try
                        {
                            // //there are chances of index out of range values 
                            char indValueOfFirstString = FirstString.Select((v, ind) => new { v, ind }).Where(a => a.ind.Equals(indChar)).First().v;
                            lastValue = indValueOfFirstString.ToString();
                            patternString.Append(indValueOfFirstString);
                        }
                        catch
                        {
                            //There are chances of multiple number of . in continuously in last index
                            patternString.Append(lastValue);
                        }
                    }
                    else
                    {
                        //Only alphabets
                        lastValue = val.ToString();
                        patternString.Append(val);
                    }
                    tempIndex++;
                }
                if (patternString.ToString().Contains(FirstString))
                    return true;
            }
            #endregion

            #region pattenSplit?.Count == 0
            else if (pattenSplit?.Count == 0)
            {
                if (SecondString.Contains("."))
                {
                    int tempIndex = 0;
                    foreach (char val in SecondString)
                    {
                        if (val.Equals('.'))
                        {
                            int indChar = SecondString.IndexOf(".");
                            char indValueOfFirstString = FirstString.Select((v, ind) => new { v, ind }).Where(a => a.ind.Equals(indChar)).First().v;
                            patternString.Append(indValueOfFirstString);
                        }
                        else if (val.Equals('*'))
                        {
                            if (val.Equals('*') && tempIndex == 0)
                            {
                                return false;
                            }
                            else
                            {
                                int indChar = SecondString.IndexOf("*");
                                char indValueOfFirstString = FirstString.Select((v, ind) => new { v, ind }).Where(a => a.ind.Equals(indChar)).First().v;
                                patternString.Append(indValueOfFirstString);
                            }
                        }
                        else
                        {
                            patternString.Append(val);
                        }
                        tempIndex++;
                    }
                    if (patternString.ToString().Contains(FirstString))
                        return true;
                    else
                        return false;
                }
                else if (SecondString.Contains("*"))
                {
                    int tempIndex = 0;
                    foreach (char val in SecondString)
                    {
                        if (val.Equals('.'))
                        {
                            int indChar = SecondString.IndexOf(".");
                            char indValueOfFirstString = FirstString.Select((v, ind) => new { v, ind }).Where(a => a.ind.Equals(indChar)).First().v;
                            patternString.Append(indValueOfFirstString);
                        }
                        else if (val.Equals('*'))
                        {
                            if (val.Equals('*') && tempIndex == 0)
                            {
                                return false;
                            }
                            else
                            {
                                int indChar = SecondString.IndexOf("*");
                                char indValueOfFirstString = FirstString.Select((v, ind) => new { v, ind }).Where(a => a.ind.Equals(indChar)).First().v;
                                patternString.Append(indValueOfFirstString);
                            }
                        }
                        else
                        {
                            patternString.Append(val);
                        }
                    }
                }
                else if (FirstString.Equals(SecondString))
                    return true;
            }
            #endregion
            else
                return false;

            return false;
        }
    }
}
