# id generator program

Final project of course 'next.py'
https://campus.gov.il/course/course-v1-cs-gov-cs-nextpy102/

My Certificate of Completion this course:
https://courses.campus.gov.il/certificates/ce6c457e33aa4d658df1fa45fd6010a6

You were asked to help the Population Authority write a plan that generates ID numbers - a plan that assigns a new ID number to every Israeli resident or citizen upon registration of his birth, or upon his immigration to Israel.

An ID number consists of nine digits. Of course, not every nine-digit number is a valid ID number.

Below is a description of the identity check process of an ID card. For the purpose of the example, we will check the correctness of the following ID card: 123456782.

Step One: Multiply each digit in the ID by 1 or 2 depending on its position in the number. A digit that is in an odd position will multiply by 1 and a digit that is in an even position will multiply by 2. for example:

2 8 7 6 5 4 3 2 1 Digit
1 2 1 2 1 2 1 2 1 Doubling in -
2 16 7 12 5 8 3 4 1 Result

Step Two: We will go over any number obtained as a result of the multiplication operation and check if it is greater than 9. If so, we will connect his two digits. Otherwise, we'll leave it as it is. For example, 16 is greater than 9, so we add its two digits (1 + 6) and get 7.

Step Three: We will sum up all the numbers that came out in the result.

Fourth stage: We will check whether the number obtained as a result of the third stage is divisible by 10 with no remainder. If so, the ID number is correct, otherwise - incorrect.

An example of any ID card verification process:

2 8 7 6 5 4 3 2 1 Digit
1 2 1 2 1 2 1 2 1 Doubling in -
2 16 7 12 5 8 3 4 1 Result
2 7 7 3 5 8 3 4 1 Add digits to numbers greater than 9
Sum of numbers
Is 40 divided by 10 with no remainder? Yes. Correct ID number!
